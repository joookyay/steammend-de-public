# Steammend Project

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
### 회원가입 기능
- 회원가입(steamgame id 검색 가능)
<img src="https://user-images.githubusercontent.com/76192858/212928456-c62b65da-799f-446f-9125-3b06cb712789.png" width="800" height="400"/>
 
- 로그인/로그아웃
<img src="https://user-images.githubusercontent.com/76192858/212929068-46d2540d-8bd2-42a9-8376-a9fdfec410f0.png" width="800" height="400"/>
 
### 검색 기능
- 인기, 무료, 세일, 최신 게임 조회(게임 누르면 스팀공식홈페이지의 해당 게임으로 연동)
<img src="https://user-images.githubusercontent.com/76192858/212885379-6a99ce92-b245-42ca-b3bd-007b1eb16200.png" width="800" height="400"/>

- 가격, 연령, 장르별 커스터마이징 가능(게임 누르면 스팀공식홈페이지의 해당 게임으로 연동)
<img src="https://user-images.githubusercontent.com/76192858/212886948-3b8367d2-a63f-43a8-bda8-ea33240a9aba.png" width="800" height="400"/>
  
### 커뮤니티 기능
- 게시글 작성 및 수정,삭제
<img src="https://user-images.githubusercontent.com/76192858/212929372-7175ae70-b099-4ac1-a936-72d6f175eb65.png" width="800" height="400"/> 
<img src="https://user-images.githubusercontent.com/76192858/212926986-643bc129-45ae-4dc3-a18b-c3753524a071.png" width="800" height="400"/>  

- 댓글 작성 및 수정, 삭제
<img src="https://user-images.githubusercontent.com/76192858/212931965-f93ac5f7-bb36-434f-abfe-87961b8c2617.png" width="800" height="400"/>  

### 게임 추천 서비스
- 메인페이지
<img src="https://user-images.githubusercontent.com/76192858/212930706-efe531a7-fff6-4a2f-a7c9-431ff3e0585d.png" width="800" height="400"/>  

- 대시보드 페이지
<img src="https://user-images.githubusercontent.com/76192858/212929933-30378592-ea8a-4958-aa29-94e34c674dd7.png" width="800" height="400"/>  

### 대시보드 시각화 서비스
<img src="https://user-images.githubusercontent.com/76192858/212931051-6840ef01-a2d3-4da6-9598-7d732db6147e.png" width="800" height="400"/> 
<img src="https://user-images.githubusercontent.com/76192858/212931320-f61f903a-ec81-475a-82b5-7232a902cccf.png" width="800" height="400"/> 



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
