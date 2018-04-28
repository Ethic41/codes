from bs4 import BeautifulSoup as bs
html_doc = """
<html><head><title>The Dormouse's story</title></head> <body> <p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#TAG

soup = bs('<b class="boldest">Extremelybold</b>', "html.parser")
tag = soup.b
print(tag, type(tag))
print(tag.name)
tag.name = "blockqoute"
print(tag)
print(tag['class'])
print(tag.attrs)

css_soup = bs('<p class="body strikeout"></p>', "html.parser")
print(css_soup.p['class'])

css_soup = bs('<p class="body"></p>', 'html.parser')
print(css_soup.p['class'])

rel_soup = bs('<p>Back to the<a rel="index">homepage</a></p>', "html.parser")
print(rel_soup.a["rel"])

soup = bs('<b class="boldest">Extremely bold</b>', "html.parser")
tag = soup.b
print(tag.string)

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = bs(markup, 'html.parser')
comment = soup.b.string
print(comment, type(comment))

#NAVIGATION
soup = bs(html_doc, "html.parser")
print(soup.head)
print(soup.title)

print(soup.body.b)
print(soup.a)
print(soup.find_all("a"))
head_tag = soup.head
print(head_tag)
print(head_tag.contents)
title_tag = head_tag.contents
print(len(soup.contents))
print(soup.contents[1].name)
for i in title_tag:
    print i
for child in head_tag.descendants:
    print(child)
print(len(list(head_tag.children)))
print(len(list(head_tag.descendants)))
for string in soup.strings:
    print(string)
for string in soup.stripped_strings:
    print(string)
title_tag = soup.title
print(title_tag)
#GOING DOWN
print(title_tag.parent)
link = soup.a
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
sibling_soup = bs("<a><b>text1</b><c>text2</c></b></a>", "html.parser")
print(sibling_soup.b.next_sibling)
print(sibling_soup.c.previous_sibling)
print(soup.a.next_sibling)
for sibling in soup.a.next_siblings:
    print(sibling)
#GOING BACK AND FORTH
link = soup.a
print(link.previous_element)
for element in soup.a.next_elements:
    print(element)
#SEARCHING THE TREE
print(soup.find_all("p"))
print(soup.find_all(["p", "b", "a"]))
for tag in soup.find_all(True):
    print(tag.name)
print(soup.find_all("title"))
print(soup.find_all(id="link1"))
print(soup.find_all(id=True))
#SEARCHING BY CSS CLASS
print(soup.find_all("a", attrs={"class":"sister"}))
#SEARCHING SIDEWAYS
a_string = soup.find(string="Lacie")
print(a_string)
print(a_string.find_parents())
print(soup.a.find_all_next("a"))
