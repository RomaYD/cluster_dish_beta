import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
# Загрузка модели из файла
loaded_model = joblib.load('my_cuisine_classifier_test3.pkl')

new_dish = 'паста'

data = pd.read_excel('DataTable.xlsx')

vectorizer = CountVectorizer()
learning_wordtovec = vectorizer.fit_transform(data['Dish'])
cluster_vectoriz = LabelEncoder()
cluster = cluster_vectoriz.fit_transform(data['Claster'])
new_dish_vectorized = vectorizer.transform([new_dish])
prediction = loaded_model.predict(new_dish_vectorized)
print('Кухня нового блюда:', cluster_vectoriz.inverse_transform([prediction[0]]))
