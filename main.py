import requests
from bs4 import BeautifulSoup
import os


def req(text):
    slack_url = os.environ['SLACK_URL']
    requests.post(slack_url, json={
        "text": text
    })


def main():
    url = 'https://www.sac.or.kr/site/main/show/dataTicketList?cp=1&pageSize=10&ticketOpenFlag=Y&sortOrder=B.TICKET_OPEN_DATE&sortDirection=DESC'
    resp = requests.get(url)
    list = resp.json()["paging"]["result"]

    text = '예술의 전당 티켓 오픈 알리미\n\n'

    for item in list:
        startTicketingDate = item["TICKET_OPEN_DATE"]
        # category = [item["CATEGORY_PRIMARY_NAME"],
        #             item["CATEGORY_SECONDARY_NAME"]]
        subject = item["PROGRAM_SUBJECT"]
        date = [item["END_DATE"], item["END_WEEK"]]
        time = item["PROGRAM_PLAYTIME"]
        price = item["PRICE_INFO"]
        sn = item["SN"]
        link = "https://www.sac.or.kr/site/main/show/show_view?SN="+str(sn)
        print(startTicketingDate,  subject, date, time, price, link)
        # print(startTicketingDate, category, subject, date, time, price, link)
        print()
        text += f"<https://www.sac.or.kr/site/main/show/show_view?SN={sn}|{subject}>\n"
        text += f"예매시작일: {startTicketingDate}\n"
        text += f"공연일: {date} {time}\n"
        text += f"가격: {price}\n"
        text += f"\n"
    req(text)


main()
