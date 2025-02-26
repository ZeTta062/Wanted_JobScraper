# Wanted_JobScraper

## 목표
- 원티드 사이트에서 **자동으로 포지션 공고를 검색**
- 검색한 정보의 **제목, 회사명, 보상금, 링크를 웹페이지에서 표시**
- 버튼 클릭 시 **CSV 파일로 저장할 수 있는 기능 구현**

---

## 사용한 스택
- **Backend:** Python, Flask  
- **Web Scraping:** Playwright, BeautifulSoup  
- **Frontend:** PicoCSS (간단한 스타일링)

---

## 기능 설명
✅ **직업 검색 기능:** 사용자가 키워드를 입력하면 해당하는 원티드 공고를 크롤링하여 웹에 표시  
✅ **실시간 크롤링:** Playwright를 활용해 **최신 공고를 스크래핑**  
✅ **CSV 다운로드 기능:** 검색한 데이터를 클릭 한 번으로 CSV 파일로 저장  
✅ **웹 UI 제공:** Flask + PicoCSS로 가벼운 웹 인터페이스 구현 
# Wanted_JobScraper
