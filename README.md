# DigitalEdu_analysis
A mathematical model that will predict the purchase of a course by a user of the DigitalEdu portal. The task was completed in python using the pandas, sklearn libraries


DigitalEdu provides data from its website about registered users who have been served ads and who have or have not purchased a course. Based on this data, you need to build and train a model

Data DigitalEdu_data.csv
id - the unique identifier of the user.
sex - gender (0 = not specified, 1 = female, 2 = male).
bdate - date of birth.
has_photo - Whether a profile photo is set (0 = not set, 1 = set).
has_mobile - whether the phone number is known (0 = not known, 1 = known).
city - city.
followers_count - number of followers.
graduation — graduation year.
education_form - the form of education.
relation - marital status (1 - not married / not married;
2 - have a friend / have a girlfriend; 3 - engaged / engaged;
4 - married / married; 5 - everything is difficult;
6 — in active search; 7 - in love / in love;
8 - in a civil marriage; 0 - not specified).
education_status - education status.
langs - a list of languages that the user speaks.
last_seen - the time of the last visit.
occupation_type - user's current occupation (school, university, work).
occupation_name - the name of the organization.
life_main - the main thing in life. (1 - family and children; 2 - career and money;
  3 - entertainment and recreation; 4 - science and research;
  5 - improvement of the world; 6 - self-development;
  7 - beauty and art; 8 - fame and influence).
people_main - the main thing in people. (1 - mind and creativity;
  2 - kindness and honesty; 3 - beauty and health;
  4 - power and wealth; 5 - courage and perseverance;
  6 - humor and love of life).
career_start - the year the job started.
career_end - the year the job ended.
result - whether the user has purchased a programming course
(0 - no, 1 - yes).
