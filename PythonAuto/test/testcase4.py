from behave import *
from action import *

try:
    open_url("https://stage.web.khulke.com/roundtable/all")
    click_on_log_in_button()
    enter_email_for_login('saikatbhattacharyya631@gmail.com')
    enter_password_for_login('Saikat123@')
    click_on_login()
except Exception as e:
    print(e)
    
close_browser()