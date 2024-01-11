menu = [
    {'title': "Отзывы", 'url_name': "comment"},
    {'title': "Услуги", 'url_name': "service"},
    {'title': "Акции", 'url_name': "discount"},
    {'title': "Контакты", 'url_name': "contact"},
    {'title': "Личный Кабинет", 'url_name': "account"},
    {'title': "Регистрация", 'url_name': "register"},
    {'title': "Авторизация", 'url_name': "auth"},
    {'title': "Главная", 'url_name': ""}

]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        context['menu'] = user_menu
        return context
