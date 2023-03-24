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
continue_button = "//*[@id='root']/div[1]/div/div[2]/div/form/button"
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
RT_moderator_option = "(//img[@class='avatar'])[8]"
panelist_option = "(//img[@class='avatar'])[8]"
moderator_intro = "(//*[@placeholder='Introduction'])[1]"
panelist_intro = "(//*[@placeholder='Introduction'])[2]"
panelist = "(//div[@class=' css-hlgwow'])[2]/div[2]/*"
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
recorded_audio_panelist = "(//div[@class='form-control-div '])[2]/*"
upload_recorded_roundtable = "(//*[text()='Upload Recorded RoundTable'])[1]"
search_a_user = "//div[@class=' css-19bb58m']/*"
email = "//*[@placeholder='Add Mobile or Email ID to invite']"
add_btn = "//button[text()='Add']"
proceed_btn = "//button[text()='PROCEED']"
my_rt = "//div[@class='d-flex']"
edit_rt = "(//*[text()='Edit'])[1]"
notification = "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1yxmbwk']"
accept_btn = "//button[text()='Accept']"
reject_btn = "//button[text()='Reject']"
notifications = "//*[text()='Notifications']"
network = "//*[text()='Network']"
first_noti = "//div[@class='user_suggestion_container']/div/div/div/div[2]/p"
profile = "//*[text()='Profile']"
snip_it_option = "//div[@class='MuiTabs-scroller MuiTabs-fixed css-1anid1y']/div/button[3]"
snip_it_img = "//div[@class='snipsDiv']/img"
menu = "(//button[@id='basic-button'])[1]"
save_btn = "//*[text()='Save']"
saved_option = "//div[@class='MuiTabs-scroller MuiTabs-fixed css-1anid1y']/div/button[4]"
unsave_btn = "//*[text()='Unsave']"
edit_profile = "//*[text()='Edit Profile']"
bio = "//div[@class='bioCount']/textarea"
full_name = "//*[@placeholder='Enter Full Name']"
dob = "//*[@placeholder='dd/mm/yyyy']"
gender = "//*[text()='Select...']"
location  = "//*[@placeholder='Enter Your Location']"
interest = "//*[@placeholder='Search and add']"
save_changes = "(//*[text()='SAVE CHANGES'])[1]"
save_changes_msg = "//*[text()='Your changes have been saved!']"
search = "//*[@placeholder='Search']"
search_options = "//div[@class='MuiTabs-flexContainer css-k008qs']/button"
following = "//*[@id='root']/div[1]/div[2]/section/div[1]/div[1]/div/div[1]/div/p"
follower = "//*[@id='root']/div[1]/div[2]/section/div[1]/div[1]/div/div[2]/div/p"
popular_shows = "//*[text()='Popular Shows']"
popular_RT = "//div[@class='rt_img_div']"
popular_RT_text = "//div[@class='card_text']"
townhall = "(//*[text()='TownHall'])[1]"
timeline_ = "//*[text()='Timeline']"
interaction = "//div[@id='townhall_post_container']/div/span[2]"
first_video = "(//div[@class='snippetVideo-wrapper']/video)[1]"
post_video = "//div[@class='d-flex']/label"
past_rt = "//div[@class='video_img']/img"
rt_playing = "//video[@class='video_player']"
live_cover_img = "//img[@class='rt_cover_img']"
invite_msg = "//p[@class='MuiTypography-root MuiTypography-body1 css-1amsfhl']"
yes_btn = "//button[text()='YES']"
card = "//p[@class='rt_tags']"
rt_details = "//*[text()='RoundTable Details']"
share_btn = "(//*[@id='share_button'])[1]"
post_it = "//*[text()='Post it']"
login_popup = "//p[@class='MuiTypography-root MuiTypography-body1 css-70xrfa']"

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

## method 12 - going to townhall
def go_to_townhall():

    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, timeline).click()  

    wait.until(ec.visibility_of(driver.find_element(By.XPATH, townhall_header)))

    if not driver.find_element(By.XPATH, townhall_header).is_displayed():
        print('Townhall not displayed')
        raise Exception
    else:
        print('Townhall is displayed')

