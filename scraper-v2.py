import urllib.request

def scrape(url, key):
    btsrc = urllib.request.urlopen(url)
    bt = btsrc.read()
    ssrc = bt.decode("utf8")
    btsrc.close()

    trf = 'scraper-output'
    ct = 0

    while True:
        try:
            outputData = open(trf + str(ct) + '.txt', 'x', encoding="utf8")
            break
        except FileExistsError:
            ct += 1


    ct = 0
    locator = key

    for character in range(len(ssrc)-4):
        if ssrc[character:(character+len(locator))] == locator:
            while ssrc[character+len(locator)+ct+1] != '\"':
                ct+=1

            outputData.write(ssrc[(character+len(locator)):(character+len(locator)+ct+2)] + "\n")
            ct = 0

websiteList = ["https://play.google.com/store/apps/details?id=com.robtopx.geometryjumplite"]
keyList = ["5,null,"]

for i in range(len(websiteList)):
    scrape(websiteList[i], keyList[i])