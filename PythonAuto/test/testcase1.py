from behave import *
from action import *

@Given('I open the browser')
def I_open_the_browser(url):
    open_url(url)

@When('I complete registraion')
def I_complete_registraion(email):
    click_on_log_in_button()
    click_on_create_an_account()
    enter_email(email)
    click_on_get_otp()
    enter_otp(input('Enter OTP'))
    click_on_sign_up()

@Then('I close the browser')
def I_close_the_browser():
    close_browser()

try:
    I_open_the_browser("https://stage.web.khulke.com/roundtable/all")
    I_complete_registraion('bbijoy854@gmail.com')
except:
    print('Sign up failed')

I_close_the_browser()
