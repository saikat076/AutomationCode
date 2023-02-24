from behave import *
from action import *
from testcase2 import *

I_open_the_browser("https://stage.web.khulke.com/roundtable/all")
I_log_in_with_email('saikatbhattacharyya631@gmail.com', 'Saikat123@')
try:
    I_validate_login_functionality()
except:
    print("")