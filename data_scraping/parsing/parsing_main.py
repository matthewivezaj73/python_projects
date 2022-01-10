#importing libraries.
import urllib.request as req
# from bs4 import BeautifulSoup
#Creating a variable and assigning it a web page.
# html = 'https://accounts.google.com/ServiceLogin/signinchooser?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin#inbox'
#Adding a flag.
not_done = False
#Testing for a reponse from the user.
while not not_done:
    my_link = input("Please enter a link whose page you would like to scrape in proper form (i.e. http, https, www., .com, .net): ")
    # print(bs.h1)
    response = req.urlopen(html)
#Printing the response returned.
# print(type(response))

print(response.read())