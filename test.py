import Cookie,os

def testCookie():
    C = Cookie.SimpleCookie()
    key = "bbsesionhash" 
    C[key] = "1addc245f9a8cd98a12d6efc79f5d92f"
    C[key]['domain'] = ".slickdeals.net"
    C[key]['path'] = "/"
    C[key]['httponly'] = "true"
    print C
    return C[key]
def test2():
    C = Cookie.SimpleCookie()
    cookie_string = os.environ.get('HTTP_COOKIE')
    print cookie_string
    C.load(cookie_string)
    print C
