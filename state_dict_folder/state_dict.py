# if i were to make this again, i would set it up as a list with dictionaries as the items
# instead of a dictionary of dictionaries

# TODO: add the numerical values as numbers instead of strings

full_state_dictionary = {
    "AL": {
        "bird": "Yellowhammer",
        "capital": "Montgomery",
        "flower": "Camellia",
        "governor": "Kay Ivey",
        "land_area": "50,750",
        "name": "Alabama",
        "population": "4,903,185",
        "gov_party": "Republican",
        "lat": "32.377716",
        "lon": "-86.300568",
    },
    "AK": {
        "bird": "Willow Ptarmigan",
        "capital": "Juneau",
        "flower": "Alpine Forget Me Not",
        "governor": "Mike Dunleavy",
        "land_area": "570,641",
        "name": "Alaska",
        "population": "731,545",
        "gov_party": "Republican",
        "lat": "58.301598",
        "lon": "-134.420212",
    },
    "AZ": {
        "bird": "Cactus Wren",
        "capital": "Phoenix",
        "flower": "Saguaro Cactus Blossom",
        "governor": "Katie Hobbs",
        "land_area": "113,642",
        "name": "Arizona",
        "population": "7,278,717",
        "gov_party": "Democratic",
        "lat": "33.448143",
        "lon": "-112.096962",
    },
    "AR": {
        "bird": "Northern Mockingbird",
        "capital": "Little Rock",
        "flower": "Apple Blossom",
        "governor": "Sarah Huckabee Sanders",
        "land_area": "52,075",
        "name": "Arkansas",
        "population": "3,017,804",
        "gov_party": "Republican",
        "lat": "34.746613",
        "lon": "-92.288986",
    },
    "CA": {
        "bird": "California Valley Quail",
        "capital": "Sacramento",
        "flower": "California Poppy",
        "governor": "Gavin Newsom",
        "land_area": "155,973",
        "name": "California",
        "population": "39,512,223",
        "gov_party": "Democratic",
        "lat": "38.576668",
        "lon": "-121.493629",
    },
    "CO": {
        "bird": "Lark Bunting",
        "capital": "Denver",
        "flower": "Rocky Mountain Columbine",
        "governor": "Jared Polis",
        "land_area": "103,730",
        "name": "Colorado",
        "population": "5,758,736",
        "gov_party": "Democratic",
        "lat": "39.739227",
        "lon": "-104.984856",
    },
    "CT": {
        "bird": "American Robin",
        "capital": "Hartford",
        "flower": "Mountain Laurel",
        "governor": "Ned Lamont",
        "land_area": "4,845",
        "name": "Connecticut",
        "population": "3,565,287",
        "gov_party": "Democratic",
        "lat": "41.764046",
        "lon": "-72.682198",
    },
    "DE": {
        "bird": "Blue Hen Chicken",
        "capital": "Dover",
        "flower": "Peach Blossom",
        "governor": "John Carney",
        "land_area": "1,955",
        "name": "Delaware",
        "population": "973,764",
        "gov_party": "Democratic",
        "lat": "39.157307",
        "lon": "-75.519722",
    },
    "FL": {
        "bird": "Mockingbird",
        "capital": "Tallahassee",
        "flower": "Orange Blossom",
        "governor": "Ron DeSantis",
        "land_area": "53,997",
        "name": "Florida",
        "population": "21,477,737",
        "gov_party": "Republican",
        "lat": "30.438118",
        "lon": "-84.281296",
    },
    "GA": {
        "bird": "Brown Thrasher",
        "capital": "Atlanta",
        "flower": "Cherokee Rose",
        "governor": "Brian Kemp",
        "land_area": "57,919",
        "name": "Georgia",
        "population": "10,617,423",
        "gov_party": "Republican",
        "lat": "33.749027",
        "lon": "-84.388229",
    },
    "HI": {
        "bird": "Nene",
        "capital": "Honolulu",
        "flower": "Pua Aloalo",
        "governor": "Josh Green",
        "land_area": "6,423",
        "name": "Hawaii",
        "population": "1,415,872",
        "gov_party": "Democratic",
        "lat": "21.307442",
        "lon": "-157.857376",
    },
    "ID": {
        "bird": "Mountain Bluebird",
        "capital": "Boise",
        "flower": "Syringa",
        "governor": "Brad Little",
        "land_area": "82,751",
        "name": "Idaho",
        "population": "1,787,065",
        "gov_party": "Republican",
        "lat": "43.617775",
        "lon": "-116.199722",
    },
    "IL": {
        "bird": "Cardinal",
        "capital": "Springfield",
        "flower": "Violet",
        "governor": "J. B. Pritzker",
        "land_area": "55,593",
        "name": "Illinois",
        "population": "12,671,821",
        "gov_party": "Democratic",
        "lat": "39.798363",
        "lon": "-89.654961",
    },
    "IN": {
        "bird": "Cardinal",
        "capital": "Indianapolis",
        "flower": "Peony",
        "governor": "Eric Holcomb",
        "land_area": "35,870",
        "name": "Indiana",
        "population": "6,732,219",
        "gov_party": "Republican",
        "lat": "39.768623",
        "lon": "-86.162643",
    },
    "IA": {
        "bird": "Eastern Goldfinch",
        "capital": "Des Moines",
        "flower": "Wild Prairie Rose",
        "governor": "Kim Reynolds",
        "land_area": "55,875",
        "name": "Iowa",
        "population": "3,155,070",
        "gov_party": "Republican",
        "lat": "41.591087",
        "lon": "-93.603729",
    },
    "KS": {
        "bird": "Western Meadowlark",
        "capital": "Topeka",
        "flower": "Wild Native Sunflower",
        "governor": "Laura Kelly",
        "land_area": "81,823",
        "name": "Kansas",
        "population": "2,913,314",
        "gov_party": "Democratic",
        "lat": "39.048191",
        "lon": "-95.677956",
    },
    "KY": {
        "bird": "Cardinal",
        "capital": "Frankfort",
        "flower": "Goldenrod",
        "governor": "Andy Beshear",
        "land_area": "39,732",
        "name": "Kentucky",
        "population": "4,467,673",
        "gov_party": "Democratic",
        "lat": "38.186722",
        "lon": "-84.875374",
    },
    "LA": {
        "bird": "Eastern Brown Pelican",
        "capital": "Baton Rouge",
        "flower": "Magnolia",
        "governor": "John Bel Edwards",
        "land_area": "43,566",
        "name": "Louisiana",
        "population": "4,648,794",
        "gov_party": "Democratic",
        "lat": "30.457069",
        "lon": "-91.187393",
    },
    "ME": {
        "bird": "Chickadee",
        "capital": "Augusta",
        "flower": "White pine cone and tassel",
        "governor": "Janet Mills",
        "land_area": "30,865",
        "name": "Maine",
        "population": "1,344,212",
        "gov_party": "Democratic",
        "lat": "44.307167",
        "lon": "-69.781693",
    },
    "MD": {
        "bird": "Baltimore Oriole",
        "capital": "Annapolis",
        "flower": "Black-eyed Susan",
        "governor": "Wes Moore",
        "land_area": "9,775",
        "name": "Maryland",
        "population": "6,045,680",
        "gov_party": "Democratic",
        "lat": "38.978764",
        "lon": "-76.490936",
    },
    "MA": {
        "bird": "Chickadee",
        "capital": "Boston",
        "flower": "Trailing-Arbutus (Mayflower)",
        "governor": "Maura Healey",
        "land_area": "7,838",
        "name": "Massachusetts",
        "population": "6,892,503",
        "gov_party": "Democratic",
        "lat": "42.358162",
        "lon": "-71.063698",
    },
    "MI": {
        "bird": "Robin",
        "capital": "Lansing",
        "flower": "Apple Blossom",
        "governor": "Gretchen Whitmer",
        "land_area": "56,539",
        "name": "Michigan",
        "population": "9,986,857",
        "gov_party": "Democratic",
        "lat": "42.733635",
        "lon": "-84.555328",
    },
    "MN": {
        "bird": "Common Loon",
        "capital": "Saint Paul",
        "flower": "Pink and white lady slipper",
        "governor": "Tim Walz",
        "land_area": "79,617",
        "name": "Minnesota",
        "population": "5,639,632",
        "gov_party": "Democratic-Farmer-Labor",
        "lat": "44.955097",
        "lon": "-93.102211",
    },
    "MS": {
        "bird": "Mockingbird",
        "capital": "Jackson",
        "flower": "Magnolia",
        "governor": "Tate Reeves",
        "land_area": "46,914",
        "name": "Mississippi",
        "population": "2,976,149",
        "gov_party": "Republican",
        "lat": "32.303848",
        "lon": "-90.182106",
    },
    "MO": {
        "bird": "Bluebird",
        "capital": "Jefferson City",
        "flower": "White Hawthorn Blossom",
        "governor": "Mike Parson",
        "land_area": "68,898",
        "name": "Missouri",
        "population": "6,137,428",
        "gov_party": "Republican",
        "lat": "38.579201",
        "lon": "-92.172935",
    },
    "MT": {
        "bird": "Western Meadowlark",
        "capital": "Helena",
        "flower": "Bitterroot",
        "governor": "Greg Gianforte",
        "land_area": "145,556",
        "name": "Montana",
        "population": "1,068,778",
        "gov_party": "Republican",
        "lat": "46.585709",
        "lon": "-112.018417",
    },
    "NE": {
        "bird": "Western Meadowlark",
        "capital": "Lincoln",
        "flower": "Goldenrod",
        "governor": "Jim Pillen",
        "land_area": "76,878",
        "name": "Nebraska",
        "population": "1,934,408",
        "gov_party": "Republican",
        "lat": "40.808075",
        "lon": "-96.699654",
    },
    "NV": {
        "bird": "Mountain Bluebird",
        "capital": "Carson City",
        "flower": "Sagebrush",
        "governor": "Joe Lombardo",
        "land_area": "109,806",
        "name": "Nevada",
        "population": "3,080,156",
        "gov_party": "Republican",
        "lat": "39.163914",
        "lon": "-119.766121",
    },
    "NH": {
        "bird": "Purple Finch",
        "capital": "Concord",
        "flower": "Purple lilac",
        "governor": "Chris Sununu",
        "land_area": "8,969",
        "name": "New Hampshire",
        "population": "1,359,711",
        "gov_party": "Republican",
        "lat": "43.206898",
        "lon": "-71.537994",
    },
    "NJ": {
        "bird": "Eastern Goldfinch",
        "capital": "Trenton",
        "flower": "Violet",
        "governor": "Phil Murphy",
        "land_area": "7,419",
        "name": "New Jersey",
        "population": "8,882,190",
        "gov_party": "Democratic",
        "lat": "40.220596",
        "lon": "-74.769913",
    },
    "NM": {
        "bird": "Roadrunner",
        "capital": "Santa Fe",
        "flower": "Yucca flower",
        "governor": "Michelle Lujan Grisham",
        "land_area": "121,365",
        "name": "New Mexico",
        "population": "2,096,829",
        "gov_party": "Democratic",
        "lat": "35.68224",
        "lon": "-105.939728",
    },
    "NY": {
        "bird": "Eastern Bluebird",
        "capital": "Albany",
        "flower": "Rose",
        "governor": "Kathy Hochul",
        "land_area": "47,224",
        "name": "New York",
        "population": "19,453,561",
        "gov_party": "Democratic",
        "lat": "42.652843",
        "lon": "-73.757874",
    },
    "NC": {
        "bird": "Cardinal",
        "capital": "Raleigh",
        "flower": "American Dogwood",
        "governor": "Roy Cooper",
        "land_area": "48,718",
        "name": "North Carolina",
        "population": "10,488,084",
        "gov_party": "Democratic",
        "lat": "35.78043",
        "lon": "-78.639099",
    },
    "ND": {
        "bird": "Western Meadowlark",
        "capital": "Bismarck",
        "flower": "Wild Prairie Rose",
        "governor": "Doug Burgum",
        "land_area": "68,994",
        "name": "North Dakota",
        "population": "762,062",
        "gov_party": "Republican",
        "lat": "46.82085",
        "lon": "-100.783318",
    },
    "OH": {
        "bird": "Cardinal",
        "capital": "Columbus",
        "flower": "Scarlet Carnation",
        "governor": "Mike DeWine",
        "land_area": "40,953",
        "name": "Ohio",
        "population": "11,689,100",
        "gov_party": "Republican",
        "lat": "39.961346",
        "lon": "-82.999069",
    },
    "OK": {
        "bird": "Scissor-tailed Flycatcher",
        "capital": "Oklahoma City",
        "flower": "Oklahoma Rose",
        "governor": "Kevin Stitt",
        "land_area": "68,679",
        "name": "Oklahoma",
        "population": "3,956,971",
        "gov_party": "Republican",
        "lat": "35.492207",
        "lon": "-97.503342",
    },
    "OR": {
        "bird": "Western Meadowlark",
        "capital": "Salem",
        "flower": "Oregon Grape",
        "governor": "Tina Kotek",
        "land_area": "96,003",
        "name": "Oregon",
        "population": "4,217,737",
        "gov_party": "Democratic",
        "lat": "44.938461",
        "lon": "-123.030403",
    },
    "PA": {
        "bird": "Ruffed Grouse",
        "capital": "Harrisburg",
        "flower": "Mountain Laurel",
        "governor": "Josh Shapiro",
        "land_area": "44,820",
        "name": "Pennsylvania",
        "population": "12,801,989",
        "gov_party": "Democratic",
        "lat": "40.264378",
        "lon": "-76.883598",
    },
    "RI": {
        "bird": "Rhode Island Red Hen",
        "capital": "Providence",
        "flower": "Common Blue Violet",
        "governor": "Dan McKee",
        "land_area": "1,034",
        "name": "Rhode Island",
        "population": "1,059,361",
        "gov_party": "Democratic",
        "lat": "41.830914",
        "lon": "-71.414963",
    },
    "SC": {
        "bird": "Carolina Wren",
        "capital": "Columbia",
        "flower": "Yellow Jessamine",
        "governor": "Henry McMaster",
        "land_area": "30,111",
        "name": "South Carolina",
        "population": "5,148,714",
        "gov_party": "Republican",
        "lat": "34.000343",
        "lon": "-81.033211",
    },
    "SD": {
        "bird": "Ring-necked Pheasant",
        "capital": "Pierre",
        "flower": "Americana Pasque",
        "governor": "Kristi Noem",
        "land_area": "75,898",
        "name": "South Dakota",
        "population": "884,659",
        "gov_party": "Republican",
        "lat": "44.367031",
        "lon": "-100.346405",
    },
    "TN": {
        "bird": "Mockingbird",
        "capital": "Nashville",
        "flower": "Iris",
        "governor": "Bill Lee",
        "land_area": "41,220",
        "name": "Tennessee",
        "population": "6,829,174",
        "gov_party": "Republican",
        "lat": "36.16581",
        "lon": "-86.784241",
    },
    "TX": {
        "bird": "Mockingbird",
        "capital": "Austin",
        "flower": "Bluebonnet",
        "governor": "Greg Abbott",
        "land_area": "261,914",
        "name": "Texas",
        "population": "28,995,881",
        "gov_party": "Republican",
        "lat": "30.27467",
        "lon": "-97.740349",
    },
    "UT": {
        "bird": "Ring-billed Gull",
        "capital": "Salt Lake City",
        "flower": "Sego lily",
        "governor": "Spencer Cox",
        "land_area": "82,168",
        "name": "Utah",
        "population": "3,205,958",
        "gov_party": "Republican",
        "lat": "40.777477",
        "lon": "-111.888237",
    },
    "VT": {
        "bird": "Hermit Thrush",
        "capital": "Montpelier",
        "flower": "Red Clover",
        "governor": "Phil Scott",
        "land_area": "9,249",
        "name": "Vermont",
        "population": "623,989",
        "gov_party": "Republican",
        "lat": "44.262436",
        "lon": "-72.580536",
    },
    "VA": {
        "bird": "Cardinal",
        "capital": "Richmond",
        "flower": "American Dogwood",
        "governor": "Glenn Youngkin",
        "land_area": "39,598",
        "name": "Virginia",
        "population": "8,535,519",
        "gov_party": "Republican",
        "lat": "37.538857",
        "lon": "-77.43364",
    },
    "WA": {
        "bird": "Willow Goldfinch",
        "capital": "Olympia",
        "flower": "Coast Rhododendron",
        "governor": "Jay Inslee",
        "land_area": "66,582",
        "name": "Washington",
        "population": "7,614,893",
        "gov_party": "Democratic",
        "lat": "47.035805",
        "lon": "-122.905014",
    },
    "WV": {
        "bird": "Cardinal",
        "capital": "Charleston",
        "flower": "Rhododendron",
        "governor": "Jim Justice",
        "land_area": "24,087",
        "name": "West Virginia",
        "population": "1,792,147",
        "gov_party": "Republican",
        "lat": "38.336246",
        "lon": "-81.612328",
    },
    "WI": {
        "bird": "Robin",
        "capital": "Madison",
        "flower": "Wood Violet",
        "governor": "Tony Evers",
        "land_area": "54,314",
        "name": "Wisconsin",
        "population": "5,822,434",
        "gov_party": "Democratic",
        "lat": "43.074684",
        "lon": "-89.384445",
    },
    "WY": {
        "bird": "Western Meadowlark",
        "capital": "Cheyenne",
        "flower": "Indian Paintbrush",
        "governor": "Mark Gordon",
        "land_area": "97,105",
        "name": "Wyoming",
        "population": "578,759",
        "gov_party": "Republican",
        "lat": "41.140259",
        "lon": "-104.820236",
    },
}