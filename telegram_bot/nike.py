import requests
from bs4 import BeautifulSoup
import requests


def get_products_by_category(category):
    # создание URL-адреса для выбранной категории
    url = f"https://www.nike.com/w/mens-shoes-nik1zy7ok"
    if category == 'женская обувь':
        url = f"https://www.nike.com/w/womens-shoes-5e1x6zy7ok"
    if category == 'детская обувь':
        url = f"https://www.nike.com/w/kids-shoes-v4dhzy7ok"
    if category == 'New&featured':
        url = f"https://www.nike.com/w/new-3n82y"
    # загрузка HTML-страницы
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # извлечение информации о продуктах и ценах
    products = []
    prices = []
    for product in soup.select('.product-card'):
        # извлечение названия продукта
        product_name = product.find('div', {'class': 'product-card__title'}).text.strip()
        # извлечение цены продукта
        product_price = product.find('div', {'class': 'product-price'}).text.strip()
        products.append(product_name)
        prices.append(product_price)

    # объединение названий продуктов и цен в одну строку и возврат
    result = ''
    for i in range(len(products)):
        result += f'{products[i]}: {prices[i]}\n'
    return result

