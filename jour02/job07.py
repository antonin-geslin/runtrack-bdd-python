import mysql.connector







class ManageEmployes():


    def __init__(self, user, password, database, host='localhost'):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.connexion = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
        self.cursor = self.connexion.cursor()


    def createEmploye(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.connexion.commit()

    def getEmploye(self, id):
        query = ("SELECT * FROM employes WHERE", id)
        self.cursor.execute(query)
        for row in self.cursor:
            print("id : ", row[0])
            print("nom : ", row[1])
            print("prenom : ", row[2])
            print("salaire : ", row[3])
            print("id_service : ", row[4])


    def getAllEmployes(self):
        query = ("SELECT * FROM employes")
        self.cursor.execute(query)
        for row in self.cursor:
            print("id : ", row[0])
            print("nom : ", row[1])
            print("prenom : ", row[2])
            print("salaire : ", row[3])
            print("id_service : ", row[4])


    def deleteEmploye(self, id):
        query = f"DELETE FROM employes WHERE id = {id}"
        self.cursor.execute(query)
        self.connexion.commit()



connexion = ManageEmployes("root", "", "job7")

connexion.createEmploye("TOTO", "Titi", 1200, 2)
connexion.deleteEmploye(13)
connexion.getAllEmployes()
