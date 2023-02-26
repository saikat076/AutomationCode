from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

driver_path = ChromeDriverManager().install()
#saikat_chrome_driver_path = 'PythonAuto/test/chromedriver_mac/chromedriver'
#suvranil_chrome_driver_path = 'PythonAuto/test/chromedriver_win/chromedriver.exe'
#driver = webdriver.Chrome(executable_path=suvranil_chrome_driver_path)
ser = Service(driver_path)
op =  webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

wait = WebDriverWait(driver, 60)

## Popultaing xpaths ##
login_button = "//button[text()='Login']"
login_header = "//p[text()='Login']"
create_an_acoount = "//span[contains(text(), 'Create an Account')]"
sign_up_header = "//p[text()='Sign Up']"
email = "//*[@type='email']"
get_otp = "//*[text()='GET OTP']"
enter_otp_header = "//p[text()='Enter OTP']"
first_digit = "//*[@id='first']"
second_digit = "//*[@id='second']"
third_digit = "//*[@id='third']"
fourth_digit = "//*[@id='fourth']"
sign_up_button = "//button[text()='SIGN UP']"
login_email = "//*[@id='fname']"
password_radio_button = "//*[text()='Password']"
continue_button = "//*[@id='root']/div[1]/div[2]/div/form/button"
enter_password_header = "//p[text()='Enter Password']"
login_password = "//*[@placeholder='Your password here']"
login_button = "//*[text()='Login']"
news = "//*[text()='News']"
timeline = "//*[@id='home_center']/div[1]/div[2]/div[2]"
popular_news = "//*[text()='Popular Shows']"
snip_it = "//*[text()='Snip-It']"
townhall_header = "//p[text()='TownHall']"
townhall_news = "//div[@id='townhall_post_body']"
no_of_likes = "(//*[@id='post_footer_container']/div[3]/p)[1]"
like_btn = "(//div[contains(@class, 'sc')]/button)[4]"
dislike_btn = "(//div[contains(@class, 'sc')]/button)[5]"
allow = "//button[text()='Allow']"
comment = "(//div[contains(@class, 'sc')]/button)[7]"
comment_box = "//textarea[contains(@placeholder, 'Write what you feel about this...')]"
post_comment = "//*[text()='Post']"
quote_or_circulate = "//*[@id='post_footer_container']/div[2]/button"
quote = "//*[text()='Quote']"
circulate = "//*[text()='Circulate']"
uncirculate = "//*[text()='Uncirculate']"
first_post = "(//p[contains(@class, 'sc-gswNZR')]/div/a)[1]"
following_button = "//button[@class='following-button-small']"
mute_button = "//button[@class='mute-btn']/i/svg[@class='MuiSvgIcon-root']"
snip_it_like = "(//img[@alt='like'])[1]"
snip_it_dislike = "(//img[@alt='dislike'])[1]"
snip_it_comment = "(//img[@alt='comment'])[1]"
snip_it_share = "(//img[@alt='share'])[1]"
snip_it_add = "//button[contains(@class, 'addBtn')]"
snip_it_post_comment = "//textarea[@placeholder='Write something...']"
snip_it_post = "//button[text()='Post']"
snip_it_video = "//div[@class='d-flex']"
roundtable = "//a[text()='RoundTable']"
all = "//button[text()='All']"
video1 = "(//div[@id='rt_img'])[1]"
recorded = "//h5[text()='recorded']"
viewers_count = "//p[@class='viewers_count']"
details_header = "//p[text()='RoundTable Details']"
live = "//button[text()='Live']"
upcoming = "//button[text()='Upcoming']"
cover_img = "//div[@class='rt_img_div']"
mine = "//button[text()='Mine']"
new_RT = "//div[@class='newStep']"
RT_video = "(//button[@class='torbtn'])[1]"
RT_audio = "(//button[@class='torbtn'])[2]"
recorded_audio_video = "(//button[@class='torbtn'])[3]"
add_video_title = "//*[@placeholder='Add Title']"
add_video_description = "//textarea[@placeholder='Add Description']"
RT_continue = "//div/button[text()='CONTINUE']"
RT_moderator = "(//div[@class=' css-hlgwow'])[1]/div[2]/*"
RT_moderator_option = "//div[@id='react-select-2-listbox']/*"
moderator_intro = "(//*[@placeholder='Introduction'])[1]"
panelist_intro = "(//*[@placeholder='Introduction'])[2]"
panelist = "(//*[text()='Search and add'])[2]"
add_panelist_btn = "//button[contains(@class, 'addpanelistbtn')]"
upload_image = "(//*[text()='Upload Image'])[2]"
upload_logo = "(//*[text()='Upload Logo'])"
upload_intro = "(//*[text()='Upload Intro Video'])[2]"
upload_outro = "(//*[text()='Upload Outro Video'])[2]"
upload_doc = "(//*[text()='Upload Document'])[1]"
categories = "(//*[@placeholder='Search and add'])[1]"
tags = "(//*[@placeholder='Search and add'])[2]"
categories_add = "(//button[text()='Add'])[1]"
tags_add = "(//button[text()='Add'])[2]"


