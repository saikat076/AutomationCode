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

@Then("I go to profile RT and validate snip it")
def I_go_to_profile_RT_and_validate_snip_it():
    go_to_profile_RT_and_validate()

try:
    I_open_the_browser("https://stage.web.khulke.com/roundtable/all")
    I_log_in_with_email('saikatbhattacharyya631@gmail.com', 'Saikat123@')
    I_validate_login_functionality()
    I_go_to_profile_RT_and_validate_snip_it()
except Exception as e:
    print(e)
    print('Validation failed')

close_browser()