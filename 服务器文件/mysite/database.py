import sqlite3
cu = sqlite3.connect("/webapp/gyh/zwh2/db.sqlite3")
gyh = cu.cursor()
#gyh.execute("select name from sqlite_master where type='table' order by name")
#gyh.execute("SELECT mysite_post FROM sqlite_master")
gyh.execute("SELECT * FROM mysite_post")
TAB=gyh.fetchall()
for x in TAB:
    for y in x:
        print (y)
    print("=============")
