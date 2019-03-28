import csv
with open("yingping.csv", "a", encoding='utf-8', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(
        ["user", "star_rate", "comment", "vote", "comment_time"])
    user_name = 'sss'
    star_rate = '21323'
    short_comment = 'ssssadsafewfseftgretesfdfsdfesradaseawewadsad'
    vote = '123'
    comment_time = '1111111111111'
    spamwriter.writerow(
        [user_name, star_rate, short_comment, vote, comment_time])
    #ceshiaaaaaaaaaaaaaaaaaa