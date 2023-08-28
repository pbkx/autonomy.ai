with open('google-play-source.txt', 'r', encoding="utf8") as fin:
    sourceData = fin.read()

outputData = open('scraper-output.txt', 'x', encoding="utf8")

counter = 0
locator = "5,null,"

for character in range(len(sourceData)-4):
    if sourceData[character:(character+len(locator))] == locator:
        while sourceData[character+len(locator)+counter+1] != '\"':
           counter+=1

        outputData.write(sourceData[(character+len(locator)):(character+len(locator)+counter+2)])
        counter = 0

