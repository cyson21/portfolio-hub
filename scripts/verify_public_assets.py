#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
MANIFEST = ARTIFACTS / "manifest.json"
ALLOWED_EMAILS = {"cyson21@kakao.com"}
REQUIRED_PUBLIC_ASSETS = {
    "resume.pdf",
    "portfolio-complete.html",
    "portfolio-index.html",
    "project-01-stockrush-portfolio.html",
    "project-02-enterprise-policy-rag-portfolio.html",
    "project-03-member-event-consistency-portfolio.html",
    "project-04-ai-gateway-portfolio.html",
    "project-05-cdc-data-platform-portfolio.html",
    "project-06-fashion-personalization-platform-portfolio.html",
}
BANNED_TEXT = [
    ("local absolute path", re.compile(r"/Users/")),
    ("file URL", re.compile(r"file://", re.IGNORECASE)),
    ("loopback address", re.compile(r"127\.0\.0\.1|localhost", re.IGNORECASE)),
    ("Korean phone number", re.compile(r"\b01[016789][-.\s]?\d{3,4}[-.\s]?\d{4}\b")),
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
]


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def scan_text(name: str, text: str, findings: list[str]) -> None:
    for label, pattern in BANNED_TEXT:
        if pattern.search(text):
            findings.append(f"{name}: {label}")
    for email in re.findall(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", text, re.IGNORECASE):
        if email.lower() not in ALLOWED_EMAILS:
            findings.append(f"{name}: unapproved email {email}")


def extract_pdf_text(path: Path) -> str:
    executable = os.environ.get("PDFTOTEXT_BIN") or shutil.which("pdftotext")
    if not executable:
        raise RuntimeError("pdftotext is required to verify PDF text")
    with tempfile.TemporaryDirectory(prefix="portfolio-pdf-text-") as directory:
        output = Path(directory) / "document.txt"
        completed = subprocess.run(
            [executable, "-layout", str(path), str(output)],
            check=False,
            capture_output=True,
            text=True,
        )
        if completed.returncode != 0:
            raise RuntimeError(completed.stderr.strip() or f"pdftotext failed for {path.name}")
        return output.read_text(encoding="utf-8", errors="replace")


def main() -> None:
    findings: list[str] = []
    if not MANIFEST.is_file():
        raise SystemExit("artifacts/manifest.json is missing")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    entries = manifest.get("assets") if isinstance(manifest, dict) else None
    if manifest.get("schemaVersion") != 1 or not isinstance(entries, list):
        raise SystemExit("artifacts/manifest.json has an invalid schema")

    expected = {entry.get("name") for entry in entries}
    actual = {path.name for path in ARTIFACTS.iterdir() if path.is_file() and path.name != "manifest.json"}
    if expected != actual:
        findings.append(f"artifact set differs: expected={sorted(expected)} actual={sorted(actual)}")
    missing_required = REQUIRED_PUBLIC_ASSETS - expected
    if missing_required:
        findings.append(f"required public assets are missing: {sorted(missing_required)}")

    for entry in entries:
        name = entry.get("name")
        path = ARTIFACTS / str(name)
        if not path.is_file():
            findings.append(f"missing artifact: {name}")
            continue
        if entry.get("path") != f"artifacts/{name}":
            findings.append(f"invalid manifest path: {name}")
        if entry.get("bytes") != path.stat().st_size:
            findings.append(f"size differs: {name}")
        if entry.get("sha256") != digest(path):
            findings.append(f"sha256 differs: {name}")
        if path.suffix == ".pdf":
            if not path.name.startswith("resume"):
                findings.append(f"portfolio PDF is not allowed in public artifacts: {name}")
            if path.read_bytes()[:5] != b"%PDF-":
                findings.append(f"invalid PDF header: {name}")
            else:
                try:
                    scan_text(str(name), extract_pdf_text(path), findings)
                except RuntimeError as error:
                    findings.append(f"{name}: {error}")
        if path.suffix == ".html":
            text = path.read_text(encoding="utf-8", errors="replace")
            if "<html" not in text.lower() or "</html>" not in text.lower():
                findings.append(f"invalid HTML document: {name}")
            scan_text(str(name), text, findings)

    if findings:
        raise SystemExit("Public artifact verification failed:\n- " + "\n- ".join(findings))
    print(f"Public artifact verification passed: {len(entries)} assets")


if __name__ == "__main__":
    main()
