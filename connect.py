import pyodbc

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-EP03SKT;"
                      "Database=Wardrobe;"
                      "Trusted_Connection=yes;")

cursor = cnxn.cursor()

cursor.execute("SELECT * FROM dbo.War")

rows = cursor.fetchall()

for row in rows:
    print('Type:', row[0])
    print('Name:', row[1])
    print('Brand:', row[2])
    print('Color:', row[3])
    print('Price:', row[4])
    print('-----------------------')

cursor.close()
cnxn.close()