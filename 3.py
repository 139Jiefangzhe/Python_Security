import requests
import base64

#https://fofa.info/api/v1/search/all?email=your_email&key=your_key&qbase64=dGl0bGU9ImJpbmci



def get_fofa_data(email,apikey):
    for eduname in open('eduname.txt',encoding='utf-8'):
        e=eduname.strip()
        search='"%s" && country="CN" && title=="Error 404--Not Found"'%e
        b=base64.b64encode(search.encode('utf-8'))
        b=b.decode('utf-8')
        url='https://fofa.info/api/v1/search/all?email=%s&key=%s&qbase64=%s'%(email,apikey,b)
        s=requests.get(url).json()
        print('查询->'+eduname)
        print(url)
        if s['size'] != 0:
            print(eduname+'有数据啦！')
            for ip in s['results']:
                print(ip[0])
        else:
            print('没有数据')







if __name__ == '__main__':
    email='471656814@qq.com'
    apikey='0fccc926c6d0c4922cbdc620659b9a42'
    get_fofa_data(email,apikey)