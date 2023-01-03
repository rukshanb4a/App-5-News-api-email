import requests
from send_email import send_email

api_key = '4a28d0323aa04807a81acdbee0732d44'
url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=4a28d0323aa04807a81acdbee0732d44"

request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = " "
# Access the article titles and description
for article in content["articles"]:
    if article["ttile"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode('utf-8')

# Send email
send_email(body)

print("Email has been sent")