## populating action methods here ##

## method 1 - opening URL ##
def open_url(url):
    driver.get(url)
    driver.maximize_window()
    wait.until(ec.visibility_of(driver.find_element(By.XPATH, login_button)))
    
## method 2 - clicking on log in button ##
def click_on_log_in_button():
   driver.find_element(By.XPATH, login_button).click()
   driver.implicitly_wait(10)
   wait.until(ec.visibility_of(driver.find_element(By.XPATH, login_header)))

## method 3 - clicking on create an account ##
def click_on_create_an_account():
    driver.find_element(By.XPATH, create_an_acoount).click()
    wait.until(ec.visibility_of(driver.find_element(By.XPATH, sign_up_header)))

## method 4 - entering email ##
def enter_email(emailid):
    driver.find_element(By.XPATH, email).click()
    driver.find_element(By.XPATH, email).send_keys(emailid)

## method 5 - click on get otp ##
def click_on_get_otp():
    driver.find_element(By.XPATH, get_otp).click()

## method 6 - enter OTP ##
def enter_otp(otp):
    wait.until(ec.visibility_of(driver.find_element(By.XPATH, enter_otp_header)))
    
    driver.find_element(By.XPATH, first_digit).send_keys(otp[0])
    driver.find_element(By.XPATH, second_digit).send_keys(otp[1])
    driver.find_element(By.XPATH, third_digit).send_keys(otp[2])
    driver.find_element(By.XPATH, fourth_digit).send_keys(otp[3])

## method 7 - clicking on sign up ##
def click_on_sign_up():
    driver.find_element(By.XPATH, sign_up_button).click()
    driver.implicitly_wait(100)

## method 8 - entering email id ##
def enter_email_for_login(emailid):
    driver.find_element(By.XPATH, login_email).send_keys(emailid)
    driver.find_element(By.XPATH, password_radio_button).click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, continue_button).click()
    driver.implicitly_wait(5)

    try:
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, continue_button).click()
    except:
        print("")

## method 9 - entering password ##
def enter_password_for_login(password):
    driver.implicitly_wait(5)
    wait.until(ec.visibility_of(driver.find_element(By.XPATH, enter_password_header)))
    driver.find_element(By.XPATH, login_password).send_keys(password)

## method 10 -  clicking on log in button ##
def click_on_login():
    wait.until(ec.visibility_of(driver.find_element(By.XPATH, login_button)))
    driver.find_element(By.XPATH, login_button).click()
    
    try:
       driver.implicitly_wait(5)
       driver.find_element(By.XPATH, login_button).click()
    except:
        print("")

## method 11 - validating post log in options
def validate_post_login():
    driver.implicitly_wait(30)

    try:
        driver.find_element(By.XPATH, allow).click()
    except:
        print("")

    if driver.current_url == "https://stage.web.khulke.com/home":
        print('URL valudation passed')
    else: 
        raise Exception

    if not driver.find_element(By.XPATH, news).is_displayed():
        raise Exception
    else:
        print('News is displayed')

    if not driver.find_element(By.XPATH, timeline).is_displayed():
        raise Exception
    else:
        print('Timeline is displayed')


    if not driver.find_element(By.XPATH, popular_news).is_displayed():
        raise Exception
    else:
        print('Popular news is displayed')  

    if not driver.find_element(By.XPATH, snip_it).is_displayed():
        raise Exception
    else:
        print('Snip it is displayed') 

