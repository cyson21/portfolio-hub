# 공개 자료 유지보수

공개 파일은 로컬 작업 공간의 생성 산출물에서 허용 목록만 동기화합니다.

```bash
python3 scripts/sync_from_workspace.py --source /path/to/side-projects
python3 scripts/verify_public_assets.py
```

`main` 반영 후 GitHub Actions가 검증하고 `latest` 릴리스의 고정 파일명을 교체합니다. manifest 허용 목록에서 빠진 기존 릴리스 자산도 이때 삭제합니다. `artifacts/manifest.json`은 공개 파일의 SHA-256과 크기를 기록합니다. `pdftotext`가 PATH에 없다면 `PDFTOTEXT_BIN`으로 절대경로를 지정합니다.

## 공개 범위

- 포함: 전화번호를 제외한 이력서 PDF/HTML, 통합·인덱스·프로젝트별 포트폴리오 HTML, 공개 프로젝트 링크
- 제외: 포트폴리오 PDF, 원본 일감, 지원 공고, 내부 작업 기록, 비공개 검토 문서, 로컬 경로

이력서는 PDF를 제출·다운로드 기준으로 운영하고, 포트폴리오는 웹사이트와 HTML을 공개 기준으로 운영합니다. 포트폴리오 PDF는 로컬 렌더링 검증용이므로 이 저장소와 릴리스에 동기화하지 않습니다.
