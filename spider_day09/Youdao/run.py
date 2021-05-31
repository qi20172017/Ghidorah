# from scrapy import cmdline
# cmdline.execute('scrapy crawl youdao'.split())

def get_cookie():
    cookie = "OUTFOX_SEARCH_USER_ID=970246104@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=570559528.1224236; _ntes_nnid=96bc13a2f5ce64962adfd6a278467214,1551873108952; JSESSIONID=aaae9i7plXPlKaJH_gkYw; td_cookie=18446744072941336803; SESSION_FROM_COOKIE=unknown; ___rl__test__cookies=1565689460872"
    cookie_dir = {}
    for kv in cookie.split('; '):
        # res = kv.split('=')
        # cookie_dir[res[0]] = res[1]
        k,v = kv.split('=')
        cookie_dir[k]=v
    return cookie_dir

print(get_cookie())