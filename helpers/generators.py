import random

NAMES = ("Ахилл", "Одиссей", "Агамемнон", "Гектор", "Парис", "Патрокл", "Приам")
SURNAMES = ("Великий", "Мудрый", "Прекрасный", "Ясноликий", "Первый", "Последний", "Синий")
ADDRESSES = ("Москва", "Санкт-Петербург", "Екатеринбург", "Бобруйск", "деревня Тушино")


def random_name() -> str:
    return random.choice(NAMES)

def random_surname() -> str:
    return random.choice(SURNAMES)

def random_address() -> str:
    return random.choice(ADDRESSES)

def random_phone() -> str:
    return str(random.randint(10000000000, 99999999999))
