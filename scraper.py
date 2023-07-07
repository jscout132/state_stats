import requests
from bs4 import BeautifulSoup
# from states import states

url = 'https://www.50states.com/tools/thelist.htm'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="content")

def state_birds_scrape():
    bird_url = "https://www.50states.com/bird/"
    birds = requests.get(bird_url)
    soup = BeautifulSoup(birds.content,"html.parser")
    results = soup.find(id="post-748")
    bird_list = results.find_all("div", class_="row")
    state_bird_list = []
    for bird in bird_list:
        state = bird.find('div', class_="col-sm-5 flagsCols textCenter")
        if state == None:
            continue
        else:
            state_bird_list.append(state.text)
    print(state_bird_list)

def capital_scrape():
    capitals = requests.get('https://www.50states.com/tools/thelist.htm')
    soup = BeautifulSoup(capitals.content,'html.parser')
    results = soup.find(id='post-1292')
    cap_list = results.find_all('td')
    state_cap_list = []
    for cap in cap_list:
        capital = cap.find('span')
        state_cap_list.append(capital.text)
    
    capital_list = []
    for i in range(0,len(state_cap_list)):
        if i % 2 != 0:
            capital_list.append(state_cap_list[i])    
    
    print(capital_list)

# capital_scrape()

# scraping for state flower
def flower_scrape():
    flowers = requests.get('https://www.50states.com/flower.htm')
    soup = BeautifulSoup(flowers.content, 'html.parser')
    results = soup.find(id='post-1746')
    print(results)

flower_scrape()