import mysql.connector
if __name__ == "__main__":
    connect_to_db,
    add_capital,
    del_capital,
    edit_capital,
    edit_population,
    edit_mayor

def connect_to_db():
    db = mysql.connector.connect(
        host="localhost", user="root", passwd="")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS City;")
    cursor.execute("USE City;")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS capitals (id INT AUTO_INCREMENT PRIMARY KEY, country VARCHAR(255), capitals VARCHAR(255), population INT(10), mayor VARCHAR(255))")
    return db


def add_capital(country, capital, population, Mayor):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "INSERT INTO capitals (country,capitals,population,mayor ) VALUES (%s,%s,%s,%s)"
    val = (country, capital, population, Mayor)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "Capital added\n")

def del_capital(country):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "DELETE FROM `capitals` WHERE country='" + country + "'"
    val = (country)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "Capital delete\n")

def show_all_country():
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `capitals`")
    rows = cursor.fetchall()
    print("\n\n")
    for row in rows:
        print("[ID] = ", row[0], "\n[country] = ", row[1], "\n[capital] = ", row[2], "\n[population] = ", row[3], "\n[Mayor] = ",row[4])
        print("====================================================")
    print ("\n")

def edit_capital(country,capital):
    db = connect_to_db()
    cursor = db.cursor()
    sql = " UPDATE capitals SET capitals='" + capital + "' WHERE country = '" + country + "'"
    val = (country)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "recort update inserted\n")

def edit_population(country, population):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "UPDATE capitals SET population='" + population + "' WHERE country='" + country + "'"
    val = (country)
    cursor.execute(sql, val)
    db.commit()

def edit_mayor(country, Mayor):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "UPDATE capitals SET Mayor= '" + Mayor + "' WHERE country='" + country + "'"
    val = (country)
    cursor.execute(sql, val)
    db.commit()