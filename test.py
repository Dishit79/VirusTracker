from flask import Flask,render_template, request
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

app = Flask(__name__)


@app.route('/')

def main():

    my_url = 'https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19.html?utm_campaign=not-applicable&utm_medium=vanity-url&utm_source=canada-ca_coronavirus'

    uclient = uReq(my_url)

    pagehtml = uclient.read()
    uclient.close()

    pagesoup = soup(pagehtml, "html.parser")
    data = pagesoup.findAll("p", {"class":"h2 mrgn-tp-md"})
    update = pagesoup.findAll("p", {"class":"text-right h3 mrgn-tp-sm"})


    date = update[0]
    data1 = data[0]
    data2 = data[1]
    data3 = data[2]
    data4 = data[3]

    lastupdate = date.text
    ppltestes = data1.text
    concases = data2.text
    probcases = data3.text
    deaths = data4.text

    onturl = 'https://covid-19.ontario.ca/'

    ontclient = uReq(onturl)

    intpagehtml = ontclient.read()
    ontclient.close()

    pagesoup2 = soup(intpagehtml, "html.parser")
    ontdata = pagesoup2.findAll('div' , {'class' : 'ontario-infographic-number'})
    date = pagesoup2.findAll('p' , {'class' : 'ontario-margin-top-32-!'})

    date10 = date[1]
    numcases = ontdata[0]
    res = ontdata[1]
    death = ontdata[2]
    hos = ontdata[3]
    tw = ontdata[4]
    te = ontdata[5]


    d1 =  numcases.text
    d2 =  res.text
    d3 =  death.text
    d4 =  hos.text
    d5 = tw.text
    d6 = te.text
    up = date10.text

    return render_template('index.html', d1=d1, d2=d2, d3=d3, d4=d4, d5=d5, d6=d6, up=up, a=lastupdate, b=ppltestes, c=concases , d=probcases, e=deaths)


if __name__ == "__main__" :
    app.run(debug=True)
