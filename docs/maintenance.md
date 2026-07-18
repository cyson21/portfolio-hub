# 공개 자료 유지보수

공개 파일은 로컬 작업 공간의 생성 산출물에서 허용 목록만 동기화합니다.

```bash
python3 scripts/sync_from_workspace.py --source /path/to/side-projects
python3 scripts/verify_public_assets.py
```

`main` 반영 후 GitHub Actions가 검증하고 `latest` 릴리스의 고정 파일명을 교체합니다. `artifacts/manifest.json`은 공개 파일의 SHA-256과 크기를 기록합니다. `pdftotext`가 PATH에 없다면 `PDFTOTEXT_BIN`으로 절대경로를 지정합니다.

## 공개 범위

- 포함: 전화번호를 제외한 공개용 이력서, 통합·프로젝트별 포트폴리오, 공개 프로젝트 링크
- 제외: 원본 일감, 지원 공고, 내부 작업 기록, 비공개 검토 문서, 로컬 경로
