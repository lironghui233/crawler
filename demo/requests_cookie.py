

# 登陆 —> 得到cookie
# 带着cookie 去请求到书架url -> 书架上的内容

# 必须把上面的两个操作连起来
# 我们可以使用session进行请求 -> session你可以认为是一连串的请求，在这个过程中的cookie不会丢失

import requests

# 会话
session = requests.session()

# 1. 登陆
url = "https://passport.17k.com/ck/user/login"

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}
data = {
    "loginName":"19928416305",
    "password":"li123123"
}
resp = session.post(url, data=data, headers=headers)
# resp.encoding = "utf-8"
# print(resp.text)
# print(resp.cookies)

# 2. 拿书架上的数据
# 刚才哪个session中是有cookie的
resp = session.get('https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919')
print(resp.json())

resp = requests.get('https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919', headers={
    "Cookie":"GUID=612d02a3-48ac-4a47-9925-864e04567e3b; sajssdk_2015_cross_new_user=1; BAIDU_SSP_lcr=https://cn.bing.com/; Hm_lvt_9793f42b498361373512340937deb2a0=1730885627; HMACCOUNT=D593412F7E6E46B2; c_channel=0; c_csc=web; acw_sc__v2=672b441ad6677328a0a8befbc7bc6c5f1473ced3; ssxmod_itna=YqIOY5D5AIqUxiq0KGHiiQnLwDGopCCpl1cr=Yp1x0yc4PGzDAxn40iDtraqr+9O0+Nt7=mGKYiS0Si5IqOtr3eH1iIx0aDbqGkKDbxiigDCeDIDWeDiDG4GmS4GtDpxG=Djjtz1M6xYPDEj5DR6PDuxBGDGP1LaKhDeKD0=uFDQ9hUcxDBZnT+gG71QYDe6Phn1ECeWSPHjKD91YDs6D61j9mczk5Sa8LXKYdpx0kPq0O9g7CH4GdU2y1x+baqDxPvQi4WjGdeQRxdrGe7vR5biD5qA=MoWDeKCbKvWNDiObKCN0P4D; ssxmod_itna2=YqIOY5D5AIqUxiq0KGHiiQnLwDGopCCpl1cr=Y1xn9Scb4DsqYDLQCxaTYo1esEFv8HKYdB0+1CedO=Yi8bCH5Ex2Pqidxq3uEjje9aMH9xwXiiMO98PsUlO1psHqQk+HnfTvmcyjkXv4Qj23wN4HAKPurdPcr64Pqj5ou22Dq2RQEKofhEjnxtyDlUE+TY42qQmjCLEQ=ARWCRVS+nuQ=H6B+AxjZTzTZ4Zz1YVCRNwXxgE3bBGB0ftpSj=I/5vz9ocK8nHXZaLd/3f=quV9ZlXH1SKHF+fK4limSaXfgcjuvdZIy8l1UwmX8=N2jNxtq4KAGm0uWAsYI4ow5ziPS0l6L5f2Q8oozLKtfFPiOxe/OE5K=M2pfnfCnRW=0hi2WZwuQu7YKCfwhlqP1X7AqGfTN9rOYrL6GdzPT30aDG2C0D+4vK0bY4xnhWESaU88n2KlqvU0xtDrtG7UiNnq2tLOoL7Gxibbk=i49r8W8koFijL1tbbY01=RkC0rB+GXr4tAeD08DiQgZ4ErjIldTnmrj=5Y9Pngj6GP0e/+Qn4mHlLtGP+padvITNDpfSUamrdxcijR3D=; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F18%252F58%252F77%252F103857758.jpg-88x88%253Fv%253D1730885849000%26id%3D103857758%26nickname%3Dleoh999%26e%3D1746441187%26s%3D877134d673d72745; tfstk=frKSg2YXt7VW7lur5JHVGqyuNJsIQBiZVJ6pIpEzpgIJpM9pK65P868fDOdlJ3SyUIMBMCvP8gKBok9MK3klYYjkEMjK_foNOLvlx1VNcrt5DsBkH9FdwYJnWaSK_fo4u-QoaMdP2Yh0cKCcdTeRpBexh96FvuQL2rFAisCdv_B-DoBhd6EdyMHXHsXdv6ho6u6qFsvS3kZSZuV1WLCbfKxGeJ1sj_ZL0n6W71pJBkEpcT_Wxeb_38byJdbM4poQmgJ6kiBBxAUCONTp4iK-McQcJeLNREP-UCdBHBjyDvUR6URPD3L_pkpfVUQhFZNSG1KkHhjAucH6HnAyEn9UpDB2_spk2MitIgsRwi6DYjqROELp4aj3wX1HcKKJRguzb1g8yywfSkBf_xMb-y0oOlJNbpzjXaBc3XkjhPJhytXf4xMb-3QRnt4mhxaaN; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22103857758%22%2C%22%24device_id%22%3A%2219300d2ab04419-057639f030cb1-4c657b58-1296000-19300d2ab0526b6%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24latest_referrer_host%22%3A%22cn.bing.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22612d02a3-48ac-4a47-9925-864e04567e3b%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1730889201"
})
print(resp.json())