## method 13 - validating townhall
def validate_townhall():
    wait.until(ec.visibility_of(driver.find_element(By.XPATH, "//*[contains(text(), 'Write something')]")))
    driver.implicitly_wait(20)

    list = driver.find_elements(By.XPATH, townhall_news)
    
    if(len(list)>0 and list[0].is_displayed()):
        print('Townhall news validated')
    else:
        print('Townhall news validation failed')
        raise Exception

## method 14 - validating likes
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

## method 15 - validating dislikes
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
    
    if(driver.find_element(By.XPATH, first_video).is_displayed()):
        print('Only first snip-it is displayed on page')
    else:
        print('Snip-it display validation failed')

    time.sleep(5)

    if(driver.find_element(By.XPATH, snip_it_like).is_displayed() and driver.find_element(By.XPATH, snip_it_dislike).is_displayed() and driver.find_element(By.XPATH, snip_it_comment).is_displayed() and driver.find_element(By.XPATH, snip_it_share).is_displayed()):
        print('Snip it like, dislike, comment and share displayed')
    else:
        print('Snip it like, dislike, comment, share is not displayed')
        raise Exception

def click_on_add_and_validate():
    driver.find_element(By.XPATH, snip_it_add).click()
    time.sleep(2)
    
    post_video_element = driver.find_element(By.XPATH, post_video)
    file_path = 'vid.mp4'
    post_video_element.send_keys(file_path)

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

    driver.back()
    time.sleep(3)
    
    if(driver.find_element(By.XPATH, past_rt).is_displayed()):

        time.sleep(10)
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
    
    driver.find_element(By.XPATH, live_cover_img).click()
    try:
        if(driver.find_element(By.XPATH, invite_msg).is_displayed()):
            print('User is uninvited, sending invitation')
            driver.find_element(By.XPATH, yes_btn).click()
    except:
        driver.find_element(By.XPATH, card).click()
        if(driver.find_element(By.XPATH, rt_details).is_displayed()):
            print('RT details validation succesful')
        else:
            print('RT details validation failed')
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

    if(driver.find_element(By.XPATH, upcoming).is_displayed() and driver.find_element(By.XPATH, live).is_displayed() and driver.find_element(By.XPATH, all).is_displayed()):
        print('All RT options are displayed')
    else:
        print('Options are not displayed')
        raise Exception
    
    driver.find_element(By.XPATH, card).click()
    if(driver.find_element(By.XPATH, rt_details).is_displayed()):
            print('RT details validation succesful')
    else:
        print('RT details validation failed')
        raise Exception

def click_on_new():
    driver.find_element(By.XPATH, new_RT).click()

def click_and_validate_RT_videos():

    time.sleep(5)

    try:
        driver.find_element(By.XPATH, RT_video).click()
    except:
        print('')
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
    
    
    driver.find_element(By.XPATH, moderator_intro).send_keys('Test moderator introduction')

    time.sleep(5)

    driver.find_element(By.XPATH, panelist).click()
    driver.find_element(By.XPATH, panelist).send_keys('testkhulke103')
    time.sleep(5)
    driver.find_element(By.XPATH, panelist_option).click()

    driver.find_element(By.XPATH, panelist_intro).send_keys('Test panelist introduction')

    time.sleep(5)

    try:
        driver.find_element(By.XPATH, add_panelist_btn).click()
    except:
        driver.find_element(By.XPATH, add_panelist_btn).click()

    time.sleep(5)

    try:
        driver.find_element(By.XPATH, RT_continue).click()
    except:
        driver.find_element(By.XPATH, RT_continue).click()

    time.sleep(3)

    status = True
    if(driver.find_element(By.XPATH, upload_image).is_displayed() and driver.find_element(By.XPATH, upload_intro).is_displayed() and driver.find_element(By.XPATH, upload_outro).is_displayed()):
        status = True
    else:
        status = False

    elements = driver.find_elements(By.XPATH, upload_logo)
    for i in elements:
        if(not i.is_displayed()):
            status = False;

    if(not status):
        print('RT video - Validation failed!')
   
    try:
        driver.find_element(By.XPATH, RT_continue).click()
    except:
        driver.find_element(By.XPATH, RT_continue).click()

    driver.find_element(By.XPATH, search_a_user).click()
    driver.find_element(By.XPATH, search_a_user).send_keys('iostester147')

    driver.find_element(By.XPATH, RT_moderator_option).click()
    driver.find_element(By.XPATH, email).send_keys('bbijoy854@gmail.com')
    driver.find_element(By.XPATH, add_btn).click()

    try:
        driver.find_element(By.XPATH, RT_continue).click()
    except:
        driver.find_element(By.XPATH, RT_continue).click()

    if(driver.find_element(By.XPATH, proceed_btn)):
        print('RT video validation successful')
    else:
        print('RT video validation failed')
        raise Exception

