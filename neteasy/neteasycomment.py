#获取网易云音乐评论
#1.找到未加密参数        window.asrsea()
#2.找到参数加密方式      params => encText encSecKey =>  
#3.请求网易，获取评论

from Crypto.Cipher import AES
from base64 import b64encode
import json
import requests

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

#1.原始数据
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_2606045283",
    "threadId": "R_SO_4_2606045283"
}


#2.加密过程
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "hvv3RQmJaWBrn64E"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

def get_encSecKey():
    return "8b812556b33ecebfde7f4fe7de4472c0f1039c6aed0d841168a2c2dfd9e8e2b56140da1f5746b96d6938c92b9c50fa4ae16ac021165b87433939e95f23f110bbbd3f654531d19b3d783dfa8516f16351375cad78137981c0b35f630f0ff6eb7f3aa930f9dcf49085cf4761eb8356d4eb251adcbcbd74417cc3937556b189a674"

def get_params(data):
    first = enc_params(data,g)
    second = enc_params(first,i)
    return second

def enc_params(data,key):
    iv = "0102030405060708"
    aes = AES.new(key=key.encode("utf-8"),mode=AES.MODE_CBC,IV=iv.encode("utf-8"))
    bs = aes.encrypt(to_16(data).encode("utf-8")) #加密,加密长度必须为16的长度
    return str(b64encode(bs),"utf-8") #转换为字符串

 

"""
function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d, #偏移量
            mode: CryptoJS.mode.CBC #加密模式
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);  16位随机数  
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),  如果i固定 则这个也是固定
        h
    }

    var bVi6c = window.asrsea(JSON.stringify(i0x), bse6Y(["流泪", "强"]), bse6Y(Qu1x.md), bse6Y(["爱心", "女孩", "惊恐", "大笑"]));
            e0x.data = j0x.cr1x({
                params: bVi6c.encText,
                encSecKey: bVi6c.encSecKey
            })
"""

#3.参数加密后请求数据
resp = requests.post(url, headers=headers,data={
    "params":get_params(json.dumps(data)),
    "encSecKey":get_encSecKey()
})

commentData = resp.json()['data']

print(commentData)