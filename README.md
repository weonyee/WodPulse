# 운동 기록 웹 애플리케이션 WodPulse 🏋️‍♂️💓

### Wod(Workout of the day) + Pulse 💓

![Image](https://github.com/user-attachments/assets/2f129b0c-3ae1-4804-af57-465a90c0fae2)
![Image](https://github.com/user-attachments/assets/3440bf73-b801-4a29-bcac-4f2a4d92d57b)

이 **Flask** 애플리케이션은 사용자가 운동 기록을 추가, 조회, 삭제할 수 있는 기능을 제공하는 웹 애플리케이션입니다. 주로 운동 기록(WOD)과 1RM(최고 기록)을 관리하는 시스템입니다. 이 애플리케이션은 **SQLite** 데이터베이스를 사용하여 데이터를 저장하고, `SQLAlchemy`와 `Flask-Migrate`를 사용하여 데이터베이스를 관리합니다.

## 📅 기간
- 25.3.27 - 25.3.28

## 주요 기능 🚀

### 1. 운동 기록 추가 및 조회
- 사용자가 날짜, 제목, WOD(운동), 별점(⭐), 메모를 입력하여 운동 기록을 추가할 수 있습니다.
- 저장된 기록은 `index.html` 페이지에서 확인할 수 있습니다.
- 기록은 DB에 저장되며, 홈 화면에서 최근 3개의 기록을 표시합니다.

### 2. 기록 상세 보기 및 삭제
- 각 운동 기록에 대해 상세 페이지를 제공하며, 기록을 삭제할 수도 있습니다.
- 기록 삭제는 `POST` 요청을 통해 처리됩니다.

### 3. 1RM(최고 기록) 입력 및 조회
- 사용자는 다양한 운동(예: back squat, deadlift 등)에 대한 최고 기록을 추가할 수 있습니다.
- 1RM 기록은 kg 단위로 자동 변환되어 저장됩니다.
- `pr_form.html`에서 1RM 기록을 입력할 수 있으며, 입력된 기록은 `view_pr.html`에서 확인할 수 있습니다.

## 파일 설명 📂

### Flask 애플리케이션 (Python 코드)
- `app.py`: `WodRecord`와 `Record` 모델을 정의하고, `SQLAlchemy`와 `Flask-Migrate`를 사용하여 데이터베이스와 상호작용합니다. 라우트 설정을 통해 운동 기록과 1RM 기록을 관리할 수 있습니다.

### HTML 템플릿
- `index.html`: 홈 화면에서 최근 운동 기록을 확인하고, 새로운 기록을 추가할 수 있습니다.
- `record_list.html`: 모든 운동 기록을 나열하고, 삭제할 수 있는 기능을 제공합니다.
- `record_detail.html`: 개별 운동 기록의 상세 정보를 보여줍니다.
- `pr_form.html`: 1RM 기록을 추가하는 폼을 제공합니다.
- `view_pr.html`: 입력된 1RM 기록을 테이블 형식으로 나열하여 보여줍니다.

## 실행 방법 ⚙️

1. 필요한 패키지를 설치합니다:
   ```bash
   pip install flask flask_sqlalchemy flask_migrate

   ```

2. `app.py` 파일을 실행하여 서버를 시작합니다.
   ```bash
   python app.py
   ```

3. **(배포예정)** 웹 브라우저에서 `http://127.0.0.1:5000/`로 접속하여 애플리케이션을 사용할 수 있습니다. 



## 기술 스택 🔧 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)


## 프로젝트 구조 📁

```bash
/project
│
├── app.py              # Flask 애플리케이션 코드
├── models.py           # 데이터베이스 모델
├── templates/          # HTML 템플릿 폴더
│   ├── index.html      # 홈 화면
│   ├── record_list.html# 운동 기록 리스트 페이지
│   ├── record_detail.html # 운동 기록 상세 페이지
│   ├── pr_form.html    # 1RM 기록 추가 폼
│   └── view_pr.html    # 1RM 기록 조회 페이지
├── static/             # 정적 파일 (CSS 등)
└── README.md           # 프로젝트 설명 (이 파일)
```

## 기여 🤝
이 프로젝트에 기여하고 싶다면, 먼저 이 프로젝트를 포크한 후 변경 사항을 제안해 주세요. 풀 리퀘스트(Pull Request)를 보내기 전에 로컬에서 테스트를 충분히 진행해 주세요.

## 라이센스 📜
이 프로젝트는 MIT 라이센스 하에 제공됩니다. 자세한 내용은 LICENSE 파일을 확인해 주세요.
