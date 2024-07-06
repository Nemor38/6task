from flask_admin.contrib.sqla import ModelView

class BasketAdminView(ModelView):
    column_list = ('id', 'user', 'price', 'status')  # Список полів для відображення у списку інстансів
    column_searchable_list = ('id', 'user.name')  # Поля, за якими можна здійснювати пошук
    column_filters = ('user.name', 'status')  # Фільтри для колонок
    can_create = True
    can_edit = True
    can_delete = True
    page_size = 50  # Кількість записів на сторінці
    icon_type = 'glyph'
    icon_value = 'glyphicon-shopping-cart'
