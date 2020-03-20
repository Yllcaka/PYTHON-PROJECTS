#! /usr/bin/python3
import bs4, requests,re
def temperature(temp):
    regex = re.compile("\d+")
    final = regex.search(temp[0].text).group()
    return int(final)
url = "https://www.bbc.com/weather/786714"
site = requests.get(url)
try:
    site.raise_for_status()
    soup = bs4.BeautifulSoup(site.text,"html.parser")
    weather = soup.select("#daylink-0 > div.wr-day__body > div.wr-day__weather-type-description-container > div")
    low = soup.select("#daylink-0 > div.wr-day__body > div.wr-day__details-container > div > div.wr-day__temperature > div > div.wr-day-temperature__high > span.wr-day-temperature__high-value > span > span.wr-value--temperature--c")
    high = soup.select("#daylink-0 > div.wr-day__body > div.wr-day__details-container > div > div.wr-day__temperature > div > div.wr-day-temperature__low > span.wr-day-temperature__low-value > span > span.wr-value--temperature--c")
    print(f"WEATHER REPORT:\n{weather[0].text}\nTemperature from {low[0].text} to {high[0].text}")
    print(f"With an average Temperature of: {(temperature(low)+temperature(high)/2)}")
except:
    print("The site isn't corrently working")