import requests
import json
from bs4 import BeautifulSoup as bs
import time


# Функция для получения данных о рецептах
def get_data(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }

    data_list = []  # Список для хранения данных о рецептах
    total = 3500  # Общее количество страниц
    print(f'Всего страниц: {total}')

    # Перебираем страницы
    for page in range(1511, 3500):
        req = requests.get(f'{url}={page}', headers=headers)
        soup = bs(req.text, 'lxml')

        all_href = []

        # Ищем ссылки на рецепты на текущей странице
        all_elements = soup.find_all('a', 'emotion-18hxz5k')

        for element in all_elements:
            href = f'https://eda.ru{element.get("href")}'
            all_href.append(href)

        # Обрабатываем каждую ссылку на рецепт
        for href in all_href:
            req = requests.get(href, headers=headers)
            soup = bs(req.text, 'lxml')
            name = soup.find('h1', 'emotion-gl52ge').text
            country = soup.find_all('span', 'emotion-1h6i17m')[2].text

            # Добавляем данные о рецепте в список
            name = name.replace(' ', ' ')
            big_classter = ''
            if country == 'Грузинская кухня' or country == 'Армянская кухня' or country == 'Азербайджанская кухня' or country == 'Дагестанская кухня' or country == 'Осетинская кухня' or country == 'Чеченская кухня' or country == 'Кавказская кухня':
                big_classter = 'Кавказская кухня'
            elif country == 'Ирландская кухня' or country == 'Югославская кухня' or country == 'Швейцарская кухня' or country == 'Болгарская кухня' or country == 'Бельгийская кухня' or country == 'Шотландская кухня' or country == 'Европейская кухня' or country == 'Французская кухня' or country == 'Немецкая кухня' or country == 'Португальская кухня' or country == 'Польская кухня' or country == 'Британская кухня' or country == 'Австрийская кухня' or country == 'Финская кухня' or country == 'Сербская кухня' or country == 'Венгерская кухня' or country == 'Чешская кухня' or country == 'Скандинавская кухня' or country == 'Голландская кухня' or country == 'Румынская кухня' or country == 'Молдавская кухня' or country == 'Хорватская кухня' or country == 'Словецкая кухня' or country == 'Эстонская кухня' or country == 'Латвийская кухня' or country == 'Литовская кухня' or country == 'Черногорская кухня' or country == 'Мальтийская кухня':
                big_classter = 'Европейская кухня'
            elif country == 'Китайская кухня' or country == 'Японская кухня' or country == 'Индийская кухня' or country == 'Корейская кухня' or country == 'Тайская кухня' or country == 'Вьетнамская кухня' or country == 'Индонезийская кухня' or country == 'Сингапурская кухня' or country == 'Филиппинская кухня' or country == 'Камбоджийская кухня' or country == 'Паназиатская кухня' or country == 'Мировая кухня' or country == 'Раджастанская кухня' or country == 'Пенджабская кухня' or country == 'Вовосточно-индийская кухня' or country == 'Северно-индийская кухня' or country == 'Южно-индийская кухня':
                big_classter = 'Азиатская кухня'

            elif country == 'Австралийская кухня' or country == 'Средиземноморская кухня' or country == 'Итальянская кухня' or country == 'Испанская кухня' or country == 'Греческая кухня' or country == 'Турецкая кухня' or country == 'Марокканская кухня' or country == 'Египетская кухня' or country == 'Ливанская кухня' or country == 'Сирийская кухня' or country == 'Каталонская кухня' or country == 'Сицилийская кухня' or country == 'Кипрская кухня':
                big_classter = 'Средиземноморская кухня'

            elif country == 'Канадская кухня' or country == 'Креольская кухня' or country == 'Американская кухня' or country == 'Латиноамериканская кухня' or country == 'Мексиканская кухня' or country == 'Перуанская кухня' or country == 'Колумбийская кухня' or country == 'Кубинская кухня' or country == 'Бразильская кухня' or country == 'Аргентинская кухня':
                big_classter = 'Латиноамериканская кухня'

            elif country == 'Персидская кухня' or country == 'Восточно-индийская кухня' or country == 'Малайзийская кухня' or country == 'Еврейская кухня' or country == 'Арабская кухня' or country == 'Афганская кухня' or country == 'Албанская кухня' or country == 'Алжирская кухня' or country == 'Тунисская кухня' or country == 'Йеменская кухня':
                big_classter = 'Восточная кухня'

            elif country == 'Узбекская кухня' or country == 'Туркменская кухня' or country == 'Казахская кухня' or country == 'Киргизская кухня':
                big_classter = 'Среднеазиатская кухня'

            elif country == 'Татарская кухня' or country == 'Башкирская кухня':
                big_classter = 'Татарская кухня'

            elif country == 'Одесская кухня' or country == 'Советская кухня' or country == 'Русская кухня' or country == 'Украинская кухня' or country == 'Белорусская кухня':
                big_classter = 'Славянская кухня'

            elif country == 'Исландская кухня' or country == 'Норвежская кухня' or country == 'Датская кухня' or country == 'Шведская кухня':
                big_classter = 'Скандинавская кухня'

            elif country == 'Кухня Вестероса' or country == 'Пошаговые рецепты' or country == 'Авторская кухня' or country == 'Молекулярная кухня' or country == 'Фьюжн кухня':
                big_classter = 'Авторская кухня'
            else:
                big_classter = 'Авторская кухня'
            data_list.append(
                {
                    'Dish': name.strip(),
                    'Cuisine': country,
                    'Claster': big_classter
                }
            )

            # Сохраняем данные в JSON-файл
            with open('ddd.json', 'w', encoding='utf-8') as f:
                json.dump(data_list, f, indent=4, ensure_ascii=False)

        if total == 0:
            print('Сбор данных завершён')
        else:
            print(f'Информация со страницы {page} обработана')
            total -= 1
        time.sleep(0.5)


