from bs4 import BeautifulSoup
q = __import__('queue').Queue()
bs = BeautifulSoup(__import__('requests').get('https://www.macmillandictionary.com/us/thesaurus-category/american/insulting-words-for-someone-who-is-stupid-or-silly').content, 'html.parser')
for word in bs.find_all('a', {'class': 'thes-ref-title-link'}):
    q.put(word.get('title'))
input('Dear diary, who am I?')
while not q.empty(): input('You are a %s' % q.get())