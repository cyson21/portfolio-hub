# 손찬양 | Backend Engineering Portfolio

Java/Spring을 중심으로 동시성, 부분 실패 복구, 이벤트 전달과 데이터 흐름을 다룬 프로젝트 자료를 모았습니다.

아래 프로젝트 설명과 기술 스택은 개인 프로젝트에서 설계·구현·검증한 범위이며, 실무 운영 경험과 구분합니다.

실무에서는 백엔드 2명, 프론트엔드 1명의 3인 개발팀에서 20개 이상의 기업 고객 서비스를 개발·운영했습니다.

## 바로 보기

| 이력서 PDF | 웹 포트폴리오 | 통합 포트폴리오 HTML |
|---|---|---|
| [resume.pdf](https://github.com/cyson21/portfolio-hub/releases/download/latest/resume.pdf) | [cyson21.github.io](https://cyson21.github.io/) | [cyson21.github.io/portfolio](https://cyson21.github.io/portfolio/) |

## 직무 주제별 프로젝트

| 주제 | 프로젝트 | 확인할 구현 |
|---|---|---|
| 분산 상태와 복구 | [StockRush](https://github.com/cyson21/stockrush) · [웹 사례](https://cyson21.github.io/projects/stockrush/) | Saga, Transactional Outbox, 소비자 멱등성, Kafka 중단 복구 |
| 동시성과 데이터 정합성 | [Member Event Consistency](https://github.com/cyson21/member-event-consistency) · [웹 사례](https://cyson21.github.io/projects/member-event-consistency/) | PostgreSQL 제약·행 잠금, Redis 잠금, RabbitMQ 단일 소비자 기반 캠페인 발급 경합 제어 |
| 공통 API 인프라 | [AI Gateway](https://github.com/cyson21/ai-gateway) · [웹 사례](https://cyson21.github.io/projects/ai-gateway/) | 조직 인증, 사용량 제한, 캐시, 모델 선택과 장애 복구 |
| 변경 데이터와 재처리 | [CDC Data Platform (프로토타입)](https://github.com/cyson21/cdc-data-platform) · [웹 사례](https://cyson21.github.io/projects/cdc-data-platform/) | 독립된 CDC 구성요소에서 Debezium CDC, 중복 처리 방지, 실패 추적과 재처리를 검증 |
| 권한 기반 검색 | [Enterprise Policy RAG](https://github.com/cyson21/enterprise-policy-rag) · [웹 사례](https://cyson21.github.io/projects/enterprise-policy-rag/) | 검색 전 권한 필터, 근거 없는 답변 거절과 출처 제공 |

각 프로젝트에서 어떤 설계로 실패 조건을 막았고 어디까지 구현했는지는 저장소와 웹 사례에서 확인할 수 있습니다.

문서와 개인 자료의 이용 범위는 [CONTENT-NOTICE.md](CONTENT-NOTICE.md)를 따릅니다.

자료 생성·검증·배포 절차는 [유지보수 문서](docs/maintenance.md)에 분리했습니다.
