import sys
from bs4 import BeautifulSoup as Soup

def parseLog(file):
    print('hola')
    handler = open(file).read()
    soup = Soup(handler,'lxml')
    for message in soup.findAll('section'):
        title = message.find('num').attrs['value']
        filename = format(title + ".xml")
        with open('./xmls/'+filename, 'w') as f:
            f.write(str(message))
            f.close()

        print(message.find('num').attrs['value'])

if __name__ == "__main__":
    parseLog('usc26.xml')