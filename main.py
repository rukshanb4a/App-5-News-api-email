import requests
from send_email import send_email

topic = "Tesla"
from_date = "2022-12-03"

api_key = '4a28d0323aa04807a81acdbee0732d44'
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&from={from_date}&" \
      "sortBy=publishedAt&" \
      "apiKey=4a28d0323aa04807a81acdbee0732d44&" \
      "language=En"

request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = " "
# Access the article titles and description
for article in content["articles"][0:10]:
    if article["ttile"] is not None:
        body = "Subject: today's news" \
               + "\n" + body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode('utf-8')

# Send email
send_email(body)

print("Email has been sent")

