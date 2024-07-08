import requests
from bs4 import BeautifulSoup

# Grab the GitHub username and URL
github_name = input("What's your Github User? ")
url = "https://github.com/" + github_name
res = requests.get(url)

# Check if the request was successful
if res.status_code == 200:
    # Store the response in htmlData
    htmlData = res.content

    # Making it look good so I understand what the HTML is
    parsedData = BeautifulSoup(htmlData, "html.parser")
    print(parsedData.prettify())

    # Find the profile picture
    pfp = parsedData.find('img', {'alt': 'Avatar'})
    if pfp:
        pfp_url = pfp['src']
        print("Profile picture URL:", pfp_url)
    else:
        print("PFP missing")
else:
    print("Couldn't retrieve the page. Status code:", res.status_code)