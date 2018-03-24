from urllib.request import urlopen , Request
url="https://www.linkedin.com"
requ=Request(url)
resp=urlopen(requ)
html=resp.read()
resp.close()

#or using a "get" with package "requests"
import requests


# Specify the url: url
url="https://www.facebook.com"

# Packages the request, send the request and catch the response: r
r=requests.get(url)

# Extract the response: text
text=r.text

# Print the html
print(text)
