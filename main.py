#!/usr/bin/python

from InjectCookie import * 
from test   import *

if __name__ == '__main__':
#ptr = InjectCookie("db/Cookie")
#ptr.connectToDb()

    C = testCookie()    

    I = InjectCookie("/Users/samato/Library/Application Support/Firefox/Profiles/rzbjcf3w.default/cookies.sqlite")
    I.connectToDb()
    I.insertCookieFirefox(C)
