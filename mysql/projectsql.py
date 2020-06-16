import mysql.connector
con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)
cursor = con.cursor()

w = input("Enter The Word: ")
query = cursor.execute("SELECT * FROM Dictionary WHERE EXPRESSION = '%s'"%w)
r = cursor.fetchall()

def transfer(results):
    if results:
        for i in results:
            print(i[1])
    else:
        print("No word Found")