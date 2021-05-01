# Import necessary modules
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from flask import Flask, render_template

# Create Flask Object
app = Flask(__name__)

# Constants
STOCK_ENDPOINT = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

# Parameters for Stock API
parameters = {
    'symbol': 'DOGE',
    'convert': 'USD',
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '74f7773e-2411-49ae-b39f-5e46409c3327',
}
session = Session()
session.headers.update(headers)

# Access API, if exception occurs, print error.
try:
    response = session.get(STOCK_ENDPOINT, params=parameters)
    data = json.loads(response.text)
# print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

# Place Json data into list
data_list = [value for (key, value) in data.items()]

# Extract price from Json data. Assign to variable val
doge = data_list[1]
price = doge['DOGE']['quote']['USD']['price']
val = f"{price:.5f}"


# Routes
# Index
@app.route('/')
def home():
    # render index page. val passed to index page as value
    return render_template("index.html", value=val)

# Run Command
if __name__ == '__main__':
    app.run(debug=False)
