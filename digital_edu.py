# DigitalEdu предоставляет данные со своего сайта о зарегистрированных пользователях, которым рассылалась реклама 
# и которые купили или не купили курс. На основе этих данных нужно будет построить и обучить модель
'''
Данные DigitalEdu_data.csv
id — уникальный идентификатор пользователя.
sex — пол (0 = не указан, 1 = женский, 2 = мужской).
bdate — дата рождения.
has_photo — установлено ли фото профиля (0 = не установлено, 1 = установлено).
has_mobile — известен ли номер телефона (0 = не известен, 1 = известен).
city — город.
followers_count — количество подписчиков.
graduation — год окончания обучения.
education_form — форма обучения.
relation — семейное положение (1 — не женат/не замужем; 
2 — есть друг/есть подруга; 3 — помолвлен/помолвлена; 
4 — женат/замужем; 5 — всё сложно;
6 — в активном поиске; 7 — влюблён/влюблена; 
8 — в гражданском браке; 0 — не указано).
education_status — статус обучения.
langs — список языков, которыми владеет пользователь.
last_seen — время последнего посещения.
occupation_type — текущее занятие пользователя (школа, университет, работа).
occupation_name — название организации.
life_main — главное в жизни. (1 — семья и дети; 2 — карьера и деньги;
 3 — развлечения и отдых; 4 — наука и исследования;
 5 — совершенствование мира; 6 — саморазвитие;
 7 — красота и искусство; 8 — слава и влияние).
people_main — главное в людях. (1 — ум и креативность; 
 2 — доброта и честность; 3 — красота и здоровье; 
 4 — власть и богатство; 5 — смелость и упорство;
 6 — юмор и жизнелюбие).
career_start — год начала работы.
career_end — год окончания работы.
result — приобрёл ли пользователь курс по программированию
(0 — нет, 1 — да).
'''

import pandas as pd
df = pd.read_csv('DigitalEdu_data.csv')

# print(df.info())
# print(df.head())

group_df = df.groupby(by = ['result', 'sex'])['graduation'].agg('mean')
pt_df = df.pivot_table(index = 'result', columns = 'sex', values = 'graduation', aggfunc = ('min', 'mean', 'max'))
#print(group_df)

# !преобраззовать столбцы в численный тип данных
#print(df['bdate'].value_counts())

# Преобразуем значения столбца df['bdate'] в день рождения по году 
def day_of_birth(date):
    year_months = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    leap_year_months = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    date = str(date).lower()
    if date != 'nan':
        date_list = list(map(int, date.split('.')))
        try:
            if date_list[2] % 4 != 0:
                date = date_list[0] + year_months[date_list[1] - 1]
            else:
                date = date_list[0] + leap_year_months[date_list[1] - 1]
        except:
            date = date_list[0] + year_months[date_list[1] - 1]
    return date
df['bdate'] = df['bdate'].apply(day_of_birth)
# print(df['bdate'])
# print(df['bdate'].value_counts())

global sum_date 
global count_date
sum_date, count_date = 0, 0

# Вычисляем среднюю дату рождения
def average_date_func(date):
    global sum_date 
    global count_date
    date = str(date).lower()
    if date != 'nan':
        sum_date += int(date)
        count_date += 1

df['bdate'].apply(average_date_func)
#print(sum_date, count_date)
global average_date
average_date = int(sum_date/count_date)

#Присваиваем к NaN средний день рождения
def no_NaN_func(date):
    global average_date
    if str(date).lower() == 'nan':
        return average_date
    return date
df['bdate'] = df['bdate'].apply(no_NaN_func)

# print(df['bdate'])
# print('почему то разные элементы повторяются в разных наборах', df['bdate'].value_counts())


# Преобразовываем в int значение столбца education_status
#print(df['education_status'].value_counts())
def education_int(status):
    if status == 'None':
        return 0
    elif status == 'Undergraduate applicant':
        return 1
    elif status == "Student (Bachelor's)":
        return 2
    elif status == "Alumnus (Bachelor's)":
        return 3
    elif status == "Student (Specialist)":
        return 4
    elif status == "Alumnus (Specialist)":
        return 5
    elif status == "Student (Master's)":
        return 6    
    elif status == "Alumnus (Master's)":
        return 7
    elif status == "Candidate of Sciences":
        return 8
    elif status == "PhD":
        return 9

df['education_status'] = df['education_status'].apply(education_int)
# print(df['education_status'].value_counts())

#Преобразуем в числа значения столбца education_form
# print(df['education_form'].value_counts())
def education_form_func(type):
    if type == 'Full-time':
        return 3
    elif type == 'Distance Learning':
        return 2
    elif type == 'Part-time':
        return 1
    else:
        return 0
df['education_form'] = df['education_form'].apply(education_form_func)

# Преобразуем столбцы langs, life_main в число
# print(df['langs'].value_counts())
def langs_func(langs):
    amount = len(langs.split(';'))
    return amount
df['langs'] = df['langs'].apply(langs_func)    

def int_convert_func(value):
    if value == 'False':
        value = 0
    return int(value)
df['life_main'] = df['life_main'].apply(int_convert_func)  
df['people_main'] = df['people_main'].apply(int_convert_func)  

# Преобразуем значения столбца city в число
cities = set(df['city'].tolist())

list_cities = list(cities)
global dict_cities
dict_cities = dict()
for index in range(len(list_cities)):
    dict_cities[list_cities[index]] = index + 1

def city_toint_func(city):
    return dict_cities[city]

df['city'] = df['city'].apply(city_toint_func)
# print(df['city'])

# Преобразуем значения столбца last_seen в число
def last_seen_func(visit):
    example = '2020-08-19'
    visit_day = len(example)
    try:
        visit = visit[:]
        return int(visit[:visit_day].replace('-', ''))
    except:
        return 0
df['last_seen'] = df['last_seen'].apply(last_seen_func)
# print(df['last_seen'].value_counts())

# Преобразуем значения столбца occupation_type в число
def occupation_type_func(occupation):
    if occupation == 'university':
        return 1
    elif occupation == 'work':
        return 2
    else:
        return 0
df['occupation_type'] = df['occupation_type'].apply(occupation_type_func)

# Преобразуем значения столбца occupation_name в число
list_places = list(set(df['occupation_name'].tolist()))

global dict_places
dict_places = dict()
for index in range(len(list_places)):
    dict_places[list_places[index]] = index + 1

def occupation_name_func(name):
    return dict_places[name]

df['occupation_name'] = df['occupation_name'].apply(occupation_name_func)

# Преобразуем значения столбца career_start в число
def career_func(year):
    try:
        return int(year)
    except:
        return 0
df['career_start'] = df['career_start'].apply(career_func)
df['career_end'] = df['career_end'].apply(career_func)

# print(df['career_start'].value_counts())

# print(df.info())
# print(df.head())

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

x = df.drop('result', axis = 1)
y = df['result']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

classifier = KNeighborsClassifier(n_neighbors = 4)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

pred_percent = accuracy_score(y_test, y_pred) * 100
print('Точность модели:', pred_percent, '(%)')