def click_and_validate_RT_audio():
    time.sleep(5)

    driver.find_element(By.XPATH, RT_audio).click()
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
    
    
    driver.find_element(By.XPATH, moderator_intro).send_keys('Test moderator introduction')

    time.sleep(5)

    driver.find_element(By.XPATH, panelist).click()
    driver.find_element(By.XPATH, panelist).send_keys('testkhulke103')
    time.sleep(5)
    driver.find_element(By.XPATH, panelist_option).click()

    driver.find_element(By.XPATH, panelist_intro).send_keys('Test panelist introduction')

    time.sleep(5)

    try:
        driver.find_element(By.XPATH, add_panelist_btn).click()
    except:
        driver.find_element(By.XPATH, add_panelist_btn).click()

    time.sleep(5)

    try:
        driver.find_element(By.XPATH, RT_continue).click()
    except:
        driver.find_element(By.XPATH, RT_continue).click()

    time.sleep(3)

    status = True
    if(driver.find_element(By.XPATH, upload_image).is_displayed() and driver.find_element(By.XPATH, upload_intro).is_displayed() and driver.find_element(By.XPATH, upload_outro).is_displayed()):
        status = True
    else:
        status = False

    elements = driver.find_elements(By.XPATH, upload_logo)
    for i in elements:
        if(not i.is_displayed()):
            status = False;

    if(not status):
        print('RT audio validation failed!')
        raise Exception
    
    time.sleep(5)

    try:
        driver.find_element(By.XPATH, RT_continue).click()
    except:
        driver.find_element(By.XPATH, RT_continue).click()

    driver.find_element(By.XPATH, search_a_user).click()
    driver.find_element(By.XPATH, search_a_user).send_keys('iostester147')

    driver.find_element(By.XPATH, RT_moderator_option).click()
    driver.find_element(By.XPATH, email).send_keys('bbijoy854@gmail.com')
    driver.find_element(By.XPATH, add_btn).click()

    try:
        driver.find_element(By.XPATH, RT_continue).click()
    except:
        driver.find_element(By.XPATH, RT_continue).click()

    if(driver.find_element(By.XPATH, proceed_btn)):
        print('RT audio validation successful')
    else:
        print('RT audio validation failed')
        raise Exception

def click_and_validate_recorded_audio():
    time.sleep(5)

    driver.find_element(By.XPATH, recorded_audio_video).click()
    driver.find_element(By.XPATH, add_video_title).send_keys('Test title')
    driver.find_element(By.XPATH, add_video_description).send_keys('Test Description')

    time.sleep(5)

    driver.find_element(By.XPATH, RT_moderator).click()
    driver.find_element(By.XPATH, RT_moderator).send_keys('test1234')
    time.sleep(5)
    driver.find_element(By.XPATH, RT_moderator_option).click()
    
    driver.find_element(By.XPATH, moderator_intro).send_keys('Test moderator introduction')

    time.sleep(5)

    try:
        driver.find_element(By.XPATH, recorded_audio_panelist).click()
    except:
        driver.find_element(By.XPATH, recorded_audio_panelist).click()

    driver.find_element(By.XPATH, recorded_audio_panelist).send_keys('testkhulke103')
    time.sleep(5)
    #driver.find_element(By.XPATH, panelist_option).click()

    driver.find_element(By.XPATH, panelist_intro).send_keys('Test panelist introduction')

    if(driver.find_element(By.XPATH, upload_image).is_displayed() and driver.find_element(By.XPATH, upload_recorded_roundtable).is_displayed()):
        print('Recorded audio validation successfull')
    else:
        print('Recorded Audio validation failed')
        raise Exception

    time.sleep(5)