# Функция для запуска парсера
def main():
    get_data('https://eda.ru/recepty?page')


# Запуск парсера при выполнении скрипта напрямую
if __name__ == '__main__':
    kitchens = ['Итальянская кухня', 'Грузинская кухня', 'Китайская кухня', 'Французская кухня', 'Русская кухня',
                'Японская кухня', 'Индийская кухня', 'Мексиканская кухня', 'Армянская кухня', 'Американская кухня',
                'Испанская кухня', 'Немецкая кухня', 'Греческая кухня', 'Азербайджанская кухня', 'Европейская кухня',
                'Еврейская кухня', 'Корейская кухня', 'Тайская кухня', 'Паназиатская кухня', 'Турецкая кухня',
                'Узбекская кухня', 'Татарская кухня', 'Средиземноморская кухня', 'Арабская кухня', 'Украинская кухня',
                'Польская кухня', 'Британская кухня', 'Белорусская кухня', 'Норвежская кухня', 'Шведская кухня',
                'Марокканская кухня', 'Болгарская кухня', 'Австрийская кухня', 'Австралийская кухня', 'Финская кухня',
                'Сербская кухня', 'Венгерская кухня', 'Вьетнамская кухня', 'Молдавская кухня', 'Осетинская кухня',
                'Канадская кухня', 'Алжирская кухня', 'Дагестанская кухня', 'Албанская кухня', 'Мировая кухня',
                'Мальтийская кухня', 'Каталонская кухня', 'Туркменская кухня', 'Афганская кухня', 'Египетская кухня',
                'Крымская кухня', 'Раджастанская кухня', 'Африканская кухня', 'Филиппинская кухня', 'Шотландская кухня',
                'Сирийская кухня', 'Таджикская кухня', 'Португальская кухня', 'Латиноамериканская кухня',
                'Латвийская кухня', 'Индонезийская кухня', 'Датская кухня', 'Бурятская кухня', 'Кавказская кухня',
                'Колумбийская кухня', 'Креольская кухня', 'Сицилийская кухня', 'Советская кухня', 'Черногорская кухня',
                'Камбоджийская кухня', 'Казахская кухня', 'Чеченская кухня', 'Северно-индийская кухня',
                'Южно-индийская кухня', 'Скандинавская кухня', 'Бразильская кухня', 'Кухня Вестероса',
                'Перуанская кухня', 'Голландская кухня', 'Чешская кухня', 'Литовская кухня', 'Ливанская кухня',
                'Кубинская кухня', 'Киргизская кухня', 'Башкирская кухня', 'Исландская кухня', 'Швейцарская кухня',
                'Абхазская кухня', 'Хорватская кухня', 'Кипрская кухня', 'Румынская кухня', 'Персидская кухня',
                'Сингапурская кухня', 'Пакистанская кухня', 'Черкесская кухня', 'Пенджабская кухня',
                'Восточно-индийская кухня', 'Одесская кухня', 'Малайзийская кухня', 'Ирландская кухня',
                'Авторская кухня', 'Югославская кухня', 'Эстонская кухня', 'Карибская кухня', 'Бельгийская кухня',
                'Аргентинская кухня']

    main()
# до 1511