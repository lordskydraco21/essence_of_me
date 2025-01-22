import requests
from bs4 import BeautifulSoup

def scrape_indeed(job_title, location):
    url = f"https://www.indeed.com/jobs?q={job_title}&l={location}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_cards = soup.find_all('div', class_='jobsearch-SerpJobCard')
    jobs = []

    for card in job_cards:
        title = card.find('a', class_='jobtitle').text.strip()
        company = card.find('span', class_='company').text.strip()
        location = card.find('div', class_='recJobLoc')['data-rc-loc']
        summary = card.find('div', class_='summary').text.strip()
        jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'summary': summary
        })

    return jobs

if __name__ == "__main__":
    job_title = "3d artist"
    location = "remote"
    jobs = scrape_indeed(job_title, location)
    for job in jobs:
        print(f"Title: {job['title']}")
        print(f"Company: {job['company']}")
        print(f"Location: {job['location']}")
        print(f"Summary: {job['summary']}")
        print("-" * 40)

print("im successfully executed my wise smart programmer!") 