def click_and_validate_recorded_video():
    time.sleep(5)

    driver.find_element(By.XPATH, recorded_audio_video).click()
    driver.find_element(By.XPATH, add_video_title).send_keys('Test title')
    driver.find_element(By.XPATH, add_video_description).send_keys('Test Description')

    time.sleep(5)

    driver.find_element(By.XPATH, RT_moderator).click()
    driver.find_element(By.XPATH, RT_moderator).send_keys('test1234')
    time.sleep(5)
    driver.find_element(By.XPATH, RT_moderator_option).click()
    
    
    driver.find_element(By.XPATH, moderator_intro).send_keys('Test moderator introduction')

    time.sleep(5)

    try:
        driver.find_element(By.XPATH, recorded_audio_panelist).click()
    except:
        driver.find_element(By.XPATH, recorded_audio_panelist).click()

    driver.find_element(By.XPATH, recorded_audio_panelist).send_keys('testkhulke103')
    time.sleep(5)
    #driver.find_element(By.XPATH, panelist_option).click()

    driver.find_element(By.XPATH, panelist_intro).send_keys('Test panelist introduction')

    if(driver.find_element(By.XPATH, upload_image).is_displayed() and driver.find_element(By.XPATH, upload_recorded_roundtable).is_displayed()):
        print('Recorded video validation successfull')
    else:
        print('Recorded video validation failed')
        raise Exception

    time.sleep(5)

def edit_upcoming_RT():
    driver.refresh()
    time.sleep(5)
    driver.find_element(By.XPATH, my_rt).click()
    time.sleep(5)
    driver.find_element(By.XPATH, edit_rt).click()

def check_noti_and_validate():
    driver.find_element(By.XPATH, notification).click()
    
    if(driver.find_element(By.XPATH, accept_btn).is_displayed() and driver.find_element(By.XPATH, reject_btn).is_displayed):
        print('Validation successful for round table invitations')
    else:
        print('Validation failed for roundtable invitaion')
        raise Exception

def go_to_network_and_validate():
    driver.find_element(By.XPATH, notifications).click()
    driver.find_element(By.XPATH, network).click()

    if((driver.find_element(By.XPATH, first_noti).is_displayed()) and ("started following you" in  driver.find_element(By.XPATH, first_noti).text)):
        print('Follow notification validation successful')
    else:
        print('Follow notification validation failed')
        raise Exception
    
def go_to_network_and_validate_interactions():
    driver.find_element(By.XPATH, notifications).click()
    #driver.find_element(By.XPATH, network).click()

    if((driver.find_element(By.XPATH, interaction).is_displayed()) and ("liked your post" in  driver.find_element(By.XPATH, interaction).text)):
        print('Interaction notification validation successful')
    else:
        print('Interaction notification validation failed')
        raise Exception

def go_to_profile_RT_and_validate():
    time.sleep(5)

    driver.find_element(By.XPATH, profile).click()
    driver.find_element(By.XPATH, snip_it_option).click()
    if(driver.find_element(By.XPATH, snip_it_img).is_displayed()):
        print('Snip it displayed under round table in profile - validated')
    else:
        print('Snip it displayed under round table in profile - validation failed')

def save_post_in_timeline():
    time.sleep(2)

    driver.find_element(By.XPATH, menu).click()
    driver.find_element(By.XPATH, save_btn).click()

def go_to_profile_and_validate_saved_post():
    driver.find_element(By.XPATH, profile).click()
    time.sleep(5)

    driver.find_element(By.XPATH, saved_option).click()
    driver.find_element(By.XPATH, menu).click()

    if(driver.find_element(By.XPATH, unsave_btn).is_displayed()):
        print('Save functionality validated')
        driver.find_element(By.XPATH, unsave_btn).click()
        time.sleep(3)
    else:
        print('Save functionality validation failed')
        raise Exception

