# 손찬양 | Backend Engineering Portfolio

Java/Spring을 중심으로 동시성, 부분 실패 복구, 이벤트 전달과 데이터 흐름 문제를 해결한 프로젝트 모음입니다.

## 바로 보기

| 이력서 PDF | 웹 포트폴리오 | 통합 포트폴리오 PDF |
|---|---|---|
| [resume.pdf](https://github.com/cyson21/portfolio-hub/releases/download/latest/resume.pdf) | [cyson21.github.io](https://cyson21.github.io/) | [portfolio-complete.pdf](https://github.com/cyson21/portfolio-hub/releases/download/latest/portfolio-complete.pdf) |

## 직무 주제별 프로젝트

| 주제 | 프로젝트 | 확인할 구현 |
|---|---|---|
| 분산 상태와 복구 | [StockRush](https://github.com/cyson21/stockrush) · [웹 사례](https://cyson21.github.io/projects/stockrush/) | Saga, Transactional Outbox, 소비자 멱등성, Kafka 중단 복구 |
| 동시성과 데이터 정합성 | [Member Event Consistency](https://github.com/cyson21/member-event-consistency) · [웹 사례](https://cyson21.github.io/projects/member-event-consistency/) | PostgreSQL 제약·행 잠금, Redis 잠금, RabbitMQ 순차 처리 |
| 공통 API 인프라 | [AI Gateway](https://github.com/cyson21/ai-gateway) · [웹 사례](https://cyson21.github.io/projects/ai-gateway/) | 조직 인증, 사용량 제한, 캐시, 모델 선택과 장애 복구 |
| 변경 데이터와 재처리 | [CDC Data Platform](https://github.com/cyson21/cdc-data-platform) · [웹 사례](https://cyson21.github.io/projects/cdc-data-platform/) | Debezium CDC, 중복 처리 방지, 실패 추적과 재처리 |
| 권한 기반 검색 | [Enterprise Policy RAG](https://github.com/cyson21/enterprise-policy-rag) · [웹 사례](https://cyson21.github.io/projects/enterprise-policy-rag/) | 검색 전 권한 필터, 근거 없는 답변 거절과 출처 제공 |
| 이벤트 기반 개인화 | [Fashion Personalization Platform](https://github.com/cyson21/fashion-personalization-platform) · [웹 사례](https://cyson21.github.io/projects/fashion-personalization-platform/) | 이벤트 중복 방지, 추천 근거와 배치 스냅샷 |

각 프로젝트에서 어떤 설계로 실패 조건을 막았고 어디까지 구현했는지는 저장소와 웹 사례에서 확인할 수 있습니다.

문서와 개인 자료의 이용 범위는 [CONTENT-NOTICE.md](CONTENT-NOTICE.md)를 따릅니다.

자료 생성·검증·배포 절차는 [유지보수 문서](docs/maintenance.md)에 분리했습니다.
