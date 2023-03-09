import requests
 
# Making a get request
response = requests.get('https://api.github.com/')
from google import google
num_page = 1
search_results = google.search(response, num_page)
for result in search_results:
    print(result.description)
 num_page2 = 2
