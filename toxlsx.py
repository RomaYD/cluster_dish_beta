import pandas as pd
import json

# Ваши данные в формате JSON

# Конвертация JSON строки в список словарей
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Создание DataFrame из списка
df = pd.DataFrame(data)

# Сохранение DataFrame в файл Excel
df.to_excel('DataTable.xlsx', index=False)