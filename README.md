# 손찬양 | Backend Engineering Portfolio

Java·Spring 기반 API 개발·운영과 운영 안정화 경험을 소개합니다. 회사 실무 경력과 개인 프로젝트의 공개 구현을 구분해 안내합니다.

아래 프로젝트 설명과 기술 스택은 개인 프로젝트에서 설계·구현·검증한 범위이며, 실무 운영 경험과 구분합니다.

실무에서는 4인 실무 개발팀에서 20개 이상의 기업 고객 서비스를 개발·운영했습니다.

## 바로 보기

| 이력서 PDF · 2쪽 | 경력기술서 PDF · 3쪽 | 포트폴리오 HTML |
|---|---|---|
| [업무·핵심 기여 요약](https://cyson21.github.io/downloads/resume.pdf) | [서비스 맥락·역할·주요 기여](https://cyson21.github.io/downloads/career-description.pdf) | [실무 사례와 개인 프로젝트 상세](https://cyson21.github.io/portfolio/index.html) |

최신 제출 파일은 위 웹사이트 경로를 사용합니다. 이 저장소의 릴리스 첨부는 과거 배포 자료이며 최신 웹 파일과 동일하다고 전제하지 않습니다.

## 개인 프로젝트 · 주제별 공개 구현

| 주제 | 프로젝트 | 확인할 구현 |
|---|---|---|
| 분산 상태와 복구 | [StockRush](https://github.com/cyson21/stockrush) · [웹 사례](https://cyson21.github.io/projects/stockrush/) | Saga, Transactional Outbox, 소비자 멱등성, Kafka 중단 복구 |
| 동시성과 데이터 정합성 | [Member Event Consistency](https://github.com/cyson21/member-event-consistency) · [웹 사례](https://cyson21.github.io/projects/member-event-consistency/) | PostgreSQL 제약·행 잠금, Redis 잠금, RabbitMQ 캠페인 경합 제어(단일 Spring 인스턴스의 listener concurrency=1 범위; 전역 ordering·전역 single-consumer 보장 아님) |
| 공통 API 인프라 | [AI Gateway](https://github.com/cyson21/ai-gateway) · [웹 사례](https://cyson21.github.io/projects/ai-gateway/) | 조직 인증, 사용량 제한, 캐시, 모델 선택과 장애 복구 |
| 변경 데이터와 재처리 | [CDC Data Platform (프로토타입)](https://github.com/cyson21/cdc-data-platform) · [웹 사례](https://cyson21.github.io/projects/cdc-data-platform/) | 독립된 CDC 구성요소에서 Debezium CDC, 중복 처리 방지, 실패 추적과 재처리를 검증 |
| 권한 기반 검색 | [Enterprise Policy RAG](https://github.com/cyson21/enterprise-policy-rag) · [웹 사례](https://cyson21.github.io/projects/enterprise-policy-rag/) | 검색 전 권한 필터, 근거 없는 답변 거절과 출처 제공 |

각 프로젝트에서 어떤 설계로 실패 조건을 막았고 어디까지 구현했는지는 저장소와 웹 사례에서 확인할 수 있습니다.

문서와 개인 자료의 이용 범위는 [CONTENT-NOTICE.md](CONTENT-NOTICE.md)를 따릅니다.

자료 생성·검증·배포 절차는 [유지보수 문서](docs/maintenance.md)에 분리했습니다.

## 저장소 간 자료 흐름

현재 제출 문서의 편집·생성·배포 기준은 [cyson21.github.io](https://github.com/cyson21/cyson21.github.io)의 사이트 소스와 공개 다운로드입니다. [GitHub 프로필](https://github.com/cyson21/cyson21)과 이 README는 해당 사이트와 각 구현 저장소를 안내합니다.

이 저장소에는 별도의 과거 자료 동기화 경로가 남아 있습니다. `scripts/sync_from_workspace.py --source <작업공간>`은 허용된 생성 파일을 `artifacts/`로 복사하고 manifest를 갱신합니다. 이 경로를 사용할 때는 `docs/maintenance.md`의 공개 범위와 검사 절차를 먼저 따릅니다. 최신 사이트 소스가 이 스크립트로 자동 변환되는 것은 아닙니다.

`publish-latest.yml`은 main의 `artifacts/**`, 자산 검사 스크립트 또는 해당 workflow가 바뀔 때 검증 후 `latest` 릴리스를 갱신합니다. README만 바꿔서는 PDF가 교체되지 않습니다. 릴리스 자산을 최신 제출 파일로 안내하려면 현재 사이트 다운로드와 내용을 먼저 대조해야 합니다.
