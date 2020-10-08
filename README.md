# 오목조목(서울 2반 5조)

![메인 페이지](https://user-images.githubusercontent.com/26289683/95407570-530c0200-0958-11eb-8c22-b2ca8177576c.JPG)


## 오목조목

#### 웹 기반 AI 오목대전 및 묘수풀이 플랫폼



## 서비스 목적

* 묘수풀이를 통해 흑돌은 게임을 이기기 위한 무적수(운월,포월,화월)를 학습하고 백돌 기준 무적수를 예측하고 끝까지 방어해 내는 것 

* 상, 중, 하로 나눠진 AI와 둬가며 AI는 어떤 최적의 수를 두는지 배우고 본인의 실력을 가늠하는 것



## 핵심 기능

#### 오목

- AI 대전: 선후공과 상, 중, 하로 나눠진 난이도를 정하여 AI와  첫수부터 1:1로 대국
- 묘수풀이 : 무적수 종류를 하나 선택해 스테이지별(5단계)로 주어진 판 상태에서 이어나가며 학습 및 풀이

#### 데이터 보관 및 관리

- 랭킹 점수와 승률 : 본인의 AI대전 및 묘수풀이 기록들을 시각화하여 제시
- JWT Token : 인증된 사용자만 데이터에 접근 가능하여 기밀성 보장



# 프로젝트 사용법

### Import

```bash
git clone https://lab.ssafy.com/s03-ai-sub3/s03p23a205.git
```

### Vue.js(Front-End)

```bash
cd s03p23a205/frontend
npm install
npm run serve
```

frontend root경로에서 node_modules가 이미 있다면 이 폴더를 지우고 없다면 

바로 npm install 후 npm run serve 로 프론트 서버 실행

#### Python(Back_End)

```json
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

로컬에서는 위와 같은 순서대로 명령어를 입력하여 db 생성 후 서버를 실행한다.

## MariaDB(DB)

- MariaDB, Docker 설치를 통해 DB 환경 구축

- Settings.py에 DATABASES를 다음과 같이 변경

  ```
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
          
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'ssafy',  #mysq
          'USER': 'root', #root
          'PASSWORD': '****', #비밀 번호를 입력한다.
          'HOST': '', #공백으로 냅두면 default localhost
          'PORT': '3305' #공백으로 냅두면 default 3306
      }
  }
  ```

- 위와 같은 작업을 진행 후에 모델을 형성하면 이후 DB 내용 변경은 HeidSQL을 이용해서 간편하게 수정할 수 있다.

# 서비스 설명

```bash
저희 서비스는 기본적으로 AI와 오목 대국을 진행하는 서비스입니다. 공격 순서로 선공과 후공중에 선택하고 난이도 상, 중, 하 중에 선택을 하여 AI와 대국을 펼칠 수 있습니다. 묘수풀이는 무적수를 학습하여 단계별로 AI를 이기면 clear하는 형식의 서비스 입니다.
```


```bash
저희 서비스는 로그인이 필수요소로 로그인페이지 이외의 페이지로 접근 시 로그인 페이지로 돌아가도록 설정해 주었습니다.

```

![로그인 페이지](https://user-images.githubusercontent.com/26289683/95407568-52736b80-0958-11eb-954e-03393feaae96.JPG)

```bash
메인페이지에서는 AI 대전, 묘수풀이, 각 서비스에 대한 설명, 유저 정보 및 실시간 순위가 표시되어 있습니다.

```

![메인 페이지](https://user-images.githubusercontent.com/26289683/95407570-530c0200-0958-11eb-8c22-b2ca8177576c.JPG)

```bash
AI 대전에서는 난이도 상 중 하 로 나뉘어져 있으며 대국이 끝나면 결과창과 함께 DB로 데이터가 전송돼 승률이 갱신됩니다.

```

![AI대전 클릭시 방설정](https://user-images.githubusercontent.com/26289683/95407565-51dad500-0958-11eb-9d0d-0bc033089d5e.JPG)

![AI대전 중](https://user-images.githubusercontent.com/26289683/95407564-51423e80-0958-11eb-87e2-d47e8772a7c0.JPG)

![AI대전 승리 시](https://user-images.githubusercontent.com/26289683/95407562-50111180-0958-11eb-8172-6f7f0a36797c.JPG)

```bash
묘수풀이에서는 무적수의 종류인 운월 포월 화월 3가지로 크게 나뉘어져 있으며 각각 5단계에 걸쳐 순차적으로 형태를 유도하며 익힐 수 있읍니다.

```

![묘수풀이 무적수고르기](https://user-images.githubusercontent.com/26289683/95407571-53a49880-0958-11eb-975f-6632ec708190.JPG)



![묘수풀이 운월 단계](https://user-images.githubusercontent.com/26289683/95407575-5606f280-0958-11eb-8a2b-90d9f85e6bca.JPG)

![묘수풀이 운월 5단계](https://user-images.githubusercontent.com/26289683/95407573-556e5c00-0958-11eb-9b59-29e9e6269e6d.JPG)

```bash
메인 페이지 상단의 물음표 아이콘으로는 저희 오목에 적용하고 있는 렌주룰에 대해 알 수 있습니다.

```

![오목룰 설명](https://user-images.githubusercontent.com/26289683/95407576-57381f80-0958-11eb-9d19-cf0856d9619d.JPG)




# 라이센스

[MIT License 2.0](https://lab.ssafy.com/s03-webmobile3-sub2/s03p12a211/blob/develop/LICENSE)



# 기타(개발 일정,  자랑하고 싶은 것, 변화된 이슈 등)

1. ### Django 환경설정

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



# 팀 소개

### 오목조목조

- 팀장 : 이준현(AI)

  Git : https://lab.ssafy.com/junhyun1993

- 팀원

  - 김남규 (Front-End)

    Git : https://lab.ssafy.com/kngking22

  - 서민규(Back-End)

    Git : https://lab.ssafy.com/alsrs3679

  - 이창로(AI)

    Git : https://lab.ssafy.com/pmiwha1004

  - 정진권 (Back-End)

    Git : https://lab.ssafy.com/jjk8060