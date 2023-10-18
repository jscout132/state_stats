import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from state_dict import full_state_dictionary
from gov_dict import gov_dictionary


def test():
    url = 'https://www.50states.com/tools/thelist.htm'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="content")

ua = UserAgent()
HEADERS = {'User-Agent': ua.random}

def gov_bio_test():
    state = 'alabama'
    gov = requests.get(f"https://www.nga.org/governors/{state}/", headers=HEADERS)
    soup = BeautifulSoup(gov.content,'html.parser')
    bio = soup.find_all('p')
    bio_list = [i.text for i in bio[0:3]]
# gov_bio_test()


def gov_info_scrape():
    file_path = 'app/state_dict_folder/gov_dict.py'
    for k,v in full_state_dictionary.items():
        gov_dictionary.update({v['name']:{'gov_name':v['governor']}})

    for k,v in gov_dictionary.items():
        gov = requests.get(f"https://www.nga.org/governors/{k}/", headers=HEADERS)
        soup = BeautifulSoup(gov.content,'html.parser')
        
        # scraping for term, birthdate, state born, and schooling
        terms = soup.find_all('li', class_='item')
        term_list = [term.text.strip() for term in terms[0:5]]
        clean_term = [term[11:].lstrip() for term in term_list]

        # scraping for 1st 2 para bio section
        bio = soup.find_all('p')
        bio_list = [i.text for i in bio[0:3]]

        # removing empty lists to prevent indexing errors
        trouble_states = []
        if len(clean_term) > 0:
            v.update({'terms':clean_term[0]})
            v.update({'birthdate':clean_term[2]})
            v.update({'bith_state':clean_term[3]})
            v.update({'school':clean_term[4]})
            v.update({'bio':bio_list})
        else:
            trouble_states.append(k)

    print(trouble_states)

    with open(file_path,'w') as file:
        file.write(str(gov_dictionary))
# gov_info_scrape()

def two_word_states():
    states = ['New-Hampshire', 'New-Jersey', 'New-York', 'New-Mexico', 'North-Carolina', 'North-Dakota', 'Rhode-Island', 'South-Carolina', 'South-Dakota', 'West-Virginia']
    for state in states:
        gov = requests.get(f"https://www.nga.org/governors/{state}/", headers=HEADERS)
        soup = BeautifulSoup(gov.content,'html.parser')
        
        # scraping for term, birthdate, state born, and schooling
        terms = soup.find_all('li', class_='item')
        term_list = [term.text.strip() for term in terms[0:5]]
        clean_term = [term[11:].lstrip() for term in term_list]
        bio = soup.find_all('p')
        bio_list = [i.text for i in bio[0:3]]
        print(state)
        print('"terms":', clean_term[0])
        print('"birthdate":', clean_term[2])
        print('"birth_state":', clean_term[3])
        print('"school":', clean_term[4])
        print('"bio":', bio_list)

# two_word_states()



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

# gov_party_scrape()


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


def num_pop_land():
    for k,v in full_state_dictionary.items():
        v['land_area_num'] = int(v['land_area'].replace(',',''))
        v['pop_num'] = int(v['population'].replace(',',''))
# num_pop_land()

def lank_pop_rankings():
    state_name = [i['name'] for i in full_state_dictionary.values()]
    land_area_dict = dict.fromkeys(state_name, 0)
    pop_dict = dict.fromkeys(state_name, 0)
    for v in full_state_dictionary.values():
        land_area_dict.update({v['name']: v['land_area_num']})
        pop_dict.update({v['name']: v['pop_num']})
        
    sorted_land_area = sorted(land_area_dict.items(), key=lambda x:x[1], reverse=True)
    sorted_pop = sorted(pop_dict.items(), key=lambda x:x[1], reverse=True)

    ranked_land = [(i[0],sorted_land_area.index(i)) for i in sorted_land_area]
    ranked_pop = [(i[0],sorted_pop.index(i)) for i in sorted_pop]

    for k,v in full_state_dictionary.items():
        for i in ranked_land:
            if i[0] == v['name']:
                full_state_dictionary[k]['land_area_rank'] = i[1]+1

    for k,v in full_state_dictionary.items():
        for i in ranked_pop:
            if i[0] == v['name']:
                full_state_dictionary[k]['pop_rank'] = i[1]+1
    print(full_state_dictionary)
# lank_pop_rankings()
