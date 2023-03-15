import mysql.connector



cnx = mysql.connector.connect(user='root', password='',
                               host='localhost', database='laplateforme')

cursor = cnx.cursor()

query = ("SELECT capacite FROM salles")

cursor.execute(query)

temp = 0

for row in cursor:
    temp += row[0]


print("La capacite de toutes les salles est de  : ", temp)
