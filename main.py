from fastapi import FastAPI
from scripts.colleagues_DB import colleagues_db
app = FastAPI()
#uvicorn main:app --reload

# - Сделайте домашний роут и верните словарь (справочник) со следующими данными:
# site_name, author_name, year. Добавьте информацию о себе.
# - Сделайте роут /contacts и верните ваши: город, страна, адрес вашей компании.
# - Сдетайте роут словарь с данными о коллегах, сделайте роут /colleagues/{name}
# и верните данные о коллеге или тест с ошибкой, если он не найден.


@app.get("/project")
def read_project():
    about = {
        'site_name':'earth.world',
        'author_name':'Yura',
        'year':'2022'
    }
    return about

@app.get("/project/contacts")
def read_contacts():
    contacts = {
        'country':'Qazaqstan',
        'city':'Almaty',
        'adress':'Pushkina str,Kolotushkina house'
    }
    return contacts

@app.get("/project/colleagues")
def read_colleagues():
    return colleagues_db

@app.get("/project/colleagues/{name}")
def read_colleagues_name(name):
    name = name.capitalize()

    if name in colleagues_db:
        return colleagues_db[name]
    else:
        return 'there is no user'




