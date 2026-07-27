#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


MAPPINGS = {
    "resumes/generated/resume-public.pdf": "resume.pdf",
    "resumes/generated/resume-public.html": "resume.html",
    "resumes/generated/resume-public-ats.pdf": "resume-ats.pdf",
    "resumes/generated/resume-public-ats.html": "resume-ats.html",
    "portfolio/portfolio-complete.html": "portfolio-complete.html",
    "portfolio/portfolio-index.html": "portfolio-index.html",
    **{
        f"portfolio/project-{number:02d}-{slug}-portfolio.{extension}":
        f"project-{number:02d}-{slug}-portfolio.{extension}"
        for number, slug in [
            (1, "stockrush"),
            (2, "enterprise-policy-rag"),
            (3, "member-event-consistency"),
            (4, "ai-gateway"),
            (5, "cdc-data-platform"),
            (6, "fashion-personalization-platform"),
        ]
        for extension in ["html"]
    },
}


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync approved portfolio artifacts into this public repository.")
    parser.add_argument("--source", type=Path, required=True, help="side-projects workspace root")
    args = parser.parse_args()

    source = args.source.expanduser().resolve()
    target_root = Path(__file__).resolve().parents[1]
    artifact_root = target_root / "artifacts"
    artifact_root.mkdir(parents=True, exist_ok=True)

    expected_names = set(MAPPINGS.values())
    for path in artifact_root.iterdir():
        if path.is_file() and path.name not in expected_names and path.name != "manifest.json":
            path.unlink()

    missing: list[str] = []
    for source_name, output_name in MAPPINGS.items():
        source_path = source / source_name
        if not source_path.is_file():
            missing.append(source_name)
            continue
        temporary = artifact_root / f".{output_name}.tmp"
        shutil.copy2(source_path, temporary)
        temporary.replace(artifact_root / output_name)

    if missing:
        raise SystemExit("Missing generated artifacts:\n- " + "\n- ".join(missing))

    assets = []
    for output_name in sorted(expected_names):
        output_path = artifact_root / output_name
        assets.append({
            "name": output_name,
            "path": f"artifacts/{output_name}",
            "sha256": digest(output_path),
            "bytes": output_path.stat().st_size,
        })

    manifest = {"schemaVersion": 1, "assets": assets}
    manifest_path = artifact_root / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Synced {len(assets)} approved artifacts into {artifact_root}")


if __name__ == "__main__":
    main()
