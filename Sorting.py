import os,sys,requests
from bs4 import BeautifulSoup
url = requests.get("https://www.online-convert.com/file-type")
soup = BeautifulSoup(url.content,"html.parser")
extensions = "td > a"
extensionName = "tr > td:nth-of-type(2)"

fileNames = {}

for k,v in zip(soup.select(extensions),soup.select(extensionName)):
    fileNames[k.get_text()] = v.get_text().replace(" ","")

try:
    folderLocation = sys.argv[1]
except:
    folderLocation = r"{}".format(input("Enter the folder you want to change: "))

os.chdir(folderLocation)

for file in os.listdir(folderLocation):
    extension = file.rsplit(".")[-1]
    if extension in fileNames.keys():
        folderName = fileNames[extension]
        try:
            os.mkdir(folderName)
        except:
            print(end="")
        os.rename(file,f"{folderName}\\{file}")
    