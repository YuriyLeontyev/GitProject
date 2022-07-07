from fastapi import FastAPI
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
