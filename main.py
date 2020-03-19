# Write a script in any language you like,  which does the following:
# Query “Rick and Morty” API and look for all! characters that meets the following conditions:
# Species is “Human”
# Status is “Alive”
# Origin is “Earth”
# Make a list of the results that will include:
# Name.
# Location.
# Image link.
# Write the results to a csv file.

import json
import requests
import csv


ricky_morty_url = 'https://rickandmortyapi.com/api/'
headers = {"Content-Type": "application/json"}

def getCharctersWithParams(species='',status='',page=1):
    urlAdd = "character/?page={}&species={}&status={}".format(page,species,status)
    return requests.get(ricky_morty_url + urlAdd, headers=headers).json()

def main():
    # Get environment variables
    global ricky_morty_url
    page=1 #init
    n_pages=10 #init
    with open('results.csv', 'w', newline='') as file:
        fieldnames = ['Name', 'Location','Image']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        while True:  
            ricky_morty_url = 'https://rickandmortyapi.com/api/'
            try:
                ret = getCharctersWithParams('human','alive',page)
            except:
                print("An exception occurred")
                break
            
            n_pages = ret['info']['pages']
            for char in ret['results']:
                if('Earth' == char['origin']['name']): #I choose contains not equal
                    writer.writerow({'Name': char['name'], 'Location': char['location']['name'],'Image' :char['image'] })
            page=page+1
            if(page > n_pages):
                    break
              
if __name__ == "__main__":
    main()
