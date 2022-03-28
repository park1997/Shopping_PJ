# Shopping_PJ
 
# 🛫 결과

<img width="1485" alt="스크린샷 2022-03-28 오후 10 48 53" src="https://user-images.githubusercontent.com/73048180/160412258-358d21e1-e219-4077-a900-a6a25c2e7285.png">

<img width="1484" alt="스크린샷 2022-03-28 오후 10 49 05" src="https://user-images.githubusercontent.com/73048180/160412315-edf3695b-28d4-4c7c-af7a-d0955691a674.png">

- 코루틴, 멀티 스레딩, 멀티 프로세싱을 이용한 **동시성 / 병렬성 프로그래밍**을 사용
- **NAVER api**(Postman 사용) 를 활용하여 **MongoDB**에 적재 및 분석
- 모던 WEB Framework인 **Fast api**를 이용한 수집한 데이터를 시각화한 웹 개발
- **AWS 클라우드**에 웹 **배포**

---

# 🔍 기술 스택

- **Fast api(REST API를 만들기위한 Python Web Framework)**
- **async(비동기) IO**
- **Mongo DB**
- **AWS lightsail (Virtual Private Server)**
- **Cloud Computing**
- **Crawling**

---

# ✍️  서론

- 프로젝트 배경
    - 인터넷에서 물건을 살 때 최저비용 최고의 물품을 고르는데 시간과 비용이 많이 든다.
    - 많은 쇼핑몰들 사이에서 최저 가격을 찾을 수 있는 방법이 있을지 고민 하였다.
- 문제 정의
    - 여러 쇼핑몰의 최저가격의 물품을 싼 가격부터 조회 하기 위한 서비스가 필요하다.
- 프로젝트 목표
    - 가격에 민감한 구매자를 위해 물품명 검색 만으로 여러 쇼핑몰의 매물 들을 저렴한 가격 순으로 제시하는 웹 서비스를 구현하고 배포한다.

---

# 👨🏻‍💻담당 업무

- 동시성 프로그래밍을 사용하여 웹 크롤링
    - 속도 향상을 위해 비동기 프로그래밍 사용
    - 네트워크 I/O 개선
- 수집한 데이터 MongoDB에 저장 및 연동
    - MongoDB CRUD
- Fast api와 연결하여 Back-end 개발을 통한 시스템 로직 구현
    - 민감한 정보(API_ID etc..)를 숨기기위해 config구현
- 간단한 Front-end 개발로 수집된 데이터 기반 웹 시각화
    - HTML, CSS
    - Jinja2Templates
- AWS 클라우드 컴퓨팅으로 프로젝트 배포
    - AWS lightsail
    - Linux/Unix
    - Ubuntu

---

# 💡 느낀 점

- 비동기 / 동시성 프로그래밍 작성 역량 강화로 정보 전달의 시간 / 비용적 절감 기대
- Database 연동 및 활용 역량 강화
- Web Framework의 사용으로 전반적인 웹 설계 능력 강화
- AWS를 통한 서버배포로 리눅스 활용 능력 강화

---

# 🛠 개발 세부내용

## 1. Fast api

- Jinja2 Templates 활용

---

## 2. Naver api

- NAVER API 신청
    
<img width="1123" alt="스크린샷 2022-03-28 오후 10 49 24" src="https://user-images.githubusercontent.com/73048180/160412371-97ca6e54-ffe8-40fd-9823-e944634cc1b2.png">

- Postman을 이용한 API 동작 확인 및 데이터 구조 확인
    

<img width="960" alt="스크린샷 2022-03-28 오후 10 49 46" src="https://user-images.githubusercontent.com/73048180/160412433-335da86a-28e8-4bde-b913-1a64563547eb.png">


---

## 3. MongoDB

- MongoDB 생성
    <img width="946" alt="스크린샷 2022-03-28 오후 10 50 00" src="https://user-images.githubusercontent.com/73048180/160412482-228ca3b4-b939-45fa-8c09-4c8a657a1f1a.png">

    
- Fast api와 DB연동

<img width="956" alt="스크린샷 2022-03-28 오후 10 51 28" src="https://user-images.githubusercontent.com/73048180/160412807-fbd06b32-3d08-45ff-a7b0-0d9ef32d2815.png">

---

## 4. AWS lightsail

- AWS lightsail 인스턴스 생성(Linux/Unix , Ubuntu)

<img width="975" alt="스크린샷 2022-03-28 오후 10 50 26" src="https://user-images.githubusercontent.com/73048180/160412577-f8bcc4c8-e6f3-4699-8e92-9f2bc4a64b41.png">



    
- AWS 클라우드 서버를 이용한 웹 서비스 배포

    <img width="991" alt="스크린샷 2022-03-28 오후 10 50 36" src="https://user-images.githubusercontent.com/73048180/160412633-b52d1103-cbd1-4183-8691-cf52f0647f99.png">
