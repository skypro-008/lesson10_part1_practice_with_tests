from flask import Flask, request

app = Flask(__name__)

locations = [
    "Москва",
    "Санкт-Петербург",
    "Новосибирск",
    "Екатеринбург",
    "Казань",
    "Нижний Новгород",
    "Челябинск",
    "Самара",
    "Омск",
    "Ростов-на-Дону",
    "Уфа",
    "Красноярск",
    "Воронеж",
    "Пермь",
    "Волгоград",
    "Краснодар",
    "Волгоград",
    "Саратов",
    "Тюмень",
    "Тольятти",
    "Ижевск",
]


@app.route("/search/")
def get_cities():
    s = request.args.get("s").lower()
    locations_match = [x for x in locations if s in x.lower()]
    if len(locations_match):
        return ", ".join(locations_match)
    return "", "Городов не найдено"


if __name__ == '__main__':
    app.run()
