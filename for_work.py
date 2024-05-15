import joblib
import pandas as pd

# Загрузка модели из файла
loaded_model = joblib.load('my_cuisine_classifier_test3.pkl')

new_dish = 'паста'

data = pd.read_excel('DataTable.xlsx')

vectorizer = joblib.load('vectorizer.joblib')
cluster_vectoriz = joblib.load('cluster_vectoriz.joblib')
new_dish_vectorized = vectorizer.transform([new_dish])
prediction = loaded_model.predict(new_dish_vectorized)
print('Кухня нового блюда:', cluster_vectoriz.inverse_transform([prediction[0]]))
