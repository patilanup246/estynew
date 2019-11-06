import requests
from bs4 import BeautifulSoup
import csv

ti = 0
quotes = []  # a list to store quotes
filepathlang = 'sort.txt'
with open(filepathlang) as fpl:
    for cntlag, linelag in enumerate(fpl):
        try:
            for i in range(1, 800):
                try:
                    print(str(linelag).replace("\n", "") + " Page :" + str(i))
                    URL = "https://www.etsy.com/in-en/search?q=printable+wall+art&explicit=1&attr_1="+str(linelag).replace("\n", "")+"&order=date_desc&ref=pagination&page="+str(i)
                    r = requests.get(URL)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    table = soup.findAll('p', attrs={'class': 'text-gray-lighter text-body-smaller display-inline-block'})

                    if table.__len__() == 0:
                        break
                        raise ValueError('A very specific bad thing happened.')

                    for row in table:
                        try:
                            if row.string in quotes:
                                print("Element Exists")
                            else:
                                ti = ti + 1
                                print(str(ti))
                                quotes.append(row.string)
                        except Exception:
                            print("error0")
                            pass

                except Exception:
                    print("error1")
                    break
            with open("alllinks"+str(linelag).replace("\n", "")+".txt", 'w') as f:
                for item in quotes:
                    f.write("%s\n" % item)
        except Exception:
            print("error2")
            pass

