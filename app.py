from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Имитация базы данных (список словарей)
orders = [
    {"id": 1, "client": "Иван Иванов", "device": "iPhone 13", "status": "В работе", "date": "2024-04-10"},
    {"id": 2, "client": "Анна Смирнова", "device": "MacBook Air", "status": "Готов", "date": "2024-04-11"}
]

@app.route("/")
def index():
    # Отображаем главную страницу со списком всех заказов
    return render_template("index.html", orders=orders)

@app.route("/add", methods=["GET", "POST"])
def add_order():
    if request.method == "POST":
        # Получаем данные из формы и добавляем в список
        new_order = {
            "id": len(orders) + 1,
            "client": request.form.get("client"),
            "device": request.form.get("device"),
            "status": "Новый",
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        orders.append(new_order)
        return redirect(url_for("index"))
    return render_template("add_order.html")

if __name__ == "__main__":
    app.run(debug=True)
