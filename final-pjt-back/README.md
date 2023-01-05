# SSAFBOX-Backend

## Getting started

Docker를 이용하여 SSAFBOX-Backend를 실행할 수 있습니다.

### Prerequisites

- Docker
- Docker-compose

### Installation

1. SSAFBOX-Backend를 clone합니다.
2. SSAFBOX-Backend 폴더로 이동합니다.
3. docker-compose build --no-cache 명령어를 실행합니다.
4. docker-compose up -d 명령어를 실행합니다.
5. docker-compose exec web python manage.py makemigraionts 명령어를 실행합니다.
6. docker-compose exec web python manage.py migrate 명령어를 실행합니다.
7. docker-compose run --rm web sh -c "python manage.py loaddata movies/fixtures/genres.json"
8. docker-compose run --rm web sh -c "python manage.py loaddata movies/fixtures/new_movie_fixture.json"

### 프로젝트 설명

해당 프로젝트는 Django,Postgresql,Gunicorn을 이용하여 구현되었습니다.

