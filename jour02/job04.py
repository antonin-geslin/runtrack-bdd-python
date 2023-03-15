import mysql.connector



connexion = mysql.connector.connect(user='root', password='IamBatman!567',
                               host='localhost', database='laplateforme')

cursor = connexion.cursor()


query = ("SELECT nom, capacite FROM salles")

cursor.execute(query)

for row in cursor:
    print(row)