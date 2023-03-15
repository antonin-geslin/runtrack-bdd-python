import mysql.connector



cnx = mysql.connector.connect(user='root', password='IamBatman!567',
                               host='localhost', database='laplateforme')

cursor = cnx.cursor()


query = ("SELECT * FROM etudiants")

cursor.execute(query)

for row in cursor:
    print(row)