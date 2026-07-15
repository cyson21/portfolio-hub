# 손찬양 | Backend Engineering Portfolio

Java/Spring을 중심으로 동시성, 부분 실패 복구, 이벤트 전달과 데이터 흐름을 구현하고 검증한 프로젝트 모음입니다.

## 바로 보기

| 이력서 PDF | 웹 포트폴리오 | 통합 포트폴리오 PDF |
|---|---|---|
| [resume.pdf](https://github.com/cyson21/portfolio-hub/releases/download/latest/resume.pdf) | [cyson21.github.io](https://cyson21.github.io/) | [portfolio-complete.pdf](https://github.com/cyson21/portfolio-hub/releases/download/latest/portfolio-complete.pdf) |

## 직무 주제별 프로젝트

| 주제 | 프로젝트 | 확인할 구현 |
|---|---|---|
| 분산 상태와 복구 | [StockRush](https://github.com/cyson21/stockrush) · [웹 사례](https://cyson21.github.io/projects/stockrush/) | Saga, Transactional Outbox, 소비자 멱등성, Kafka 중단 복구 |
| 동시성과 데이터 정합성 | [Member Event Consistency](https://github.com/cyson21/member-event-consistency) · [웹 사례](https://cyson21.github.io/projects/member-event-consistency/) | PostgreSQL 제약·행 잠금, Redis lock, RabbitMQ worker |
| 공통 API 인프라 | [AI Gateway](https://github.com/cyson21/ai-gateway) · [웹 사례](https://cyson21.github.io/projects/ai-gateway/) | tenant 인증, quota, cache, routing, provider fallback |
| 변경 데이터와 replay | [CDC Data Platform](https://github.com/cyson21/cdc-data-platform) · [웹 사례](https://cyson21.github.io/projects/cdc-data-platform/) | Debezium CDC, event ledger, retry·DLQ·replay |
| 권한 기반 검색 | [Enterprise Policy RAG](https://github.com/cyson21/enterprise-policy-rag) · [웹 사례](https://cyson21.github.io/projects/enterprise-policy-rag/) | SQL 권한 선필터, 답변 거절, citation, 평가 |
| 이벤트 기반 개인화 | [Fashion Personalization Platform](https://github.com/cyson21/fashion-personalization-platform) · [웹 사례](https://cyson21.github.io/projects/fashion-personalization-platform/) | 멱등 이벤트, 설명 가능한 ranking, batch snapshot |

각 프로젝트에서 실패 조건을 어떻게 막았고 어느 범위까지 검증했는지는 저장소와 웹 사례에서 확인할 수 있습니다.

## 공개 자료 유지보수

공개 파일은 로컬 작업 공간의 생성 산출물에서 허용 목록만 동기화합니다.

```bash
python3 scripts/sync_from_workspace.py --source /path/to/side-projects
python3 scripts/verify_public_assets.py
```

`main` 반영 후 GitHub Actions가 검증하고 `latest` 릴리스의 고정 파일명을 교체합니다. `artifacts/manifest.json`은 공개 파일의 SHA-256과 크기를 기록합니다. `pdftotext`가 PATH에 없다면 `PDFTOTEXT_BIN`으로 절대경로를 지정합니다.

## 공개 범위

- 포함: 전화번호를 제외한 공개용 이력서, 통합·프로젝트별 포트폴리오, 공개 프로젝트 링크
- 제외: 원본 일감, 지원 공고, 내부 작업 기록, 비공개 검토 문서, 로컬 경로

문서와 개인 자료의 이용 범위는 [CONTENT-NOTICE.md](CONTENT-NOTICE.md)를 따릅니다.
