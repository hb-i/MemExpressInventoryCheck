# Scrap Memory Express URL, if any item in results isn't out of order than send an email alert.
import requests
from bs4 import BeautifulSoup
import smtplib

# Enter the URL of filtered product(s) you want, all must be out of stock.
URL = 'https://www.memoryexpress.com/Category/VideoCards?FilterID=45788ec3-6bb1-e460-abe6-afa274b9d30e'
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')

results = soup.find_all("div", {"class": "c-shca-icon-item__body-extras"})
resultcount = len(results)
print("Total Results: " + str(len(results)))

# Since first item in a loop has index of 0. Otherwise last item in loop will throw error if result count var is used.
loopitemcount = len(results) - 1

i = 0
sendmail = 0 # Send mail trigger
while i <= loopitemcount:
    currentitem = results[i].find("span")
    if "Out" in str(currentitem):
        #print ("OUT OF STOCK!")
        pass
    else:
        #print ("IN STOCK!")
        sendmail = 1

    i += 1

if sendmail == 1:
    # Send email if any item is found in stock
    smtpObj = smtplib.SMTP('smtp.example.com', 25)
    smtpObj.ehlo()
    smtpObj.sendmail(' sender@example.com ', ' recipient@example.com ', 'Subject: MemExpress Alert\nItem(s) found in stock')
    smtpObj.quit()
