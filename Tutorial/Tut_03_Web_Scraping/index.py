"""
#) Web Scraping:
    -> the website that client get when client will ask using the end point or the url which is html css and javascript and show that file using the web browser but now in this case we will get those file using the python , we will get the html file from the server to the python it is called as the web Scraping

*) Step:
    0) Setting up the environment
        -> in order to use the power of python to scrap websites, we dont' have to reinvent the wheel
        -> We can use pxisting libraris to get the job done!
        -> install :
            -> pip install requests
                -> this will help to get any website content request and get that into the project
            -> pip install html5lib
            -> pip install bs4
                -> to parse the html
    1) Get the HTML 
        -> in order to work with the HTML, we will have to get the HTML  as a string.
        -> We will leverage the power of python request module to get this done!
        -> The next step then will be the parse the HTML content and give it a tree like structure so that it can be traversed!
    2) Parse the HTML 
        -> One the HTML is fetched using request as an string, we need to parse it.
        -> for parsing, we will use python's 'BeautifuSoup' module which will create a tree like structure for our DOM.
    3) HTML tree traversal
        -> Once the HTML is fetched and parsed, the next step is to manipulate the tree using BeautifulSoup's function to get our job done.
        -> we will going to learn how to get started and traverse the tree
        -> after that you will be able to scrape any website and its contents into you dsired format
"""

"""

-> If you want to scrape a websites:
    -> Use the API
        -> if some services provide the api feture that we will consider to use api feature to get the data from that website
    -> HTML web scraping using some tool like bs4

"""


# url = 'https://www.codewithharry.com'
import requests
from bs4 import BeautifulSoup
url = 'https://www.w3schools.com/html/'

# Step 1: Get the HTML

r = requests.get(url)
# 'request' will help us to use get or post request
htmlcontent = r.content
# print(htmlcontent)

# Step 2: Get Parse the HTML
soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify)
# this will prettify or make it html beautiful in structure to look


# Step 3: HTML Tree traversal
title = soup.title
# this will return the tilte tag

# print(title)
# the type of the 'title' is 'bs4.element.Tag' object which is implemented by 'bs'
# 'bs' give us a lot of attribute of this object

# print(title.string)

# Commonly used types of objects:
#   1. Tag
#       print(type(title))
#   2. NavigableString
#       print(type(title.string))
#   3. BeautifulSoup
#       print(type(soup))
#   2. Comment:
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
# print(soup2.p.string)
# print(type(soup2.p.string))

# Get all the pragraphs from the page
paras = soup.find_all('p')
# print(paras)

# Get all the anchor tags from the page
anchors = soup.find_all('a')
# print(anchors)

all_links = set()
# Get all the links on the page:
for link in anchors:
    all_links.add(link.get('href'))

# print(all_links)

# to get the first anchor tag
firstPara = soup.find('a')
# to get the class of the element
firstParaClass = firstPara['class']
# print(firstParaClass)

# Find all the elements with class lead
classLeadElm = soup.find_all('a', class_="w3-button")
# print(classLeadElm)

# Get text from the tags/soup
textTag = soup.find('p').get_text()

# to get all the text from the html
getAllText = soup.get_text()
# print(getAllText)


idTag = soup.find(id="loginactioncontainer")
# it will get the tag which have id of 'loginactioncontainer'
# print(idContent)
idTagChildren = idTag.children
# to get the children of the tag

idTagContent = idTag.contents
# to get the element of the 'idTag'

for elem in idTagContent:
    # print(elem)
    pass

# '.content' = A tag's children are available as a list
#       -> content will save in memory so not for big pages
# '.children' = A tag's children are available as a generator we can itrate that

# for item in idTag.string:
#     # it will get all the string
#     # print(item)
#     pass

for item in idTag.stripped_strings:
    # it will get all the string and stripped all the string
    # print(item)
    pass

parentTag = idTag.parent
# This will return parent element
# print(parentTag)
parentsTag = idTag.parents
# this will return the generator of all the parent element of that tag when we can itrate
# print(parentsTag)

for item in parentsTag:
    # print(item)
    # print(item.name)
    pass


nextSiblingTag = idTag.next_sibling.next_sibling
previousSiblingTag = idTag.previous_sibling.previous_sibling
# to get next and previous sibling
# NOTE: it will considered spaces or blank line also a sibling
# print(previousSiblingTag)

#
classElem = soup.select(".w3-third ")
# we can be able to get the element using css selector as well
# print(classElem)

# we can also be able to write using 'Beautiful Soup' for that read documentation
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
