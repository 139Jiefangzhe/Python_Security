import requests
from bs4 import BeautifulSoup


header={
    'cookie':'fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MjgyNzMsIm1pZCI6MTAwMDIxOTg4LCJ1c2VybmFtZSI6InhpYW9kaXNlYyIsImV4cCI6MTY3MTI4MjUzOH0.0ukMGFIrIvzDOzpUl9JglOoMpzbIPCczGRDeqKdmFYHfStd2jdwc6LGby3Ke0UR2suvErzhOTPYL2ACe4Goi8Q; '
}

url='https://fofa.info/result?qbase64=dGl0bGU9IuS4iua1t%2BS6pOmAmuWkp%2BWtpiIgJiYgY291bnRyeT0iQ04i'
s=requests.get(url,headers=header).text
soup = BeautifulSoup(s, 'lxml')
#获取页数
edu1=soup.find_all('p',attrs={'class': 'hsxa-nav-font-size'})
for edu in edu1:
    edu_name = edu.span.get_text()
    i=int(edu_name)/10
    yeshu=int(i)+1
    print(yeshu)
    for ye in range(1,yeshu+1):
        url = 'https://fofa.info/result?qbase64=dGl0bGU9IuS4iua1t%2BS6pOmAmuWkp%2BWtpiIgJiYgY291bnRyeT0iQ04i&page='+str(ye)+'&page_size=10'
        print(url)
        s = requests.get(url, headers=header).text
        edu1=soup.find_all('span',attrs={'class': 'hsxa-host'})
        for edu in edu1:
            edu_name = edu.a.get_text().strip()
            print(edu_name)

#获取名字
# edu1=soup.find_all('div',attrs={'class': 'hsxa-meta-data-list-main-left hsxa-fl'})
# for edu in edu1:
#     edu_name = edu.p.string
#     print(edu_name)
#获取域名
# edu1=soup.find_all('span',attrs={'class': 'hsxa-host'})
# for edu in edu1:
#     edu_name = edu.a.get_text().strip()
#     print(edu_name)
