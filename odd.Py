# This program prints if the program was executed at odd minute
# To learn datetiime
# from standard_library import module
# Used: sys.platform, os.getcwd(), os.environ, os.getenv()
#       sys.version, datetime.today().(minute/day/month/year)
#       from datetime import datetime => datetime.today().(minute/day/month/year)
#       import datetime => datetime.date.today().(minute/day/month/year)
#       import time => time.strftime()
#       import html => html.escape(), html.unescape()


from datetime import datetime
import sys
import os

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]
right_this_minute = datetime.today().minute

print("Platform:",sys.platform)
print("Version:",sys.version)
print("Working directory:", os.getcwd())
#print("Env variables:", os.environ)
print("Get environment varibale NUMBER_OF_PROCESSORS:", os.getenv('NUMBER_OF_PROCESSORS'))
if right_this_minute in odds:
    print("this minute seems a little odd!", right_this_minute)
else:
    print("Not an odd minute.", right_this_minute)



    
#when you do from datetime import datetime then do datetime.today.date()
#Todays date will be printed in longer version 2019-08-04 13:09:54.771319
    

print("Today's date:",datetime.today())
print("Today's date day:",datetime.today().day)
#print("Today's date day:",datetime.today().day)
print("Today's date month:",datetime.today().month)
print("Today's date year:",datetime.today().year)

#when you do import datetime, use import datetime.date.today()

import datetime
print("Today's date:",datetime.date.today())
print("Today's date day:",datetime.date.today().day)
#print("Today's date day:",datetime.date.today().day)
print("Today's date month:",datetime.date.today().month)
print("Today's date year:",datetime.date.today().year)


import time
print("Format current time:",time.strftime("%H:%M:%S"))
print("Format current time (Sun PM):",time.strftime("%H:%M:%S %A %p"))

import html
print(html.escape("This HTML fragment contains a <script>script</script> tag."))
print(html.unescape("I &hearts; Python. This HTML fragment contains a &lt;script&gt;script&lt;/script&gt; tag."))  
