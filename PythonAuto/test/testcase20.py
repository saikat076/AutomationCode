from behave import *
from action import *

@Given('I open the browser')
def I_open_the_browser(url):
    open_url(url)

@When('I log in with email')
def I_log_in_with_email(email, password):
    click_on_log_in_button()
    enter_email_for_login(email)
    enter_password_for_login(password)
    click_on_login()

@Then('I validate login functionality')
def I_validate_login_functionality():
    validate_post_login()

@When("I go to townhall news")
def I_go_to_townhall_news():
    go_to_townhall()

@Then("I validate post of following")
def I_validate_post_of_following():
    validate_post_of_following()
    
try:
    I_open_the_browser("https://stage.web.khulke.com/roundtable/all")
    I_log_in_with_email('neets', 'khulkeOO7@')
    I_validate_login_functionality()
    I_go_to_townhall_news()
    I_validate_post_of_following()

except Exception as e:
    print(e)

close_browser()