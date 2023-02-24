from behave import *
from action import *

@Given("I go to townhall news")
def I_go_to_townhall_news():
    go_to_townhall()

@When("I validate townhall news")
def I_validate_townhall_news():
    validate_townhall()

try:
    open_url("https://stage.web.khulke.com/roundtable/all")
    click_on_log_in_button()
    enter_email_for_login('saikatbhattacharyya631@gmail.com')
    enter_password_for_login('Saikat123@')
    click_on_login()
    I_go_to_townhall_news()
    I_validate_townhall_news()
except Exception as e:
    print(e)
    print('Townhall validation failed')

close_browser()