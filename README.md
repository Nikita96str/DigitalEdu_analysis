# DigitalEdu_analysis
Математическая модель, которая будет предсказывать покупку курса пользователем портала DigitalEdu. Задание выполнено на языке python с помощью библиотек pandas, sklearn


DigitalEdu предоставляет данные со своего сайта о зарегистрированных пользователях, которым рассылалась реклама и которые купили или не купили курс. На основе этих данных нужно построить и обучить модель

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

