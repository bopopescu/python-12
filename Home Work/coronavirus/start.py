from database import add_corona, show_corona, update_stat
import requests

URL = "https://api.covid19api.com/summary"


def request(URL):
    responce = requests.get(URL)
    return responce.json()


coron = requests.get(URL)
coron = coron.json()


def covid(coron):
    for item in coron["Countries"]:
        Country = item["Country"]
        Slug = item["Slug"]
        NewConfirmed = item["NewConfirmed"]
        TotalConfirmed = item["TotalConfirmed"]
        NewDeaths = item["NewDeaths"]
        TotalDeaths = item["TotalDeaths"]
        NewRecovered = item["NewRecovered"]
        TotalRecovered = item["TotalRecovered"]
        Date = item["Date"]
        add_corona(Country, Slug, NewConfirmed, TotalConfirmed,
                   NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date)


while True:
    choise = int(
        input("\n\n1. Подивитись статистику 𝐂𝐎𝐕𝐈𝐃-19 ♛ \n2. Заповнити базу данных ✎\n3. Обновити статистику 𝓋𝓅𝒹𝒶𝓉𝑒\n4. 𝐄𝐗𝐈𝐓 \n➥ "))
    if choise == 1:
        show_corona(coron)
    elif choise == 2:
        covid(coron)
    elif choise == 3:
        update_stat(coron)
        covid(coron)
    elif choise == 4:
        break
