# witter science gifs scraper
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from bs4 import BeautifulSoup as bs


# chromedriver = '/Users/samuelaltarac/Desktop/python programs/chromedriver'
browser = webdriver.Chrome()
browser.get('https://twitter.com/Learn_Things')

time.sleep(1)

user = browser.find_element_by_class_name("email-input")
user.send_keys('mraltarac')

p = browser.find_element_by_name("session[password]")
p.send_keys('**********')

btn = browser.find_element_by_class_name("submit")
btn.send_keys(Keys.RETURN)




h = browser.find_element_by_tag_name('HTML')

for i in range(0,100):
    h.send_keys(Keys.END)
    time.sleep(0.5)
#     lis = soup.find_all('li', {"class": ['js-stream-item', 'stream-item', 'stream-item']})
#     l = len(lis)
#     if l == 810:
#         break


time.sleep(1)

html_doc = browser.page_source
soup = bs(html_doc, 'html.parser')

lis = soup.find_all('li', {"class": ['js-stream-item', 'stream-item', 'stream-item']})

l = len(lis)

print('number of tweets should be: ' + str(l))

tweets = soup.find_all("div", {"class": ['tweet', 'js-stream-tweet', 'js-actionable-tweet']}, limit=l)
descriptions = soup.find_all("p", {"class": ['TweetTextSize', 'TweetTextSize--normal', 'js-tweet-text', 'tweet-text']}, limit=l)

links = []
descs = []
# print(tweets)

for t in tweets:
    links.append('https://twitter.com' + str(t.attrs['data-permalink-path']))

for d in descriptions:
    descs.append(d.text)



print(len(links))
print(len(descs))


browser.quit()



d = {'tags': 'twitter', 'descriptions' : descs, 'links': links}

df = pd.DataFrame(data=d)

df.to_csv('science_GIFs4.csv')
