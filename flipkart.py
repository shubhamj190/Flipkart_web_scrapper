import requests
from bs4 import BeautifulSoup
import smtplib
import time

url='https://www.flipkart.com/samsung-138cm-55-inch-ultra-hd-4k-curved-led-smart-tv/p/itmek9rs5kmmc6wh?pid=TVSEK9RSKAZKFBUX&lid=LSTTVSEK9RSKAZKFBUXCXAERR&marketplace=FLIPKART&srno=s_1_2&otracker=AS_Query_OrganicAutoSuggest_2_10_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_2_10_na_na_na&fm=SEARCH&iid=a97ef762-70a7-4d19-8f2d-0afbc61809b7.TVSEK9RSKAZKFBUX.SEARCH&ppt=sp&ppn=sp&ssid=9bdk4apskg0000001599496837064&qH=fa4451ed2957402b'

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

def check_price():
    page=requests.get(url,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')
    # print(soup)

    title=soup.find("span", {"class": "_35KyD6"}).get_text()

    price=soup.find('div',{'class':"_1vC4OE _3qQ9m1"}).get_text()

    converted_price=price[1:]

    final_price=int(converted_price.replace(',',''))
    # print(final_price)
    # print(type(final_price))

    if(final_price < 240000):
        send_mail()

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('shubhjadh1996@gmail.com','nokia300')

    subject='price fell down'

    body='check the flipkart link https://www.flipkart.com/samsung-138cm-55-inch-ultra-hd-4k-curved-led-smart-tv/p/itmek9rs5kmmc6wh?pid=TVSEK9RSKAZKFBUX&lid=LSTTVSEK9RSKAZKFBUXCXAERR&marketplace=FLIPKART&srno=s_1_2&otracker=AS_Query_OrganicAutoSuggest_2_10_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_2_10_na_na_na&fm=SEARCH&iid=a97ef762-70a7-4d19-8f2d-0afbc61809b7.TVSEK9RSKAZKFBUX.SEARCH&ppt=sp&ppn=sp&ssid=9bdk4apskg0000001599496837064&qH=fa4451ed2957402b'

    msg=f"Subject:{subject}\n\n{body}"

    server.sendmail('shubhjadh1996@gmail.com','shubhamjadhav190@gmail.com',msg)
    print('Hey email has been sent')


while(True):
    check_price()
    time.sleep(43200)