import requests
from bs4 import BeautifulSoup
class define:
    def __init__(self):
        pass

    def get_word_defination(self,word):
        l = []
        url = 'https://www.dictionary.com/browse/' + word + '?s=t'
        # inp = input()
        try:
            r = requests.get(url,headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9,hi;q=0.8'})
            soup = BeautifulSoup(r.content, 'html.parser')
            c1 = soup.find(class_='css-1o58fj8 e1hk9ate4').find_all('div')
        except:
            return ["Umm!! Not Found Defination for this Word"]

        else:
            for i in c1:
                l.append(i.find('span').text)
            return l
#           for i in range(2):
#               print(c1[i].find('span').text)
#
#             for i in c1:
#                 print(i.find('span').text)
