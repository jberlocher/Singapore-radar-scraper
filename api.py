from bs4 import BeautifulSoup
import requests
import urllib3.request
import re
import shutil
import os.path

j=0
print("SG Radar scraper v1.0")
#print("Radar options:")
#print("Option 1 - Scrape last 2 hours of data")
#print("Option 2 - Scrape last 7 days of data")
#j=input("Input option: ")


print("Request sent...")

url = "http://www.weather.gov.sg/weather-rain-area-50km/"
response = requests.get(url)

print("Status code: ",response.status_code)

soup = BeautifulSoup(response.text,"html.parser")
holder=soup.find_all(id=re.compile("^2021"))


#initialize list to proper length
links=[]
cleanlinks=[]
filenames=[]
for i in range(len(holder)-1):
    links.append(0)
    cleanlinks.append(0)
    filenames.append(0)



#convert to string and store in list
for i in range(len(holder)-1):
    links[i]=str(holder[i])
    
#slice list entry to get link and filename
for element in range(len(links)):
    cleanlinks[element]=links[element][65:154]
    filenames[element]=links[element][114:154]

print("Links and filenames parsed...")

#x is link
#y is filename

def download_image(x,y):
    response = requests.get(x, stream=True)
    realname = y
    
    #file = open("/Users/jakeberlocher/code/{}".format(realname), 'wb')
    #response.raw.decode_content = True
    #shutil.copyfileobj(response.raw, file)
   
    if response.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        response.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
        with open(y,'wb') as f:
            shutil.copyfileobj(response.raw, f)
        
        print('Image sucessfully Downloaded: ',y)
    else:
        print('Image Couldn\'t be retreived')


print("Downloading images...")

for i in range(len(cleanlinks)):
    if os.path.exists(filenames[i]):
        print(filenames[i], " already exists")
        continue
    else:
        download_image(cleanlinks[i],filenames[i])










