




def ES(symbol):#get earning surprises for last three quarters
#example: ES("AApl")

    import time
    from selenium import webdriver
    #from selenium import driver
    #CLICK ANY BUTTONS
    #driver.get("https://www.nasdaq.com/market-activity/stocks/aapl/earnings")
    #more_buttons = driver.find_elements_by_class_name("moreLink")
    #for x in range(len(more_buttons)):
    #  if more_buttons[x].is_displayed():
    #      driver.execute_script("arguments[0].click();", more_buttons[x])

    from bs4 import BeautifulSoup
    #import requests
    import time
    #import pandas as pd
    import re
    header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}
    url = "https://www.nasdaq.com/market-activity/stocks/"+str(symbol)+"/earnings"

    #page_source = requests.get(url, headers= header)#used to be in geckodriver-master/geckodriver
    #driver = webdriver.Firefox()
    driver = webdriver.Firefox(executable_path ='/home/or/Desktop/here/geckodriver')
    #from selenium import webdriver

    driver.get(url)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    print ('\n' + '\n')

    #time.sleep(1)#only human after all
    #time.sleep(.3)
    page_source = driver.page_source
    #print (page_source)
    soup = BeautifulSoup(page_source, features="lxml")#'lxml')
    driver.quit()
    QE = soup.find_all("td", {"class": "earnings-surprise__table-cell"})
    #print ("this is qe:" + str(QE))
    sum =0#sum of % earnings surprise for last 3 quarters
    av =0#averarge earnings surprise
    var=0#surprise variance
    sup =0#float version of the earnings surprise string
    sups = []#list of last 3 quarters earning surprises

    j=0#loop counter

    #for surprise in QE:
    for i in range (3, len(QE), 4):
        sup = re.findall(r"[-+]?\d*\.\d+|\d+|[-+]?\d*\.\d+\d+",str(QE[i]))#The site has earning surprises in various formats, both single digit, double digit and integer.
        #print (sup)
        #sup = surprise.strip('<td class="earnings-surprise__table-cell">)').strip("</td>")
        #if (len(sup)>1):
        #    continue
        s = float(sup[0])
        #if (s < 0 ):
        #    break#underperformed
        sups.append(s)
        #print(s)
        sum += s
        i += 4
        j += 1

    #print (sups )
    print("quarter surprises for " + symbol + ": " + str(sups[0]) + ", " + str(sups[1]) + ", " + str(sups[2]) + ", "  + str(sups[3]) )

    for i in range(0,4):
        av += sups[i]
    av = av/4
    print (av)

    for i in range(0,4):
        var += (abs(sups[i]-av))**2#variance is the average of squared differences from the mean.
    var = var / 4
    print(var)
    si = ((av**2) / var)#One potential "sustainability" indicator
    if (av<0):
        si = -si
    #A high earning average and low variance indicates growth and stability so the higher this number is the better.
    #It is desirable for a stock to beat it's profit projections (high earning surprise average) and do so in a consistent way (low variance) which indicates a company is ready to expand.
    result =  [sups, av, var, si]

    return result
