import requests

def login():
    url = 'https://www.douban.com/people/199444704/'
    headers = {
        'Cookie':'ll="118236"; bid=EHVvIcOdZB4; __utma=30149280.1827010698.1582522526.1582538139.1582610792.4; __utmz=30149280.1582610792.4.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1582610789%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DcQMpBFRKp5w69cQfN6mJ0JgWS_-LbQ9NYKZM5knBUL37bpOE0jBkoITmCYfS8OkA%26wd%3D%26eqid%3D90abb3ab000b9b17000000035e54b95f%22%5D; _pk_id.100001.8cb4=83aee98f67a9fc56.1582610789.1.1582611467.1582610789.; _pk_ses.100001.8cb4=*; __utmb=30149280.43.10.1582610792; __utmc=30149280; dbcl2="199444704:KYOGHyXxSLM"; ck=3CTG; ap_v=0,6.0; __yadk_uid=xxLUyFEbsiGmJQUUOMFjwwxX1HUWqVJ8; __gads=ID=e3ef8c4b1a42c5ca:T=1582610861:S=ALNI_MYJBtrzroQ5o1b32No4JtqxsO3SJw; push_noty_num=0; push_doumail_num=0; __utmv=30149280.19944; ps=y; douban-profile-remind=1; gr_user_id=5dc766e0-5223-41f5-97ad-920deb5188a7; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=995968df-d734-46e2-9eb8-7f5004e4b0a8; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_995968df-d734-46e2-9eb8-7f5004e4b0a8=true; gr_cs1_995968df-d734-46e2-9eb8-7f5004e4b0a8=user_id%3A1; __utmt_douban=1; loc-last-index-location-id="118236"; __utmt=1',
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'
    }
    html = requests.get(url=url,headers=headers).text
    print(html)

if __name__ == '__main__':
    login()
