import requests
from bs4 import BeautifulSoup
import requests


def get_products_by_category(category):
    # создание URL-адреса для выбранной категории
    url = f"https://www.adidas.com/us/men-shoes"
    if category == 'женская обувь':
        url = f"https://www.adidas.com/us/women-shoes"
    if category == 'детская мальчиковая обувь':
        url = f"https://www.adidas.com/us/boys-shoes"
    if category == 'детская девчачья обувь':
        url = f"https://www.adidas.com/us/girls-shoes"
    if category == 'New&featured MAN':
        url = f"https://www.adidas.com/us/men"
    if category == 'New&featured WOMAN':
        url = f"https://www.adidas.com/us/women"
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
