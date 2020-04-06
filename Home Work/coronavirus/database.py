import mysql.connector


if __name__ == "__main__":
    connect_to_db,
    add_corona,
    show_corona
    update_stat



def connect_to_db():
    db = mysql.connector.connect(host="localhost", user="root", passwd="")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS corona_virus;")
    cursor.execute("USE corona_virus")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS CORON (id INT AUTO_INCREMENT PRIMARY KEY, Country VARCHAR(255), " \
        "Slug VARCHAR(255), NewConfirmed INT(10), TotalConfirmed INT(10),NewDeaths INT(10),TotalDeaths INT(10), " \
        "NewRecovered INT(10),TotalRecovered INT(10), Date VARCHAR(255))"
    )

    return db


def add_corona(Country, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "INSERT INTO CORON (Country,Slug,NewConfirmed,TotalConfirmed,NewDeaths,TotalDeaths,NewRecovered,TotalRecovered,Date ) " \
          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (Country, Slug, NewConfirmed, TotalConfirmed,
           NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date)
    cursor.execute (sql, val)
    db.commit()
    print(cursor.rowcount, "Coron added")


def show_corona(coron):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM CORON ORDER BY TotalConfirmed DESC")
    coron = cursor.fetchall()
    conf_all = 0
    recov_all = 0
    for item in coron:
        print("[Країна]", item[2],
              "\n[Кількість нових захворювать за добу]", item[3], "\n[Всього захворівших]",
              item[4],
              "\n[Кількість померлих за добу]", item[5], "\n[Всього померлих] ", item[6],
              "\n[Вилікуваних за добу]", item[7], "\n[Всього вилікуваних]", item[8],"\n[Дата]",item[9])
        conf_all +=item[4]
        recov_all +=item[8]
        print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("Загальна кількість хворих  ➤", conf_all, "\nЗагальна кількість вилікуваних ➤", recov_all)

def update_stat(coron):
    db = connect_to_db()
    cursor = db.cursor()
    sql = ("DELETE FROM CORON")
    cursor.execute(sql)
    db.commit()