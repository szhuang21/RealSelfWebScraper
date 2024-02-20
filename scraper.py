from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0'}
url = "https://www.realself.com/questions/facial-fat-transfer"
response = requests.get(url, headers=headers)

print("response: ", response)
soup = BeautifulSoup(response.text, "html.parser")
response.raise_for_status()

span_tag = soup.find("span")
print("span_tag: ", span_tag)