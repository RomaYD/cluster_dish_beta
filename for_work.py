import joblib
import pandas as pd
import tkinter as tk
import random
import difflib
from tkinter import messagebox

def similarity(word1, word2):
    seq = difflib.SequenceMatcher(None, word1, word2)
    similarity_ratio = seq.ratio()
    return similarity_ratio

# Загрузка модели из файла
loaded_model = joblib.load('my_cuisine_classifier_test3.pkl')

data = pd.read_excel('DataTable.xlsx')

vectorizer = joblib.load('vectorizer.joblib')
cluster_vectoriz = joblib.load('cluster_vectoriz.joblib')

def return_kitchen_by_dish(dish, vectorizer, model, cluster_vectorizer):
    new_dish_vectorized = vectorizer.transform([dish])
    prediction = model.predict(new_dish_vectorized)
    return cluster_vectorizer.inverse_transform([prediction[0]])[0]

# Интерфейс

titles_for_happy_path_result = ['Умница, ты думаешь как искусственный интеллект', 
                                'Никогда не думал, что в опозанании откуда хинкали у меня появится соперник', 
                                'Пора бы уже перекусить этим блюдом, а то только сидим и угадываем']
titles_for_unhappy_path_result = ['Попробуй ещё раз, если что я считаю, что это ', 
                                  'Может быть я не права, но вот мой ответ на ваше блюдо ', 
                                  'Завтра поедем в ресторан и узнаем у официанта, но пока что это ']

root = tk.Tk()
root.title("Проверка принадлежности блюда к кухне")
# Установка размера окна
root.geometry("400x300")

# Функция для кнопки
def on_button_click():
    dish_input = entry1.get()
    kitchen_input = entry2.get()
    if len(dish_input) == 0:
        messagebox.showerror("Ошибка", "Не хватает названия блюда")
    elif len(kitchen_input) == 0:
        messagebox.showerror("Ошибка", "Не хватает названия кухни")
    else:
        kitchen_by_neuro = return_kitchen_by_dish(dish_input, vectorizer, loaded_model, cluster_vectoriz)

        similarity_kitchens = similarity(kitchen_by_neuro.split()[0], kitchen_input.split()[0])

        if similarity_kitchens >= 0.8:
            random_index = random.randint(0, len(titles_for_happy_path_result))
            messagebox.showinfo("Ура, вы угадали", titles_for_happy_path_result[random_index])
        else:
            random_index = random.randint(0, len(titles_for_happy_path_result))
            messagebox.showinfo("К сожалению мы считаем иначе(", titles_for_unhappy_path_result[random_index] + kitchen_by_neuro)



entry1 = tk.Entry(root, fg="blue", bg="lightgray", font=("Helvetica", 20), justify="center", width=30)
entry1.pack(fill='x')

entry2 = tk.Entry(root, fg="blue", bg="lightgray", font=("Helvetica", 20), justify="center", width=30)
entry2.pack(fill='x')

button = tk.Button(root, text="Проверить блюдо на принадлежность к кухне", command=on_button_click, justify="center")
button.pack(fill='x')


# Запускаем главный цикл окна
root.mainloop()
