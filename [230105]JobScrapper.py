from requests import get
from extractors.wwr import extractor_jobs
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extract_indeed_jobs(keyword):
    # Page 실행 후 Source 가져오기
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)

    browser.get(f"https://kr.indeed.com/jobs?q={keyword}")

    try:
        results = []

        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all('li', recursive=False)

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")

            if zone == None:
            #     print("job li")
            # else:
            #     print("mosaic li")
                # print(job.select('h2 a'))
                anchor = job.select("h2 a")[0]
                # print(anchor)
                # print(anchor['aria-label'])
                # print("/"*10)
                title = anchor['aria-label']
                link = anchor['href']
                # print("/"*10, "\n", "/"*10)
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                    'link': f"https://kr.indeed.com{link}",
                    'company': company.string,
                    'location': location.string,
                    'position': title
                }

                results.append(job_data)

        for result in results:
            print(result, "\n////////\n")

        return results

    except:
        print("Cant request page")

extract_indeed_jobs('python')