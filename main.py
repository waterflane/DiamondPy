 #* Это файл "путеводитель" при запуске он будет направлять либо на first_setup либо на launcher_main. 
import os
import flet as ft
import logging
# launcher_main.main_launcher()
logging.basicConfig(
    filename='resource\launcher_data\logs\logs.log',
    filemode='w',
    level=logging.INFO,
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.debug('Проект загружен!')
logging.info('Проверка наличия файла "tutotial"')
try:
    temp_tutorial = open('resource/launcher_data/settings/tutorial.txt', "r")
    logging.info('Файл "tutotial" Найден!')
    a = temp_tutorial.read()
    print(a)
    logging.debug('Проверка прохождения туториала...')
    if a == 'tutorial completed':
        temp_tutorial.close()
        logging.info('Туториал пройден, запуск лаунчера')
        os.system('launcher_main.py')
    else:
        temp_tutorial.close()
        logging.debug('Туториал не пройден! Запуск туториала!')
        os.system('first_setup.py')
except FileNotFoundError:
    logging.info('Файл "tutorial" Не найден!')
    logging.info('Запуск туториала!')
    os.system('first_setup.py')