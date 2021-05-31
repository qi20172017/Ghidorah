from requests import session
import requests
s = session()
url = 'https://accounts.douban.com/j/mobile/login/basic'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'

}
form = {
    'ck':'',
    'name': '19821836503',
    'password': '316952817qweQWE.',
    'remember': 'false',
    'ticket':''
}


html = s.post(url=url,headers=headers,data=form).text
print(html)
person_url = 'https://www.douban.com/people/199444704/'
person_html = s.get(url=person_url,headers=headers).text
print(person_html)
# with open('login.html','w')as f:
#     f.write(html)