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

@Then('I click on roundtable')
def I_click_on_round_table():
    click_on_round_table()

@When('I click on mine')
def I_click_on_mine():
    click_on_mine()

@Then('I validate mine')
def I_validate_mine():
    validate_mine()

try:
    I_open_the_browser("https://stage.web.khulke.com/roundtable/all")
    I_log_in_with_email('saikatbhattacharyya631@gmail.com', 'Saikat123@')
    I_validate_login_functionality()
    I_click_on_round_table()
    I_click_on_mine()
    I_validate_mine()
    
except Exception as e:
    print(e)
    print('Validation failed')

close_browser()