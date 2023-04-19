import requests

r = requests.get("http://www.google.com")
print(r.status_code)
print(r.headers)
print(r.headers["Date"])

print(r.text)