def go_to_profile_and_edit():
    driver.find_element(By.XPATH, profile).click()
    time.sleep(5)
    driver.find_element(By.XPATH, edit_profile).click()
    time.sleep(10)

    driver.find_element(By.XPATH, save_changes).click()

    time.sleep(3)

    if(driver.find_element(By.XPATH, bio).is_displayed() and driver.find_element(By.XPATH, full_name).is_displayed() and driver.find_element(By.XPATH, dob).is_displayed() and driver.find_element(By.XPATH, gender).is_displayed() and driver.find_element(By.XPATH, location).is_displayed() and driver.find_element(By.XPATH, interest).is_displayed() and driver.find_element(By.XPATH, save_changes_msg).is_displayed()):
        print('Edit profile validated successfully')
    else:
        print('Edit profile validation failed')
        raise Exception

    #driver.find_element(By.XPATH, save_changes).click()

def go_to_search_and_validate():
    driver.find_element(By.XPATH, search).send_keys('Test')
    driver.find_element(By.XPATH, search).send_keys(Keys.ENTER)

    elements = driver.find_elements(By.XPATH, search_options)

    for i in elements:
        if(not i.is_displayed()):
            raise Exception
    
    print('Search validation succesful')

def go_to_profile_and_validate():
    driver.find_element(By.XPATH, profile).click()

    time.sleep(5)

    if(driver.find_element(By.XPATH, following).is_displayed() and driver.find_element(By.XPATH, follower).is_displayed()):
        print('Number of following and followers are displayed')
    else:
        print('Number of following and followers not displayed')
        raise Exception

    driver.find_element(By.XPATH, following).click()
    time.sleep(2)

    driver.find_element(By.XPATH, "(//*[text()='Followers'])[2]").click()
    time.sleep(2)

def validate_popular_shows():
    time.sleep(3)

    if(driver.find_element(By.XPATH, popular_shows).is_displayed()):
        print('Popular shows displayed')
    else:
        print('Popular shows validation failed')
        raise Exception

def validate_popular_RT():
    if(len(driver.find_elements(By.XPATH, popular_RT))>=10):
        print('Popular RT validated')
    else:
        print('Popular RT validation failed')
        raise Exception
    
    for i in driver.find_elements(By.XPATH, popular_RT_text):
        if(not i.is_displayed()):
            raise Exception
        
def validate_roundtable():
    time.sleep(3)

    if driver.find_element(By.XPATH, all).is_displayed() and driver.find_element(By.XPATH, upcoming).is_displayed() and driver.find_element(By.XPATH, live).is_displayed() and driver.find_element(By.XPATH, mine).is_displayed():
        print('RT validated for anonymous user')
    else:
        print('RT validation failed for anonymous user')

def validate_townhall_new():
    time.sleep(5)
    driver.find_element(By.XPATH, townhall).click()
    time.sleep(5)

    if(driver.find_element(By.XPATH, news).is_displayed() and driver.find_element(By.XPATH, timeline_).is_displayed()):
        print('Timeline validation successful')
    else:
        print('Timeline validation failed')
        raise Exception
    
    driver.get("https://stage.web.khulke.com/roundtable/all")
    time.sleep(5)

    driver.find_element(By.XPATH, live).click()
    time.sleep(3)
    driver.find_element(By.XPATH, upcoming).click()
    time.sleep(3)
    #driver.find_element(By.XPATH, mine).click()
    #time.sleep(3)
    #driver.find_element(By.XPATH, all).click()
    #time.sleep(3)

    driver.find_element(By.XPATH, share_btn).click()
    driver.find_element(By.XPATH, post_it).click()

    if(driver.find_element(By.XPATH, login_popup).is_displayed()):
        print("Log in pop up validated")
    else:
        print("Log in pop up validation failed")
        raise Exception


def validate_post_of_following():
    if("cbetkvak" in driver.find_element(By.XPATH, "//p[@class='sc-gswNZR kHzHci']/div/a").text):
        print('Post of following - validated')
    else:
        print('Post of following - validation failed')

def go_to_profile_and_validate_RT():
    driver.find_element(By.XPATH, "//p[@class='sc-gswNZR kHzHci']/div/a").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//*[text()='RoundTable'])[2]").click()

    if(driver.find_element(By.XPATH, "//div[@class='rt_img_div']").is_displayed()):
        print('Roundtable validated')
    else:
        print('Roundtable validation failed')
        raise Exception

## method - close browser ##
def close_browser():
    driver.implicitly_wait(10)
    driver.close()
    driver.quit()
