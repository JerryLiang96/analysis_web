import os
import re
import pkuseg
import pymysql
from django.conf import settings


def creat_comment_file(movie_id):
    sql = "select short_comment from comment_comment where movie_id=" + movie_id
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    file_name = "static/comment/original/original" + movie_id + ".txt"
    with open(file_name, "a", encoding="utf8") as fp:
        for row in rows:
            fp.write(row[0])
        cur.close()


def creat_comment_files():
    try:
        con = pymysql.connect(
            host='localhost', user='root', passwd='665104', db='analysis_db')
        cur_m = con.cursor()
        sql_m = "select id from comment_movie where is_show=1"
        cur_m.execute(sql_m)
        rows = cur_m.fetchall()
        movie_list = []
        for row in rows:
            movie_list.append(row[0])
        for movie_id in movie_list:
            creat_comment_file(movie_id)
    except Exception as e:
        print(e)
    finally:
        cur_m.close()
        con.close()


if __name__ == "__main__":
    input_dir = 'C:/Users/lzr/analysis_web/static/comment/original'
    output_dir = 'C:/Users/lzr/analysis_web/static/comment/seg'
    rex = re.compile(r'[0-9]+')
    for f in os.listdir(input_dir):
        input_file_path = os.path.join(input_dir, f)
        out_f = 'seg' + rex.findall(f)[0] + '.txt'
        output_file_path = os.path.join(output_dir, out_f)
        pkuseg.test(input_file_path, output_file_path, nthread=1)
