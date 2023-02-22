from behave import *
from action import *
from testcase2 import *

@When('I go to townhall news')
def I_go_to_townhall_news():
    go_to_townhall()

@Then('I validate townhall news')
def I_validate_townhall_news():
    validate_townhall()

try:
    I_open_the_browser("https://stage.web.khulke.com/roundtable/all")
    I_log_in_with_email('saikatbhattacharyya631@gmail.com', 'Saikat123@')
    I_validate_login_functionality()
except:
    print('Townhall validation failed')

close_browser()