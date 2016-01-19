import requests
url = "https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-–-prepared-delivery-state-union-address/"
requests.get(url)
resp = requests.get(url)
text = resp.text
print(text.count("Applause"))
print(text.lower().count("applause"))
print(text.count("<p>"))
