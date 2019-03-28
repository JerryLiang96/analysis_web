#coding:utf-8
import re
import time
import requests
import csv
import random
from bs4 import BeautifulSoup as bs


class Crawler(object):
    def __init__(self):
        self.is_login = False
        self.session = self._login()

    def _login(self):
        if self.is_login is True:
            return

        headers = self.get_headers()
        proxies = self.get_proxies()
        session = requests.session()

        form_data = {
            'ck': 'AEus',
            'name': '17863017628',
            'password': 'liang665104',
            'remember': 'true',
            'ticket': ''
        }

        url = 'https://accounts.douban.com/j/mobile/login/basic'

        html = session.post(
            url=url,
            data=form_data,
            headers=headers,
            verify=False,
            proxies=proxies)
        if html.status_code == 200:
            self.is_login = True
            print('登录成功')
            return session
        else:
            print(html.text)
            print('登录失败')
            return False

    def get_proxies(self):
        host_list = ['10.20.1.125', '10.20.1.126', '10.20.1.127']
        proxy_list = [
            '10.152.130.12:5323', '10.152.130.14:5323', '10.152.130.15:5323',
            '10.152.130.17:5323', '10.152.130.19:5323', '10.152.130.23:5323',
            '10.152.130.28:5323', '10.152.130.22:5323', '10.152.130.56:5323',
            '10.152.130.45:5323', '10.152.130.41:5323', '10.152.130.46:5323'
        ]
        host = random.choice(host_list)
        proxy = random.choice(proxy_list)
        print(host, proxy)
        proxies = {'http://' + host: 'http://' + proxy}
        return proxies

    def get_headers(self):
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

        user_agent = random.choice(user_agent_list)

        # raw_cookies = '''__utmz=30149280.1551147826.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="118227"; push_doumail_num=0; _vwo_uuid_v2=DAB861ABCCAB7BCF8D7ABFD0EF97E254C|1412875d6fd549c93acc76e24ff7cfa5; ap_v=0,6.0; bid=3bmcHpleCsM; __utma=30149280.818389897.1551147826.1551147826.1551147826.1; __utmb=30149280.17.10.1551147826; __utmv=30149280.19243; __utmt=1; push_noty_num=0; __utmc=30149280; _pk_ref.100001.2fad=%5B%22%22%2C%22%22%2C1551147909%2C%22https%3A%2F%2Fmovie.douban.com%2Fsubject%2F1652592%2Fcomments%3Fstart%3D220%26limit%3D20%26sort%3Dnew_score%26status%3DP%26percent_type%3D%22%5D; _pk_id.100001.2fad=b479741da9da7840.1551147909.1.1551148698.1551147909.; _pk_ses.100001.2fad=*; login_start_time=1551148708422; user_data={%22area_code%22:%22+86%22%2C%22number%22:%2217863017628%22%2C%22code%22:%229918%22}; vtoken=phone_register%20574ee507b352490d8f07a32db81337e4'''

        headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN',
            'Cache-Control': 'no-cache',
            'Connection': 'Keep-Alive',
            'Content-Length': '59',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'accounts.douban.com',
            'Origin': 'https://accounts.douban.com',
            'Referer':
            'https://accounts.douban.com/passport/login_popup?login_source=anony',
            'User-Agent': user_agent,
            'X-Requested-With': 'XMLHttpRequest'
        }
        return headers

    分析首页函数, 电影生成器
    def create_movie_object(self):
        resp = requests.get(
            url='https://movie.douban.com/nowplaying/',
            proxies=self.get_proxies())
        html_data = resp.text
        soup = bs(html_data, 'html.parser')
        nowplaying_movie = soup.find_all('div', id='nowplaying')
        nowplaying_movie_list = nowplaying_movie[0].find_all(
            'li', class_='list-item')
        for item in nowplaying_movie_list:
            showed = item['data-showed']
            if showed == False:
                continue
            nowplaying_dict = {}
            movie_id = item['data-subject']
            movie_director = item['data-director']
            movie_name = item['data-title']
            movie_score = item['data-score']
            movie = Movie.objects.create(
                id=movie_id,
                director=movie_director,
                name=movie_name,
                score=movie_score)
            yield movie

    #爬取评论函数，评论数据生成器
    def _get_comments_by_id(self, movie_id):
        if self.is_login is False:
            print('未登录')
            return
        requrl = 'https://movie.douban.com/subject/' + movie_id + '/comments?start=0&limit=20'
        resp = self.session.get(url=requrl, proxies=self.get_proxies())
        html_data = resp.text
        soup = bs(html_data, 'html.parser')
        label = soup.find_all('li', class_='is-active')
        for item in label:
            comment_num = item.find_all('span')[0].string
            comment_num = int(re.search(r'\d+', comment_num).group(0))

        print('{0:-^30}'.format('共有评论' + str(comment_num) + '条'))

        if comment_num >= 500:
            comment_num = 500

        page_num = int(comment_num / 20)
        #开始获取数据
        print('{0:-^30}'.format('获取最热' + str(comment_num) + '条评论'))
        for page in range(page_num):
            start = page * 20
            requrl = 'https://movie.douban.com/subject/' + movie_id + \
                    '/comments?start=' + str(start) + '&limit=20'
            try:
                resp = self.session.get(url=requrl, proxies=self.get_proxies())
                html_data = resp.text
                soup = bs(html_data, 'html.parser')
                #获取相关数据
                comment_div_lits = soup.find_all('div', class_='comment')
                for item in comment_div_lits:
                    for value in item.find_all('span', class_='comment-info'):
                        username = value.find_all('a')[0].string
                        star_rate = value.find_all('span')[1]['title']
                        comment_time = value.find_all(
                            'span', class_='comment-time')[0].string
                    vote = item.find_all('span', class_='votes')[0].string
                    short_comment = item.find_all(
                        'span', class_='short')[0].string
                    #修正格式
                    username = username.strip()
                    star_rate = star_rate.strip()
                    short_comment = re.sub('[\r\n\t]', '', short_comment)
                    vote = vote.strip()
                    comment_time = re.search(r'\d+-\d+-\d+',
                                             comment_time).group(0)
                    data = [
                        username, star_rate, short_comment, vote, comment_time,
                        movie_id
                    ]
                    time.sleep(random.uniform(0.1, 0.2))
                    yield data
                print('{0:-^30}'.format('已获取第' + str(page + 1) + '页'))
            except Exception as e:
                print("遇到问题，以下为问题描述及出错页面：")
                print(e)
                continue

    def comments_save_csv(self, movie_id):
        with open(
                "csv_file/" + movie_id + ".csv", "a", encoding="utf8",
                newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            data = self._get_comments_by_id(movie_id)
            #初始化csv文件
            spamwriter.writerow([
                "user_name", "star_rate", "short_comment", "vote",
                "comment_time", "movie_id"
            ])
            try:
                while True:
                    spamwriter.writerow(next(data))
            except StopIteration:
                print('任务结束')

    def comments_save_db(self, movie_id):
        import pymysql
        con = pymysql.connect(
            host='localhost', user='root', passwd='665104', db='analysis_db')

        cursor = con.cursor()
        sql = "insert into comment_comment (username, star_rate, short_comment, vote, time, movie_id) VALUE (%s,%s,%s,%s,%s,%s);"
        label = [
            'username', 'star_rate', 'short_comment', 'vote', 'time',
            'movie_id'
        ]
        data = self._get_comments_by_id(movie_id)
        try:
            while True:
                data_dict = dict(zip(label, next(data)))
                cursor.execute(sql,
                               (data_dict['username'], data_dict['star_rate'],
                                data_dict['short_comment'], data_dict['vote'],
                                data_dict['time'], data_dict['movie_id']))
                con.commit()  #把修改的数据提交到数据库
        except StopIteration:
            cursor.close()
            con.close()
            print('迭代结束')
            print('爬虫任务结束')
        except Exception as e:
            con.rollback()
            print(e)
            print('发生错误，已回滚数据库')


if __name__ == "__main__":
    crawler = Crawler()
    # movie_id_list = crawler.create_movie_object()
    # while True:
    #     movie = next(movie_id_list)
    movie_id = '26213252'
    crawler.comments_save_db(movie_id)

    # crawler.comments_save_db(movie)
