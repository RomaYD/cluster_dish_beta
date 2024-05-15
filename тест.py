import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer

data = pd.read_excel('DataTable.xlsx')

vectorizer = CountVectorizer()
# vectorizer = CountVectorizer(analyzer='char')
# vectorizer = CountVectorizer(analyzer='char_wb')
learning_wordtovec = vectorizer.fit_transform(data['Dish'])

cluster_vectoriz = LabelEncoder()
cluster = cluster_vectoriz.fit_transform(data['Claster'])

# Разделение данных
word_train, word_test, cluster_train, cluster_test = train_test_split(learning_wordtovec, cluster, test_size=0.1, random_state=42)

# Создание и обучение модели
model = MLPClassifier(hidden_layer_sizes=(128), activation='tanh', solver='adam', max_iter=5, early_stopping=True, verbose=True)
model.fit(word_train, cluster_train)

# Оценка производительности
score = model.score(word_test, cluster_test)
print('Точность модели:', score)

# Сохранение модели
joblib.dump(model, 'my_cuisine_classifier_test4.pkl')

