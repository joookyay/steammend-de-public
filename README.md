# Final Project <steammend>

## 🎮프로젝트 소개
유저들의 게임 플레이 내역을 기반으로 유사한 게임 추천 및 대시보드 제공, 커뮤니티 서비스<br>
👉 [steammed 더 알아보기](https://iamcoz.notion.site/Steammend-6596f5bc20df426ba522c44d26ffe3b0)

## 📅 개발기간
2022.10.19 - 2022.11.10

## 🤖 알고리즘 소개
스팀게임 API를 사용하여 실시간으로 유저의 게임 플레이 데이터 정보 수집<br>
NLP기법 중 하나인 TF-IDF 방법을 사용하여 Elastic Cloud에 저장된 인기게임들과 코사인 유사도를 측정<br>
게임 플레이 시간이 가장 긴 5개의 게임과 유사도가 가장 높은 Top5게임 추천
  
## 📌주요 기능 소개
#### 회원가입 및 로그인 
### 인기, 무료, 세일, 최신 게임 조회/가격, 연령, 장르별 커스터마이징하여 조회 가능
<img src="https://user-images.githubusercontent.com/76192858/212885379-6a99ce92-b245-42ca-b3bd-007b1eb16200.png"/>
<img src="https://user-images.githubusercontent.com/76192858/212886948-3b8367d2-a63f-43a8-bda8-ea33240a9aba.png"/>
  
#### 커뮤니티 게시글 작성 및 수정,삭제/댓글 작성 및 수정, 삭제
  
  

## ⚙️ python 가상환경 세팅

#### 가상환경 설치 및 실행 
```
C:\project>python -m venv [가상환경 이름]
C:\project>cd [가상환경 이름]
C:\project>Script\activate.bat
```
#### requirments.txt를 가상환경 프로젝트 폴더 안에 저장 후
```
pip install -r requirements.txt
```
