import requests,time
from bs4 import BeautifulSoup
# for i in range(1,204):
#     url = 'https://src.sjtu.edu.cn/rank/firm/0/?page=%s'%str(i)
#     s=requests.get(url).text
#     print(s)


# <td class="am-text-center">
# <a href="/list/firm/3086">山东省教育厅</a>
# </td>

def get_edu_name_data():
    for i in range(1,204):
        url = 'https://src.sjtu.edu.cn/rank/firm/0/?page=%s'%str(i)
        try:
            s=requests.get(url).text
            print('->正在获取第%s页面数据'%str(i))
            soup = BeautifulSoup(s, 'lxml')
            edu1=soup.find_all('tr',attrs={'class': 'row'})
            for edu in edu1:
                edu_name=edu.a.string
                print(edu_name)
                with open('eduname.txt','a+',encoding='utf-8') as f:
                    f.write(edu_name+'\n')
                    f.close()
        
        except Exception as e:
            time.sleep(1)
            pass

if __name__ == '__main__':
    get_edu_name_data()