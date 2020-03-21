#! /usr/bin/python3
import bs4, requests,re
# spaces = re.compile("\s{2,}")
def temperature(temp):
    regex = re.compile("\d+")
    final = regex.search(temp[0].text).group()
    return int(final)
url = "https://www.weather2umbrella.com/weather-forecast-pristina-serbia-en/7-days"
site = requests.get(url)
try:
    site.raise_for_status()
    soup = bs4.BeautifulSoup(site.text,"html.parser")
    weather = soup.select("#seven_days > div:nth-of-type(2)) > div > div > div > a.day_wrap.today.selected_day > div.weather_per_day_wrap > div.day_description > p")
    low = soup.select("#seven_days > div:nth-of-type(2) > div > div > div > a.day_wrap.today.selected_day > div.weather_per_day_wrap > div.day_temperatures > div.min_day_temp_section > p")
    high = soup.select("#seven_days > div:nth-of-type(2) > div > div > div > a.day_wrap.today.selected_day > div.weather_per_day_wrap > div.day_temperatures > div.max_day_temp_section > p")
    print(f"WEATHER REPORT:{' '.join((weather[0].text.strip()).split())}\nTemperature from {(low[0].text).strip()} to {(high[0].text).strip()}")
    print(f"With an average Temperature of: {(temperature(low)+temperature(high))/2}")
except Exception as e:
    print("The site isn't corrently working")
    print("Because:",e)