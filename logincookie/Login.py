#这里是模拟登录操作，然后获取cookie后进行获取登录用户信息

import requests

# 会话
seesion = requests.session()
data = {
    "loginName": "xxx",
    "password": "xxx"
}
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Referer":"https://passport.17k.com/login/",
    "Origin":"https://passport.17k.com",
    "Host":"passport.17k.com",
    "Content-Length":"43",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
}
cookies = {
    "Cookie":"GUID=031404f8-ec33-43a1-852a-ca41284434ef; acw_sc__v2=6692301563cc411f6b2717280d47172fdb79dabf; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1720856599; HMACCOUNT=B8B744795366A2C5; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F10%252F70%252F40%252F103604070.jpg-88x88%253Fv%253D1719926339000%26id%3D103604070%26nickname%3D5kai%26e%3D1736408907%26s%3D76db2af297fea4f2; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22103604070%22%2C%22%24device_id%22%3A%22190ab0bd9721a-04dfe487fa2a94-26001f51-2073600-190ab0bd973b26%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22031404f8-ec33-43a1-852a-ca41284434ef%22%7D; ssxmod_itna=mqIxyDRD2DcAG=YGHD8Wba4DqD59kAwig4hwqqGXKoDZDiqAPGhDCb3I+TT4rqhr5qE4bDuDsLSAocDKC8RGi3IlAYx0aDbqGkeIG4iicDCeDIDWeDiDG4GmB4GtDpxG=DjAKtZSjxYPDEAKDaxDbDim8mxGCDeKD0Z+FDQKDucIKDGvKCf2DDYmP4zAFdtym2r0hmAKD9aoDs2Dj8A9w2tLKg1AfmD73mx0kxq0Oc=vzC=oDUn9z9x7NWm44H2wob003w02DWAxxNCp4YEDxV7/atCUK3jueHADNHAxDioVPwdD; ssxmod_itna2=mqIxyDRD2DcAG=YGHD8Wba4DqD59kAwig4hwqA=nT=3=D/QQ7DFrrq298YggPAP3n/pwq0CVWiuY2h3O+loipoE=7fT8K0FPhXI8j668cXWaz68B2WuptH7IvHRaok8hTNHzF4YzPFaiD7FOi7awCA1XnI73byCk6ywK=OG3OBCYixwOogiglDqNIBCqfWzW9OCf+fwH8uAUSyd0OqxLbqv9SwL=WdziKlIgz80eGkKC7w4e7q4qYSWYglseP7=whi=Vjlk4Zuq81mxqotWWo/k7kqQoozin7KcnZuDqomCxFei0usl4Sd9R8rOC0RQxui0RYMLzU+hGRhrl3=Cd=lKNfO535Bf+kn3sn+rnYYo5sS5twmwjT=rp6e7XjrHEmwwI7Qb0msT+IHOt/AG7lGjCrISThOidePD7QPihPAx4YLcmDgawI/nARYMiar1LVCq6lDhlGpcQKmD6K92F9KDGcDG78iDD; tfstk=fy7Jyi68g-2k8KrhP_ZctRKUfiNDJaCyZT5s-pvoAtBA11kkA3g7piBC33v5J6upO66UapVzm_5y8ewgIwUGa_JdZyU3s4iXGsRidmYQAM5y8ewmi2ZgW_WTxD60eeNvlBdKRetWOrNvtChWRLtIhmO6hpTBR9TjcBRHd49BFngjMiephb9nJMHMerUKQYZabZdbLd18s2AAuQKJC__-R2Nvw3p1NKeM1spDc6-d8Xupf_sNLC6SFJpFks_5fOwmqLs991jdNzgXra55fH__LD69y9K1PnhIyE8vFEdf5WmwnZpldaKbsVKHlNx6Piq4EHYJ69_PeX3CCsfGzn7LBx9FqC8X9wPsvpKC4yQGW77-IddnVSFxYD-WipPO1IA5zdF9MdV8JDoe0SRvISFxYD-WgIpgw8nEYnPV.; Hm_lpvt_9793f42b498361373512340937deb2a0=1720858354"
}

