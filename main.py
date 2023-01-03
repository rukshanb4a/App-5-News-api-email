import requests

api_key = '4a28d0323aa04807a81acdbee0732d44'
url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=4a28d0323aa04807a81acdbee0732d44"

request = requests.get(url)

# Get a dictionary with data
content = request.json()

#Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])