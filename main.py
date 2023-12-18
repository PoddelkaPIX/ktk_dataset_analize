import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('dataset.csv')
df = pd.DataFrame(dataset)

df['Дата окончания обучения'] = pd.to_datetime(df['Дата окончания обучения'], format='%d.%m.%Y')

# Посчитаем средний возраст окончания обучения
mean_year = df['Дата окончания обучения'].dt.year.mean()

# Выведем результат
print(f"Средний год окончания обучения: {mean_year}")

# 3. Получить общую информацию о данных, включая типы данных и наличие пропущенных значений: 
df.info()
# 4. Посчитать основные статистические показатели для числовых столбцов: 
df.describe()
# 5. Посчитать количество уникальных значений в каждом столбце: 
df.nunique()
# 6. Проверить наличие пропущенных значений в данных: 
df.isnull().sum()
# 7. Посчитать среднее значение по числовым столбцам: 
df.mean()
# 8. Посчитать медиану по числовым столбцам: 
df.median()
# 9. Посчитать моду по каждому столбцу: 
df.mode()
# 10. Посчитать корреляцию между числовыми столбцами: 
df.corr()
# 11. Построить гистограмму для числового столбца: 
df['Группа'].plot(kind='hist')
plt.show()
# 12. Построить круговую диаграмму для категориального столбца: 
df['Пол'].value_counts().plot(kind='pie')
plt.show()
# 13. Посчитать количество записей для каждого значения в категориальном столбце: 
df['Специальность'].value_counts()
# 14. Проверить соответствие условию для фильтрации данных: 
df[df['Работает по специальности'] == True]
# 15. Выполнить группировку данных и провести агрегацию: 
df.groupby('Пол').mean()