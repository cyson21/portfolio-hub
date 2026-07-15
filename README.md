# 손찬양 포트폴리오 허브

Java/Spring 백엔드 개발자 손찬양의 최신 이력서, 통합 포트폴리오와 프로젝트별 제출 자료를 한곳에서 제공합니다.

## 바로 보기

| 자료 | 최신 고정 주소 |
|---|---|
| 웹 포트폴리오 | [cyson21.github.io](https://cyson21.github.io/) |
| 이력서 PDF | [resume.pdf](https://github.com/cyson21/portfolio-hub/releases/download/latest/resume.pdf) |
| 이력서 HTML | [resume.html](https://github.com/cyson21/portfolio-hub/releases/download/latest/resume.html) |
| ATS 이력서 PDF | [resume-ats.pdf](https://github.com/cyson21/portfolio-hub/releases/download/latest/resume-ats.pdf) |
| 통합 포트폴리오 PDF | [portfolio-complete.pdf](https://github.com/cyson21/portfolio-hub/releases/download/latest/portfolio-complete.pdf) |
| 통합 포트폴리오 HTML | [portfolio-complete.html](https://github.com/cyson21/portfolio-hub/releases/download/latest/portfolio-complete.html) |
| 프로젝트 인덱스 PDF | [portfolio-index.pdf](https://github.com/cyson21/portfolio-hub/releases/download/latest/portfolio-index.pdf) |

`latest` 릴리스의 자산 이름은 바꾸지 않습니다. 새로운 내용이 반영되어도 위 주소는 그대로 유지됩니다.

## 프로젝트

| 프로젝트 | 핵심 주제 | 저장소 | 상세 웹 페이지 |
|---|---|---|---|
| StockRush | Saga, Transactional Outbox, Kafka 복구 | [GitHub](https://github.com/cyson21/stockrush) | [상세](https://cyson21.github.io/projects/stockrush/) |
| Enterprise Policy RAG | 권한 검색, 인용, 평가 | [GitHub](https://github.com/cyson21/enterprise-policy-rag) | [상세](https://cyson21.github.io/projects/enterprise-policy-rag/) |
| Member Event Consistency | PostgreSQL, Redis, RabbitMQ 동시성 | [GitHub](https://github.com/cyson21/member-event-consistency) | [상세](https://cyson21.github.io/projects/member-event-consistency/) |
| AI Gateway | 라우팅, 캐시, 폴백, 사용량 제한 | [GitHub](https://github.com/cyson21/ai-gateway) | [상세](https://cyson21.github.io/projects/ai-gateway/) |
| CDC Data Platform | Debezium, Kafka, lineage, replay | [GitHub](https://github.com/cyson21/cdc-data-platform) | [상세](https://cyson21.github.io/projects/cdc-data-platform/) |
| Fashion Personalization Platform | 행동 이벤트, 추천 점수, 배치 스냅샷 | [GitHub](https://github.com/cyson21/fashion-personalization-platform) | [상세](https://cyson21.github.io/projects/fashion-personalization-platform/) |

## 최신 상태 유지

공개 파일은 로컬 작업 공간의 생성 산출물에서 허용 목록만 동기화합니다.

```bash
python3 scripts/sync_from_workspace.py --source /path/to/side-projects
python3 scripts/verify_public_assets.py
```

로컬 PATH에 `pdftotext`가 없으면 `PDFTOTEXT_BIN=/path/to/pdftotext`를 검증 명령 앞에 지정합니다.

`main`에 변경이 반영되면 GitHub Actions가 검증을 다시 실행하고 `latest` 릴리스의 동일한 파일 이름을 교체합니다. `artifacts/manifest.json`은 공개 파일의 SHA-256과 크기를 기록합니다.

## 공개 범위

- 포함: 전화번호를 제외한 공개용 이력서, 통합·프로젝트별 포트폴리오, 공개 프로젝트 링크
- 제외: 원본 일감, 지원 공고, 내부 작업 기록, 비공개 검토 문서, 로컬 경로

문서와 개인 자료의 이용 범위는 [CONTENT-NOTICE.md](CONTENT-NOTICE.md)를 따릅니다.
