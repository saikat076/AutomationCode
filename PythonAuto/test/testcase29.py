from behave import *
from action import *

@Given('I open the browser')
def I_open_the_browser(url):
    open_url(url)

@When('I validate the popular RT')
def I_validate_the_popular_RT():
    validate_popular_RT()

@Then("I validate roundtable")
def I_validate_roundtable():
    validate_roundtable()

@Then('I validate townhall')
def I_validate_townhall():
    validate_townhall_new()


try:
    I_open_the_browser("https://stage.web.khulke.com/roundtable/all")
    I_validate_the_popular_RT()
    I_validate_roundtable()
    I_validate_townhall()
except Exception as e:
    print(e)

close_browser()