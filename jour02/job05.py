import mysql.connector



cnx = mysql.connector.connect(user='root', password='IamBatman!567',
                               host='localhost', database='laplateforme')

cursor = cnx.cursor()

query = ("SELECT superficie FROM etage")

cursor.execute(query)

temp = 0

for row in cursor:
    temp += row[0]


print("La superficie de laplateforme est de  : ", temp, "m²")