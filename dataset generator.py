import random
import csv
from russian_names import RussianNames

groups = []
for i in range(50, 71):
    groups.append(i)

specializations = [
    'Информатика и вычислительная техника', 
    'Прикладная информатика (по отраслям)', 
    'Сетевое и системное администрирование', 
    'Информационные системы и программирование',
    'Электроника, радиотехника и системы связи',
    'Электронные приборы и устройства',
    'Электро- и теплоэнергетика',
    'Теплоснабжение и теплотехническое оборудование',
    'Техническая эксплуатация и обслуживание электрического и электромеханического оборудования (по отраслям)',
    'Технологии материалов',
    'Сварочное производство',
    'Техника и технологии наземного транспорта',
    'Организация перевозок и управление на транспорте (по видам)',
    'Техническое обслуживание и ремонт автомобильного транспорта',
    'Техническое обслуживание и ремонт двигателей, систем и агрегатов автомобилей',
    'Юриспруденция',
    'Право и организация социального обеспечения',
    'Сервис и туризм',
    'Технология парикмахерского искусства',
    'История и археология',
    'Документационное обеспечение управления и архивоведение',
    'Изобразительные и прикладные виды искусств',
    'Дизайн (по отраслям)',
]

def generate_gender():
    genders = ['мужской', 'мужской', 'женский']
    return random.choice(genders)

def generate_graduation_date():
    return f"{random.randint(1, 30)}.{random.randint(1, 12)}.{random.randint(2000, 2006)}"

def generate_specialization():
    return f"{random.choice(specializations)}"

def generate_group():
    return f"{random.choice(groups)}"

dataset = [['Id', 'Пол', 'ФИО', 'Дата окончания обучения', 'Группа', 'Специальность', 'Работает по специальности']]
for id in range(2000):
    gender = generate_gender()
    name = RussianNames().get_person(gender = 1 if gender == 'мужской' else 0)
    graduation_date = generate_graduation_date()
    group = generate_group()
    specialization = generate_specialization()
    dataset.append([id, gender, name, graduation_date, group, specialization, random.choice([True, False, False])])

with open("dataset.csv","w+", encoding="utf-8", newline="") as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=',')
    csvWriter.writerows(dataset)