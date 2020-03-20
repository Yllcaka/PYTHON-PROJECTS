import bs4,requests,sys
def Ebay(url):
    site = requests.get(url)
    site.raise_for_status()
    soup = bs4.BeautifulSoup(site.text,"html.parser")
    selector = soup.select('#prcIsum')
    print(selector[0].text)
Ebay(sys.argv[1])