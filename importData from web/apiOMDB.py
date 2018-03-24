import requests 
url="http://www.omdbapi.com/?apikey=ff21610b&t=veronica"


# Assign URL to variable: url


# Package the request, send the request and catch the response: r
r = requests.get(url)

#decoding jason to dictionary
json_data=r.json()
for key in json_data.keys():
    print(key+'=',json_data[key])
    