def go_to_townhall():

    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, timeline).click()  

    wait.until(ec.visibility_of(driver.find_element(By.XPATH, townhall_header)))

    if not driver.find_element(By.XPATH, townhall_header).is_displayed():
        print('Townhall not displayed')
        raise Exception
    else:
        print('Townhall is displayed')

def validate_townhall():
    wait.until(ec.visibility_of(driver.find_element(By.XPATH, "//*[contains(text(), 'Write something')]")))
    driver.implicitly_wait(20)

    list = driver.find_elements(By.XPATH, townhall_news)
    
    if(len(list)>0 and list[0].is_displayed()):
        print('Townhall news validated')
    else:
        print('Townhall news validation failed')
        raise Exception

def validate_likes():
    num_of_likes1 = int(driver.find_element(By.XPATH, no_of_likes).text)
    time.sleep(5)
    driver.find_element(By.XPATH, like_btn).click()
    time.sleep(5)
    num_of_likes2 = int(driver.find_element(By.XPATH, no_of_likes).text)

    if(num_of_likes2-num_of_likes1 == 1):
        print('Like validation successful')
    else:
        print('Like validation failed', num_of_likes1, ' ', num_of_likes2)
        raise Exception
    
    driver.find_element(By.XPATH, like_btn).click()
    time.sleep(5)

def validate_dislike():
    driver.find_element(By.XPATH, dislike_btn).click()
    time.sleep(2)
    driver.find_element(By.XPATH, dislike_btn).click()
    time.sleep(2)

def validate_comment():
    driver.find_element(By.XPATH, comment).click()
    time.sleep(5)
    driver.find_element(By.XPATH, comment_box).send_keys('Test comment')
    driver.find_element(By.XPATH, post_comment).click()
    time.sleep(5)

def validate_circulate_and_quote():
    driver.find_element(By.XPATH, quote_or_circulate).click()
    time.sleep(2)
    driver.find_element(By.XPATH, circulate).click()
    time.sleep(2)
    print('Circulate is validated')

    driver.refresh()
    time.sleep(5)
    driver.find_element(By.XPATH, timeline).click() 

    driver.find_element(By.XPATH, quote_or_circulate).click()
    time.sleep(2)
    driver.find_element(By.XPATH, uncirculate).click()
    time.sleep(2)
    print('Uncirculate is Validated')

    driver.find_element(By.XPATH, quote_or_circulate).click()
    time.sleep(2)
    driver.find_element(By.XPATH, quote).click()
    time.sleep(2)
    print('Quote is validate')

def validate_timeline_post():
    driver.find_element(By.XPATH, first_post).click()
    time.sleep(10)
    if(driver.find_element(By.XPATH, following_button).is_displayed() and driver.find_element(By.XPATH, following_button).text == 'Following'):
        print('Timeline is showing post from the persons I follow')
    else:
        print('Validation of timeline post - failed')
        raise Exception

    driver.back()
    time.sleep(5)
    driver.find_element(By.XPATH, timeline).click()

    if(driver.find_element(By.XPATH, like_btn).is_displayed and driver.find_element(By.XPATH, dislike_btn).is_displayed() and driver.find_element(By.XPATH, comment).is_displayed() and driver.find_element(By.XPATH, quote_or_circulate).is_displayed()):
        print('like, dislike, comment, circulate or quote is validated')
    else:
        print('Validation failed for like, dislike, comment, circulate or quote')
        raise Exception

def validate_snip_it():

    driver.find_element(By.XPATH, snip_it).click()

    if(driver.current_url == 'https://stage.web.khulke.com/snip-it'):
        print('Redirected to snip it - ', driver.current_url)
    else:
        print('Not redirected to snip it')
        raise Exception

    videos = driver.find_elements(By.XPATH, '//video')
    if(len(videos) > 1):
        print('All snip-its available')
    else:
        print('Snip its are not available')
        raise Exception

    #hover = ActionChains(driver).move_to_element(driver.find_element(By.XPATH, mute_button))
    #hover.perform()

    #driver.find_element(By.XPATH, mute_button).click()
    #print('Mute button clicked')

    time.sleep(5)

    if(driver.find_element(By.XPATH, snip_it_like).is_displayed() and driver.find_element(By.XPATH, snip_it_dislike).is_displayed() and driver.find_element(By.XPATH, snip_it_comment).is_displayed() and driver.find_element(By.XPATH, snip_it_share).is_displayed()):
        print('Snip it like, dislike, comment and share displayed')
    else:
        print('Snip it like, dislike, comment, share is not displayed')
        raise Exception

