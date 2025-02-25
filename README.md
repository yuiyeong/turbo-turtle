# 개요

- 이 프로젝트는 다양한 토이 프로젝트를 포트폴리오 형태로 선보이는 웹 갤러리입니다.
- Django의 클린 아키텍처, DDD 패턴을 적용하여 각 서비스가 독립적으로 작동할 수 있도록 설계되었습니다.
- 메인 포트폴리오 앱은 Django 템플릿을 활용한 웹 사이트로 구현되며, 각 토이 프로젝트는 다양한 기술 스택(Django, Next.js, 모바일 등)으로 개발될 수 있습니다.

## 주요 특징

- **클린 아키텍처 적용**: Django의 강력한 기능을 활용하면서도 비즈니스 로직을 분리
- **DDD 원칙 준수**: 도메인 모델 중심의 설계로 복잡한 비즈니스 요구사항 처리
- **실용적인 접근**: 이론적 완벽함보다 실질적인 이점을 추구하는 아키텍처

# 시스템 아키텍처

프로젝트는 클린 아키텍처 원칙에 따라 다음과 같은 계층 구조를 가집니다.

```
.
├── config/                   # 프로젝트 설정
├── apps/                     # 앱 컨테이너
│   ├── core/                 # 공통 기능 (인증, 유틸리티 등)
│   ├── portfolio/            # 포트폴리오 관리 앱
│   ├── todo/                 # Todo 서비스 앱
│   ├── notion_clone/         # Notion 클론 앱
│   ├── trello_clone/         # Trello 클론 앱
│   └── ...                   # 기타 독립적인 앱들
└── tests/                    # 테스트 디렉토리
    ├── unit/
    ├── integration/
    └── e2e/
```

각 앱은 다음과 같은 내부 구조를 가집니다.

```
apps/some_app/
├── admin/           # 패키지화된 admin
├── models/          # 패키지화된 models
├── serializers/     # 패키지화된 serializers (DRF 사용 시)
├── templates/       # 템플릿 (Django Template 사용 시)
├── views/           # 패키지화된 views
├── domain/          # 도메인 로직
├── application/     # 유스케이스/서비스
└── infrastructure/  # 인프라 구현체
```

## 주요 계층 설명

1. **도메인 계층 (Domain Layer)**
    - 핵심 비즈니스 로직 및 규칙
    - 도메인 모델, 엔티티, 값 객체 정의
    - 외부 서비스에 대한 인터페이스 정의
2. **애플리케이션 계층 (Application Layer)**
    - 유스케이스 구현 및 도메인 서비스 조율
    - 데이터 전송 객체(DTO) 정의
    - 트랜잭션 관리
3. **인프라 계층 (Infrastructure Layer)**
    - 외부 시스템 통합 구현체
    - 데이터 접근 계층 구현
    - 프레임워크 종속적인 코드
4. **인터페이스 계층 (Interface Layer)**
    - Django 뷰, 템플릿, 폼
    - REST API 엔드포인트
    - 사용자 인터페이스

# 설치 및 설정

## 사전 요구사항

- Python 3.11+
- Docker 및 Docker Compose
- Poetry

## 🛠️ 기술 스택

### 개발 환경

- **Pyenv**: Python 버전 관리
- **Docker & Docker Compose**: 컨테이너화 및 환경 관리
- **Poetry**: 패키지 관리
- **Ruff**: 코드 품질 관리
- **Pre-commit**: 커밋 전 코드 검사

### 백엔드

- **Django & Django REST Framework**: 웹 프레임워크 및 RESTful API 구현
- **PostgreSQL**: 주요 데이터베이스
- **Redis**: 캐싱 및 메시지 브로커
- **Celery**: 비동기 작업 처리

### 프론트엔드

- **Django Templates**: 서버 사이드 렌더링 (일부 앱)
- **Next.js (React)**: 클라이언트 사이드 렌더링 (일부 앱)
