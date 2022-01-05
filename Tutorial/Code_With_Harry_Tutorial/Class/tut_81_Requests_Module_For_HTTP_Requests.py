
import requests

"""  get request """
r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
print(r.text)
# this will give you the contect of the link
print(r.status_code)
# this will return the status code

# url = "www.something.com"
# this is the url for the post request
# data = {
#     "p1":4,
#     "p2":8
# }
# data is the data of parameter for send in the url
# r2 = requests.post(url=url, data=data)
