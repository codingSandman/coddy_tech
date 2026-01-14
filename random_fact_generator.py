"""A simple script to fetch and display random useless facts from the uselessfacts-API.
You can choose a number between 1 and 7 to specify how many facts to retrieve in one execution.
The code is based on an online course by Coddy.tech."""

import requests 
import json
from time import sleep, time

def get_fact():
    response = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random')
    content = response.text
    data = json.loads(content)
    fact = data['text']
    return fact 

if __name__ == "__main__":
    entry = int(input("Enter number of facts to retrieve (1-7): "))
    if entry < 1:
        print("Minimum number of facts per execution is 1")    
    elif entry > 7:
        print("Maximum number of facts per execution is 7")
    else:
        for _ in range(entry):
            print(get_fact())
            
