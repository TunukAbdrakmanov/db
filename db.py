# база данных - данные, структурированные определенным образом 

# СУБД - набор инструментов для работы с БД

# SQL (Structured Query Language) - язык запросов в БД 

# типы данных POSTGRESQL 

# числа - целые
# SMALLINT(INT2) #2 байта
# -32768 до 32767 (2 ** 15)

# INTEGER(INT, INT4) #4 байта
# -2_147_483_648 до +2_147_483_647 (2 ** 31)

# BIGINT(INT8) #8 байта
# -9_223_372_036_854_775_808 до +9_223_372_036_854_775_807 (2 ** 63)

#         float
# real    (4 байта)
# точность до 6 знаков 

# double precision (8 байта)
# точность до 15 знаков

#         Decimal
# DECIMAL 
# NUMERIC

# 121072 знаков до запятой, 16383 после запятой

# SERIAL - целые числа с автоприбавлением
# SMALLSERIAL 1...32767
# SERIAL      1...2_147_483_647
# BIGSERIAL   1...9_223_372_036_854_775_807

# # строки
# CHAR(n) - строка с постоянной длиной 
# CHAR(10)
# test -> 'test    '

# VARCHAR(n) - строка с максимальной длиной
# VARCHAR(10)
# test -> 'test'

# TEXT - строка неограниченной длины


# bool(1 байт)
# 't', 'f'
# 1, 0
# 'on', 'off'
# 'yes', 'no'
# 'true', 'false'

# None 
# NULL 
# DATA TIME 
# DATA (дата)
# TIME (время)
# TIMESTAMP (дата и время)

# ограничения (CONSTRAINTS)

# DEFAULT - значение по умолчанию 
# NULL/NOT NULL - будет ли поле(столбец) обязательным или нет, может ли столбец содержать
# пустое значение
# UNIQUE - должны ли значение в столбце на определенное условие 
# CHECK - проверяет значение в столбце на определенное условие
# PRIMARY KEY - определяет какое поле будет ключом 
# FOREIGN KEY - определяет, какое поле ссылается на другую таблицу 

# создать БД
# CREATE DATABASE <название>

# удаление БД
# DROP DATABASE <название>;

# проверить список БД
# \l (PSQL) 
# SHOW DATABASES; (MySQL)

# соединение с БД
# \c <название БД>

# создание таблицы
# CREAT TABLE <название> (столбец тип ограничение, столбец2 тип ограничение, ...) 

# удаление таблицы
# DROP TABLE <название>;

# обновление таблицы
# (переименование таблицы, переименование столбцов, добавление, удаление столбца,
#  изменение типа столбца, изменение ограничений столбца)

# ALTER TABLE

# переименование таблицы
# ALTER TABLE <название> RENAME TO <новое название>;

# переименование столбца
# ALTER TABLE <название таблицы> RENAME COLUMN <название столбца> TO <новое название>;

# удаление столбца
# ALTER TABLE <название таблицы> DROP COLUMN <название столбца>;
# AlTER TABLE student DROP COLUMN date_of_birth;

# добавление столбца
# ALTER TABLE <название таблицы> ADD COLUMN <название столбца> <тип столбца> <ограничения>;
# ALTER TABLE student ADD COLUMN age SMALLINT NOT NULL;

# изменить тип столбца
# ALTER TABLE <название таблицы> ALTER COLUMN <название столбца> TYPE <новый тип>;
# ALTER TABLE student ALTER COLUMN name TYPE VARCHAR(30);

# добавление ограничений
# NULL| NOT NULL
# указать NOT NULL
# ALTER TABLE <название таблицы> ALTER COLUMN <название столбца> SET NOT NULL;

# указать как NULL
# ALTER TABLE <название таблицы> ALTER COLUMN <название столбца> DROP NOT NULL;

# задать DEFAULT
# ALTER TABLE <название таблицы> ALTER COLUMN <название столбца> SET DEFAULT <значение>;

# убрать DEFAULT
# ALTER TABLE <название таблицы> ALTER COLUMN <название столбца> DROP DEFAULT;

# добавление ограничений
# ALTER TABLE <название таблицы> ADD <ограничение>;
# ALTER TABLE student ADD CHECK(age >= 16);

# ALTER TABLE <название таблицы> ADD CONSTRAINT <название ограничения> <ограничение>
# ALTER TABLE student ADD CONSTRAINT check age CHECK(age >= 16);

# удаление ограничений
# ALTER TABLE student DROP CONSTRAINT <название ограничения>;
# ALTER TABLE student DROP CONSTRAINT age_check;



import schedule
import requests


def greeting():
    """Greeting function"""
    
    todos_dict = {
        '08:00': 'Drink coffee',
        '11:00': 'Work meeting',
        '23:59': 'Hack the Planet!'
    }
    
    print("Day's tasks")
    for k, v in todos_dict.items():
        print(f'{k} - {v}')
        
    response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
    data = response.json()
    btc_price = f"BTC: {round(data.get('btc_usd').get('last'), 2)}$\n"
    
    print(btc_price)
        
        
def main():
    
    schedule.every(4).seconds.do(greeting)
    schedule.every(5).minutes.do(greeting)
    schedule.every().hour.do(greeting)
    schedule.every().day.at('21:51').do(greeting)
    schedule.every().thursday.do(greeting)
    schedule.every().friday.at('23:45').do(greeting)
    
    while True:
        schedule.run_pending()
    
    
if __name__ == '__main__':
    main()