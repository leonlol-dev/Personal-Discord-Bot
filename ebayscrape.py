from bs4 import BeautifulSoup
from enum import Enum
from re import sub
from decimal import Decimal
import requests

# If you want to install packages the command is: "py -m pip install (package)"
# example link: https://www.ebay.co.uk/sch/i.html?_nkw=asd+asd&_sacat=0&LH_Complete=1&LH_Sold=1

def ebayGetImage(soup):
    listing = soup.find('div', class_=('s-item__image-wrapper image-treatment'))
    

def ebayAverage(userSearch, conditionChoice):
    
    #SEARCHING FOR ITEM
    userSearch = userSearch.replace(" ", "+")

    print(userSearch)

    print("\nChoose a condition: \n" +
          "1 - Used \n" +
          "2 - New \n" +
          "3 - Parts Only \n")
    

    link = "www.ebay.co.uk"

    if(conditionChoice == "used"):
        print("YOU CHOSE USED.")
        link = "https://www.ebay.co.uk/sch/i.html?_nkw=" + userSearch + "&_sacat=0&LH_Complete=1&LH_Sold=1"  + "&LH_ItemCondition=3000"
        htmlText = requests.get("https://www.ebay.co.uk/sch/i.html?_nkw=" + userSearch + "&_sacat=0&LH_Complete=1&LH_Sold=1"  + "&LH_ItemCondition=3000")
    elif(conditionChoice == "new"):
        print("YOU CHOSE NEW.")
        link = "https://www.ebay.co.uk/sch/i.html?_nkw=" + userSearch + "&_sacat=0&LH_Complete=1&LH_Sold=1"  + "&LH_ItemCondition=1000"
        htmlText = requests.get("https://www.ebay.co.uk/sch/i.html?_nkw=" + userSearch + "&_sacat=0&LH_Complete=1&LH_Sold=1"  + "&LH_ItemCondition=1000")
    elif(conditionChoice == "parts"):
        print("YOU CHOSE PARTS.")
        link = "https://www.ebay.co.uk/sch/i.html?_nkw=" + userSearch + "&_sacat=0&LH_Complete=1&LH_Sold=1"  + "&LH_ItemCondition=7000"
        htmlText = requests.get("https://www.ebay.co.uk/sch/i.html?_nkw=" + userSearch + "&_sacat=0&LH_Complete=1&LH_Sold=1"  + "&LH_ItemCondition=7000")  
    else:
        print("YOU CHOSE NOTHING")
        link = "https://www.ebay.co.uk/sch/i.html?_nkw=" + userSearch + "&_sacat=0&LH_Complete=1&LH_Sold=1"
        htmlText = requests.get("https://www.ebay.co.uk/sch/i.html?_nkw=" + userSearch + "&_sacat=0&LH_Complete=1&LH_Sold=1")


    soup = BeautifulSoup(htmlText.text, 'lxml')

    listings = soup.find_all('li', attrs={'class': 's-item'})

    totalAmount = 0
    HighestAmount = 0
    LowestAmount = 0


    for listing in listings[1:]:

        priceClass = listing.find('span', class_='s-item__price')


        #Sometimes there are eBay listings that show multiple quantities so there is a range of prices. 
        #Avoided this by checking if the string is longer than 9 characters 
        #(THIS NEEDS TO BE AFTER THE LISTING.FIND AND BEFORE EVERYTHING ELSE!!)
        if(len(priceClass.text)>9):
            continue

        #Changes currency to float
        money = float(Decimal(sub(r'[^\d.]', '', priceClass.text)))

        #if(listing.find('shipping'))

        #If its the first element in the array, set the money. Also gets the image from the first listing for the thumbnail.
        if(listings.index(listing) == 1):
            LowestAmount = money
            image = listing.find('div', class_="s-item__image").find("img")["src"]
            print(str(image))

        

        #Check for highest amount
        if(money > HighestAmount):
            HighestAmount = money

        #Check for lowest amount
        if(money < LowestAmount):
            LowestAmount = money

        print(priceClass.text)
        totalAmount += Decimal(sub(r'[^\d.]', '', priceClass.text))


    totalAmount = float(round((totalAmount/(len(listings)-1)), 2))
    
    print("Average Cost: " + '£{:,.2f}'.format(totalAmount))
    print("Highest Listing: " + '£{:,.2f}'.format(HighestAmount))
    print("Lowest Listing: " + '£{:,.2f}'.format(LowestAmount))
    print(link)

    returnList = ['£{:,.2f}'.format(totalAmount), '£{:,.2f}'.format(HighestAmount), '£{:,.2f}'.format(LowestAmount), link, image]
    return returnList 

