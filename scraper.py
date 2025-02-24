from playwright.sync_api import sync_playwright  # python -m pip install playwright / # playwright install
import time
from bs4 import BeautifulSoup  # pip install beautifulsoup4

def scrape_jobs(keyword):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 사용자가 입력한 검색어로 URL 생성
    url = f"https://www.wanted.co.kr/search?query={keyword}&tab=position"
    page.goto(url)  # 새로운 {link}의 페이지를 열음
    time.sleep(3)

    for x in range(5):  # 2초의 시간이 흐르고 end키를 눌러 페이지를 가장 아래로 내린다
        time.sleep(2)
        page.keyboard.down("End")

    content = page.content()  # beautifulsoup에 제공할 내용

    p.stop()

    # BeautifulSoup을 사용하여 페이지에서 원하는 정보 추출
    soup = BeautifulSoup(content, "html.parser")

    jobs = soup.find_all("div", class_="JobCard_container__REty8")

    jobs_db = []
    seen_links = set()  # 이미 처리한 링크를 기록할 집합

    for JobCard in jobs:
        link = f"https://www.wanted.co.kr{JobCard.find('a')['href']}"
        # 중복된 링크를 처리하지 않도록 확인
        if link in seen_links:
            continue  # 이미 처리한 링크는 건너뛰기
        seen_links.add(link)  # 새 링크를 처리한 링크 목록에 추가

        title = JobCard.find("strong", class_="JobCard_title__HBpZf").text

        company = JobCard.find("span", class_="JobCard_companyName__N1YrF").text
        
        reward = JobCard.find("span", class_="JobCard_reward__cNlG5")
        reward = reward.text if reward else "-"
        
        JobCard = {
            "title": title,
            "company": company,
            "reward": reward,
            "link": link
        }
        jobs_db.append(JobCard)

    return jobs_db  # 결과 직업 리스트 반환

