# postly

## 개요

이번 프로젝트는 간단하게 FastAPI를 사용해보고 Django와 다른 점을 알아나가기 위해 진행되었습니다.

## 프로젝트 진행 과정

### 1일차

- FastAPI를 사용해 마이크로서비스(post_service)를 구현하기 위한 기초 작업 진행
  - FastAPI의 폴더 구조를 익히고 각 파일의 주요 역할에 대해 학습
    - main.py: FastAPI 애플리케이션을 초기화하고 라우트를 등록
    - models.py: 데이터 구조를 정의하며 FastAPI의 Pydantic 모델을 사용
    - routes.py: 서비스의 API 엔드포인트를 정의
    - crud.py: 데이터 처리 로직을 캡슐화하여 유지보수성과 재사용성 향상에 기여, DB를 사용하는 경우 SQLAlchemy 등을 사용
