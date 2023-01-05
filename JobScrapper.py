from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extractor_jobs

# bot 감지로 인해 막힘

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("Cant request page")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    jobs = job_list.find_all('li', recursive=False)

    for job in jobs:
        print(job)
        print("/"*10)