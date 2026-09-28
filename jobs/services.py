import requests
from bs4 import BeautifulSoup
from .models import Job

def fetch_and_save_jobs():
    url = "https://www.python.org/jobs/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0
    soup = BeautifulSoup(response.text, "html.parser")

    jobs_list = soup.find_all("ol", class_='list-recent-jobs')

    if not jobs_list:
        return 0

    job_items = jobs_list[0].find_all('li')

    saved_count = 0

    for item in job_items:
        title_element = item.find('h2', class_='listing-company')
        title = title_element.text.strip() if title_element else "Без назви"

        company_element = item.find("span", class_='listing-company-name')
        company = company_element.text.strip() if company_element else "Не вказано"

        location_element = item.find("span", class_='listing-location')
        location = location_element.text.strip() if location_element else "Не вказано"

        link_element = title_element.find('a') if title_element else None
        link = f'https://www.python.org{link_element["href"]}' if link_element and 'href' in link_element.attrs else ""

        if link:
            job, created = Job.objects.get_or_create(
                link=link,
                defaults={
                    'title': title,
                    'company': company,
                    'location': location,
                }
            )
            if created:
                saved_count += 1

    return saved_count