def click_on_add_and_validate():
    driver.find_element(By.XPATH, snip_it_add).click()
    time.sleep(2)
    driver.find_element(By.XPATH, snip_it_post_comment).send_keys('Test Post')
    if(driver.find_element(By.XPATH, snip_it_video).is_displayed()):
        print('Post validated!')
        driver.find_element(By.XPATH, snip_it_post).click()
    else:
        print('Post validation failed!')

def click_on_round_table():
    driver.find_element(By.XPATH, roundtable).click()

def click_on_all():
    driver.find_element(By.XPATH, all).click()

def validate_RT():
    driver.find_element(By.XPATH, video1).click()
    time.sleep(3)
    
    if(driver.find_element(By.XPATH, recorded).is_displayed()):
        print('RT validation passed')
    else:
        print('RT validation failed')
        raise Exception
    
    driver.back()
    driver.find_element(By.XPATH, viewers_count).click()

    if(driver.find_element(By.XPATH, details_header).is_displayed()):
        print('RT details displayed')
    else:
        print('RT details validation failed')
        raise Exception

def click_on_live():
    driver.find_element(By.XPATH, live).click()

def validate_live():
    if(driver.current_url == 'https://stage.web.khulke.com/roundtable/live'):
        print('Live page reirection validated')
    else:
        print('Live page redirection validation failed')
        raise Exception

def click_on_upcoming():
    driver.find_element(By.XPATH, upcoming).click()

def validate_upcoming():
    if(driver.current_url == "https://stage.web.khulke.com/roundtable/upcoming"):
        print('Upcoming URL validated')
    else:
        print('Upcoming URL validation failed')
        raise Exception

    time.sleep(2)
    driver.find_element(By.XPATH, cover_img).click()
    time.sleep(2)

    try:
        driver.find_element(By.XPATH, "//*[contains(text(), 'YES')]").click()
    except:
        print("")

    time.sleep(2)

    driver.find_element(By.XPATH, viewers_count).click()
    time.sleep(1)
    if(driver.find_element(By.XPATH, details_header).is_displayed()):
        print('Upcoming roundtable validated')
    else:
        print('Upcoming roundtable validation failed')
        raise Exception

def click_on_mine():
    driver.find_element(By.XPATH, mine).click()

def validate_mine():
    if(driver.current_url == 'https://stage.web.khulke.com/roundtable/mine'):
        print('Mine URL validated')
    else:
        print('Mine URL validation failed')
        raise Exception

def click_on_new():
    driver.find_element(By.XPATH, new_RT).click()

def click_and_validate_RT_videos():

    time.sleep(5)

    driver.find_element(By.XPATH, RT_video).click()
    driver.find_element(By.XPATH, add_video_title).send_keys('Test title')
    driver.find_element(By.XPATH, add_video_description).send_keys('Test Description')
    
    time.sleep(5)
    try:
        driver.find_element(By.XPATH, RT_continue).click()
    except:
        driver.find_element(By.XPATH, RT_continue).click()

    time.sleep(5)

    print('Added video details')

    time.sleep(5)

    driver.find_element(By.XPATH, RT_moderator).click()
    driver.find_element(By.XPATH, RT_moderator).send_keys('test1234')
    time.sleep(5)
    driver.find_element(By.XPATH, RT_moderator_option).click()
    driver.find_element(By.XPATH, moderator_intro).send_keys('Test mderator introduction')

    time.sleep(5)

    driver.find_element(By.XPATH, panelist).send_keys('testkhulke103')
    time.sleep(5)
    driver.find_element(By.XPATH, panelist).send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, panelist_intro).send_keys('Test panelist introduction')
    driver.find_element(By.XPATH, add_panelist_btn).click()
    driver.find_element(By.XPATH, RT_continue).click()


## method - close browser ##
def close_browser():
    driver.implicitly_wait(10)
    driver.close()
    driver.quit()
