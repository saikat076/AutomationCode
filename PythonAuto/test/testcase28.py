from behave import *
from action import *

@Given('I open the browser')
def I_open_the_browser(url):
    open_url(url)

@When('I validate the popular RT')
def I_validate_the_popular_RT():
    validate_popular_RT()

try:
    I_open_the_browser("https://stage.web.khulke.com/roundtable/all")
    I_validate_the_popular_RT()
except Exception as e:
    print(e)

close_browser()