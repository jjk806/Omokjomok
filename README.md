### Django 환경설정

* 가상환경 설정

  * 전에 만들어뒀던 anaconda의 `AI`가상환경으로 프로젝트 시작
  * ⭐같은 패키지를 설치하더라도, pip 로 설치하는 것과 conda 를 통해 설치하는 것은 다릅니다.⭐
    - 프로젝트 전체 팀원이 모두 vitrualenv 나 conda 를 통한 설치 중 한 가지만을 사용하는 편이 정확합니다.
  - pip 를 사용한다면 requirements.txt 를, conda 를 사용한다면 yaml 파일을 만들어 다른 팀원들과 같은 환경을 공유할 수 있도록 합니다.
  * pip로 설치 했을 경우
    * requiremenets.txt
      * 생성 : `pip freeze > requirements.txt`
      * 사용 : `pip install -r requirements.txt`
  * conda로 설치 했을 경우
    * environment.yaml
      * 생성 : `conda env export > environment.yaml`
      * 사용 : `conda env create --file environment.yaml`
      * 사용시 기존 가상환경 제거 후 새로 설치하기
  
* 프로젝트 생성

  ```bash
  $django-admin startproject omok_jomok
  ```

* settings.py 설정

  ```python
  LANGUAGE_CODE = 'ko-kr'
  TIME_ZONE = 'Asia/Seoul'
  ```

* app 생성

  ```bash
  $python manage.py startapp account
  ```

* db 설정
  mariadb이용
  설치 참고 사이트 : https://offbyone.tistory.com/199
  연동 참고 사이트 : https://ministar.tistory.com/4

  ```bash
  $pip install mysqlclient
  ``` 
  
  MYSQL이용
  ```bash
  $pip install PyMySQL
  ```

* django-rest 인증
  django-restframework 설치
  django-rest-auth 설치
  allauth 설치
  jwt 설치
  설치 참고 사이트 : https://django-rest-auth.readthedocs.io/en/latest/installation.html#jwt-support-optional

  ```bash
  $pip install djangorestframework
  $pip install django-rest-auth
  $pip install django-allauth
  $pip install djangorestframework djangorestframework-jwt
  ```
* cors 작업
  참고사이트 : https://github.com/adamchainz/django-cors-headers

  ```bash
  $python -m pip install django-cors-headers
  ```
* Email 인증 작업
  참고사이트 : https://velog.io/@snowman39/Django-%EC%97%90%EC%84%9C-%EC%9D%B4%EB%A9%94%EC%9D%BC-%EB%B3%B4%EB%82%B4%EA%B8%B0-SMT-Gmail-API