import httplib2
from bs4 import BeautifulSoup

def getFemaleProfileLinks(url, atttype, attval, file):
    http = httplib2.Http()
    status, response = http.request(url)

    soup = BeautifulSoup(response, "html.parser")
    table = soup.find('table', attrs={atttype : attval})
    for a in table.find_all("a"):
        if "ladies" in a['href']:
            file.write(a['href'] + "\n")
        else:
            file.write("/ladies/" + a['href'] + "\n")

def getMaleProfileLinks(url, atttype, attval, file):
    http = httplib2.Http()
    status, response = http.request(url)

    soup = BeautifulSoup(response, "html.parser")
    td = soup.find_all('td', attrs={atttype : attval})
    for row in td:
        for a in row.find_all("a"):
            file.write(a['href'] + "\n")

outfile = open("links.txt", "w")

outfile.write("18-23 ladies\n")
getFemaleProfileLinks('http://www.meet-an-inmate.com/ladies/18-23.htm', 'id',
                'table161', outfile)
outfile.write("50+ ladies\n")
getFemaleProfileLinks('http://www.meet-an-inmate.com/ladies/50-65-1.htm', 'id',
                'table161', outfile)
outfile.write("18-21 men\n")
getMaleProfileLinks('http://www.meet-an-inmate.com/male/18-21.htm', 'style',
                'height: 91px', outfile)
outfile.write("50+ men\n")
getMaleProfileLinks('http://www.meet-an-inmate.com/male/50-65.htm', 'class',
                'auto-style171', outfile)
