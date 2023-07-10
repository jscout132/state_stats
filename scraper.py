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
    flower_list = results.find_all("div", class_='row')
    state_flower_list = []
    for flower in flower_list:
        flow = flower.find_all('div', class_="col-sm-3 flagsCols textCenter")
        if len(flow) > 0:    
            state_flower_list.append(flow[1].text)
    # print(state_flower_list)
# flower_scrape()

def gov_scrape():
    governors = requests.get('https://en.wikipedia.org/wiki/List_of_current_United_States_governors')
    soup = BeautifulSoup(governors.content, 'html.parser')
    results = soup.find(id="mw-content-text")
    gov_table = results.find('table', class_='wikitable')
    gov_tbody = gov_table.find('tbody')
    gov_th = gov_tbody.find_all('th')
    gov_name_list = []
    for i in gov_th:
        gov_name = i.find('a')
        if gov_name != None:
            gov_name_list.append(gov_name.text)
    print(gov_name_list)
# gov_scrape()

def gov_party_scrape():
    governors = requests.get('https://en.wikipedia.org/wiki/List_of_current_United_States_governors')
    soup = BeautifulSoup(governors.content, 'html.parser')
    results = soup.find(id='mw-content-text')
    gov_table = results.find('table', class_='wikitable')
    gov_tbody = gov_table.find('tbody')
    gov_td = gov_tbody.find_all('td')
    party_list = []
    for i in gov_td:
        gov_party = i.find('a')
        if gov_party != None:
            party_list.append(gov_party.text)

    
    print(party_list)
    # party_list = ['Democratic','Republican']
    # gov_party_list = []
    # for i in gov_td:
    #     gov_party = i.find('a')
    #     if gov_party != None: #and gov_party.text in party_list:
    #         gov_party_list.append(gov_party.text)

    # print(gov_party_list)
gov_party_scrape()


def state_population_scrape():
    population_request = requests.get('https://www.50states.com/population-by-state/')
    soup = BeautifulSoup(population_request.content, 'html.parser')
    results = soup.find(id='post-353907')
    pop_tbody = results.find('tbody')
    pop_td = pop_tbody.find_all('td')
    # creating the list of states and their population
    pop_list = [i.text for i in pop_td]

    # cleaning up population list to remove state number and create state dictionary
    pop_dict = {}
    while len(pop_list) >= 3:
        # Remove the first item
        pop_list.pop(0)
        
        # Create a dictionary entry
        key = pop_list.pop(0)
        value = pop_list.pop(0)
        pop_dict[key] = value
    # making dict keys into a list for sorting
    state_pop_list = list(pop_dict.keys())
    state_pop_list.sort()

    # dictionary comprehension to rebuild the dict in alpha order
    state_pop_sorted = {i: pop_dict[i] for i in state_pop_list}

    # creating a list of just populations without state names, but still in alpha order
    population = [i for i in state_pop_sorted.values()]
    print(population)

# state_population_scrape()


def state_land_area_scrape():
    land_request = requests.get('https://statesymbolsusa.org/symbol-official-item/national-us/uncategorized/states-size')
    soup = BeautifulSoup(land_request.content, 'html.parser')
    results = soup.find('tbody')
    land_td = results.find_all('td')

    # creating land area list, excluding first row on site table
    land_list = [i.text for i in land_td[3:]]

    land_dict = {}
    while len(land_list) >= 3:
        # removing numeric count of state
        land_list.pop(0)

        key = land_list.pop(0)
        value = land_list.pop(0)
        # creating land dictionary
        land_dict[key] = value

    land_area_list = list(land_dict.keys())
    land_area_list.sort()

    # creating an alpha sorta dictionary
    land_area_sorted = {i: land_dict[i] for i in land_area_list}

    land_area = [i for i in land_area_sorted.values()]
    print(land_area)
    

# state_land_area_scrape()