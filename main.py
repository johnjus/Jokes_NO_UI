import requests
from bs4 import BeautifulSoup
import random
#e
#global list of jokes so I can build once and grab it with other function
dad_jokes = []
pun_jokes = []

#int value to determine which joke humor has been selected by the user.
#0 = no joke humor has been selected
#1 = dad jokes have been selected
#2 = pun jokes have been selected


#data scrap the following webpage to grab the jokes I wanted for this application
def generatedadjokes():
    global dad_jokes
    url = 'https://www.countryliving.com/life/a27452412/best-dad-jokes/'
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    # print(set([t.parent.name for t in text]))
    all_output = []
    blacklist = [
            'h1', 'body', 'title', 'form', 'style', 'nav', 'div', 'a', 'h2', 'header', 'img', 'svg', 'html', 'em', 'main',
            'ul', 'time', 'script', 'head', 'footer', 'p', 'span', 'label', '[document]', 'g', 'small'

        ]
    for t in text:
        if t.parent.name not in blacklist:
            all_output.append(t)
    for i in range(0, len(all_output)):
        #checked data before 25 and after 89 is spaces
        if 25 < i < 89:
            dad_jokes.append(all_output[i])


#data scrap the following webpage to grab the jokes I wanted for this application
def genereatepunjokes():
    global pun_jokes
    url = 'https://inews.co.uk/light-relief/jokes/best-pun-based-jokes-170096'
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    all_outputs = []
    blacklist = [
        'a', 'div', 'span', 'script', 'figcaption', 'title', 'strong', '[document]', 'blockquote', 'style', 'button',
        'body', 'h2', 'h3', 'h1'
    ]

    for t in text:
        if t.parent.name not in blacklist:
            all_outputs.append(t)
    for i in range(0, len(all_outputs)):
        if 3 < i < 55:
            pun_jokes.append(all_outputs[i])

#generating all joke sections here
genereatepunjokes()
generatedadjokes()

#allows me to grab a random joke from the array of this jokes type
def getrandomdadjoke():
    num =  random.randint(0, 62)
    return dad_jokes[num]
#""
def getrandompunjoke():
    num = random.randint(0,50)
    return pun_jokes[num]

#simple helper method to change the int value of what joke type is being selected
def whatjokeselected(num):
    global which_joke
    which_joke = num

#needed this to return me a joke from my joke type lists
def getjoke(value):
    if value == 1:
        return getrandomdadjoke()
    elif value == 2:
        return getrandompunjoke()


def driver():
    print("Welcome to Jokes4You!")
    cont = True
    again = False
    otherchoice = None
    userchoice = None
    anotherone = None
    while cont:
        userchoice = input("Choose an option of Dad Jokes or Pun Jokes")
        if userchoice.lower() == "dad joke":
            print(getjoke(1))
            otherchoice = "Pun Joke"
            anotherone = input(f'Do you want another {userchoice} or {otherchoice}?')
            if anotherone.lower() == "dad joke" or anotherone.lower() == "pun joke":
                again = True
            cont = False
        elif userchoice.lower() == "pun joke":
            print(getjoke(2))
            otherchoice = "Dad Joke"
            anotherone = input(f'Do you want another {userchoice} or {otherchoice}?')
            if anotherone.lower() == "dad joke" or anotherone.lower() == "pun joke":
                again = True
            cont = False
        else:
            print(f'{userchoice} is not an option. Please type in Dad joke or pun joke')


    while again:
        if anotherone.lower() == "dad joke":
            print(getjoke(1))
            otherchoice = "Pun Joke"
            anotherone = input(f'Do you want another {userchoice} or {otherchoice}?')
            if anotherone.lower() == "dad joke" or anotherone.lower() == "pun joke":
                again = True
            else:
                again = False
        elif anotherone.lower() == "pun joke":
            print(getjoke(2))
            otherchoice = "Dad Joke"
            anotherone = input(f'Do you want another {userchoice} or {otherchoice}?')
            if anotherone.lower() == "dad joke" or anotherone.lower() == "pun joke":
                again = True
            else:
                again = False


if __name__ == '__main__':
    driver()