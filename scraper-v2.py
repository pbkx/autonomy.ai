import urllib.request
btsrc = urllib.request.urlopen("https://stackoverflow.com/questions/24153519/how-to-read-html-from-a-url-in-python-3")
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
locator = "text"

for character in range(len(ssrc)-4):
    if ssrc[character:(character+len(locator))] == locator:
        while ssrc[character+len(locator)+ct+1] != '\"':
           ct+=1

        outputData.write(ssrc[(character+len(locator)):(character+len(locator)+ct+2)])
        ct = 0

