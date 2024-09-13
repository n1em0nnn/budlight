import sqlite3
from xlsxwriter.workbook import Workbook
workbook = Workbook('output2.xlsx')
worksheet = workbook.add_worksheet()
conn=sqlite3.connect('db.sqlite3')
c=conn.cursor()
mysel=c.execute('SELECT username,first_name,last_name FROM auth_user')
for i, row in enumerate(mysel):
    print(row)
    worksheet.write(i, 0, row[0])
    worksheet.write(i, 1, row[1])
workbook.close()