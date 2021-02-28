
# step 0:: install  all req.
import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com"
# step 1: get html 

r = requests.get(url)
html_content = r.content
# print(html_content)




# step 2: parse the html
soup = BeautifulSoup(html_content,'html.parser')
print(soup.prettify)





# step 3: tree transevrse the html
# objects ::
# 1.tag ,print(type(title))
# 2.navigable string ,print(type(title.string))
# 3.BeautifulSoup , print(type(soup))
# 4.comment





# title of html page
title = soup.title


# all paragraphs in page
# paras = soup.find_all('p')
# print(paras)

# all anchor tags in page
anchors = soup.find_all('a')
# print(anchors)




# 1st paragraph 
# print(soup.find('p'))




# class of paragraph:
# print(soup.find('p')['class'])

#  getting id of a class:
# print(soup.find('p')['id']) 


# all classes with class =lead
print(soup.find_all("p",class_="lead"))


# all text in a  1st paragraph:
print(soup.find("p").get_text())


# all text in a page
# print(soup.get_text())

 


 # all anchor tags in page

anchors = soup.find_all('a')
all_links = set() 
# print(anchors)
for link in anchors:
    if(link.get('href') !='#'):
        link_text = "https://www.codewithharry.com" +link.get('href')
        all_links.add(link_text)
        # print(link_text)



# comment
# x = "<p><!--klkjhk></p>"
# soup = BeautifulSoup(x)
# print(type(soup.p.string))