loginCookies = {
    "Cookie":"GUID=031404f8-ec33-43a1-852a-ca41284434ef; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1720856599; HMACCOUNT=B8B744795366A2C5; c_channel=0; c_csc=web; acw_sc__v2=66927219911b325dee0c3218dc39f4f9f0f98f9e; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22031404f8-ec33-43a1-852a-ca41284434ef%22%2C%22%24device_id%22%3A%22190ab0bd9721a-04dfe487fa2a94-26001f51-2073600-190ab0bd973b26%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22031404f8-ec33-43a1-852a-ca41284434ef%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1720873523; acw_tc=2760829817208735269087848e14749e10f90571d8e1b564d40baad34b7f53; ssxmod_itna=eqjxg7Dti=T4uDGxBPGI2CDUxYTQEZj0E=lOEr=D0y0ReGzDAxn40iDt=rHpig2O25=Le/YwxN6/eE7mIaYnCfpoDU4i8DCMxvooIDYYCDt4DTD34DYDixib8xi5GRD0KDFWqvz19Dm4GWWqGfDDoDYb=RDitD4qDBmxdDKqGg8d4D0MEvQDDhUi0q282gIQU5tCGxWqDMfeGXFD9YWM27v=+ltQcaxCPRDB6GxBjSITN6IeDH8kNMDC4tf7pEvB50FAp5C0G3+Bx4fDotKi+Rs7lKmY45+0dQWg8DGReQY7+PeD; ssxmod_itna2=eqjxg7Dti=T4uDGxBPGI2CDUxYTQEZj0E=lOEPxnI8bWeDsrDLl7tH0WoNu=v0u5i84q/uB0z5E=7otv=T9mqxw8GcQfxjNxIPyts=yZig47aWU1rHnNXRUg9nR1yl8O8DTL5F/OH2yQkZ5iP4wNDnbW/=q=Hcn+5PO13STa=cvpTtwmzcow3FHID+YACSoHnjpApbwmjS7EWREIv/orMiSKIRWa/inOm+vjDo9r55L6yO8FNASQS/nFs22D0Yo=aW2uDwwYZFShn=EylfhjahzfLMua6selkrivpxeZoFe/PpF/5csr3T+jHwbpDd46/mVQ96BbfYabFYnW71zPubYNmYe17PNP59hPV2F4OxR7FlD99ae9r9023axDKMx8Gk7hYzD5C05ujIq73BCDSj5eGq9npnMx9BknQK/lAciEQ0AzD1C0DvnP7O3rAfH=vrDDLxD2+23T052brwirqfDD; tfstk=f2tjtNsXzSVX8kJ5sZHPABL0FBjsLIiEcR69KdE4BiIvBG99I15V718529dcWnS23QM6wBvV7iK6rl9HInkcbxjDnGjtTXoefKvcjmsY_ExfyLBpeOeAkxJiJZStTXozVXW-YGLNdN8MFLClCteAkCe-FO61XoQTDzFRZOIO6CCYw0B1LlBTXoB-iVeCCq1DhYOJ_BTS5ApfNlELKtbYZK4ajlmF3Z5de_ZOU36fl6pvmFRw-TKyVw7zQjjJKURAFMibttTJdiB6jvU11NtcV_OIvlXkkItR53kioLt1GwKAP-MDhiB96NToOkWf0U_BcEDgwKdFGeIDQJG2FwT5-TQ8CrI28p-GJnnbt_7hCQ_elXZX9g-bY6NIjPw5-lB5TYM7SPSEwJd8a_fo_ZBlhakSFSLGkTX5TYM7SPbAEt6EFYNvS"
}


# 登录
url = "https://passport.17k.com/ck/user/login"
# resp = seesion.post(url,data=data,headers=headers)
resp = requests.post(url=url,data=data,headers=headers,cookies=loginCookies)
print(resp.text)

#登录被限制 先用浏览器的cookie做个处理
# url2 = "https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919"

# resp = requests.get(url=url2,headers=headers,cookies=cookies)

# print(resp.json())
