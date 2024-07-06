from flask import Flask
from flask_admin import Admin
from models import db, User, Basket
from admin import BasketAdminView

app = Flask(__name__)
app.config.from_object('config.Config')

# Ініціалізація бази даних
db.init_app(app)

# Ініціалізація адмін-панелі
admin = Admin(app, name='SQLAdmin Example', template_mode='bootstrap3')

# Додавання моделей до адмін-панелі
admin.add_view(BasketAdminView(Basket, db.session, category='Basket Management', name='Baskets'))

# Додавання маршруту для перевірки
@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Створення таблиць у базі даних
    app.run(debug=True)
