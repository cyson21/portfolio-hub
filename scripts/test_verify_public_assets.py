from __future__ import annotations

import importlib.util
import os
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "verify_public_assets.py"
SPEC = importlib.util.spec_from_file_location("verify_public_assets", MODULE_PATH)
assert SPEC and SPEC.loader
verify_public_assets = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify_public_assets)


class VerifyPublicAssetsTests(unittest.TestCase):
    def test_scan_text_allows_phone_in_user_approved_resume_pdf(self) -> None:
        findings: list[str] = []

        verify_public_assets.scan_text(
            "resume.pdf",
            "연락처 010-0000-0000",
            findings,
            allow_phone=True,
        )

        self.assertNotIn("resume.pdf: Korean phone number", findings)

    def test_scan_text_rejects_phone_without_resume_allowance(self) -> None:
        findings: list[str] = []

        verify_public_assets.scan_text(
            "portfolio-index.html",
            "연락처 010-0000-0000",
            findings,
        )

        self.assertIn("portfolio-index.html: Korean phone number", findings)

    def test_scan_text_allows_user_approved_kakao_email(self) -> None:
        findings: list[str] = []

        verify_public_assets.scan_text(
            "resume.pdf",
            "cyson21@kakao.com",
            findings,
        )

        self.assertNotIn("resume.pdf: unapproved email cyson21@kakao.com", findings)

    def test_extract_pdf_text_falls_back_to_pypdf_without_pdftotext(self) -> None:
        with patch.dict(os.environ, {"PDFTOTEXT_BIN": ""}, clear=False):
            with patch.object(verify_public_assets.shutil, "which", return_value=None):
                text = verify_public_assets.extract_pdf_text(ROOT / "artifacts" / "resume.pdf")

        self.assertGreater(len(text), 100)


if __name__ == "__main__":
    unittest.main()