import requests
from bs4 import BeautifulSoup

def fetch_jobs():
    url = "https://www.python.org/jobs/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Помилка завантаження сторінки. Статус код: {response.status_code}")
        return []
    soup = BeautifulSoup(response.text, "html.parser")

    jobs_list = soup.find_all("ol", class_='list-recent-jobs')

    if not jobs_list:
        print("Вакансій не знайдено.")
        return []

    job_items = jobs_list[0].find_all('li')

    parsed_jobs = []

    for item in job_items:
        title_element = item.find('h2', class_='listing-company')
        title = title_element.text.strip() if title_element else "Без назви"

        company_element = item.find("span", class_='listing-company-name')
        company = company_element.text.strip() if company_element else "Не вказано"

        location_element = item.find("span", class_='listing-location')
        location = location_element.text.strip() if location_element else "Не вказано"

        link_element = title_element.find('a') if title_element else None
        link = f'https://www.python.org{link_element["href"]}' if link_element and 'href' in link_element.attrs else ""

        parsed_jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'link': link,
        })
    return parsed_jobs

if __name__ == "__main__":
    jobs = fetch_jobs()
    print(f"Знайдено вакансій: {len(jobs)}\n")
    for job in jobs[:3]:  # Виведемо перші 3 для перевірки
        print(f"Посада:  {job['title']}")
        print(f"Компанія: {job['company']}")
        print(f"Локація: {job['location']}")
        print(f"Сайт:    {job['link']}")
        print("-" * 40)