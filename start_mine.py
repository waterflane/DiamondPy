import minecraft_launcher_lib as mll
import subprocess
import requests
import os
import webbrowser

# read_settings() - вспомогательная функция, возращает лист с данными файла(построчно)
# first_launch() - первый запуск, настраивает файл SettingInfo, возращает 1 когда завершится
# settings() - меняет настройки в файле SettingInfo, подавать значения которые нужно изменить, возращает 1 когда завершится
# ely_by_auth() - принимает логин и пароль от системы ely, если все правильно то функция запишет в файл SettingInfo UUID и поменяет use_api? на True(поменяет режим на онлайн)
#   Ошибки: вернет 'требуется TOPT токен', если на аккаунте ely включена двухфакторная аутентификация
#           вернет 'ошибка при входе', если сайт вернул не 200
# start() - запускает майнкрафт поданой версии, если версии нет то установит, возращает 1 когда завершится
# def download_version() - скачивает версии поданной версии и ядра(пока только ванила)


# Для SettingInfo.txt:
#     1 - директория майна
#     2 - ник
#     3 - uuid
#     4 - use api?  

def read_settings():
    file = open("resource/data/SettingInfo", "r")
    Nl = file.readlines()
    for i in range(len(Nl)):
        Nl[i] = Nl[i].replace('\n', '')
        Nl[i] = Nl[i].replace('\\', '/')
    return Nl

def first_launch(system_launch, login_if_ely=None, pass_if_ely=None, username_if_offline='Player'):
    minecraft_directory = mll.utils.get_minecraft_directory()

    file = open("resource/data/SettingInfo", "w") 
    #-----------------дирректория------------------ник----------uuid---use uuid 
    file.write(f'{minecraft_directory}\n{username_if_offline}\n{None}\n{False}')

    if system_launch == 'ely':
        ely_by_auth(login_if_ely, pass_if_ely)
    return 1




def settings(new_dir=None, new_username=None, new_uuid=None, use_uuid=None):
    dir, username, uuid, uuid_use = read_settings()
    file = open("resource/data/SettingInfo", "w") 
    file.write(f'{dir if new_dir == None else new_dir}\n{username if new_username == None else new_username}\n{uuid if new_uuid == None else new_uuid}\n{uuid_use if use_uuid == None else use_uuid}')
    return 1

def ely_by_auth(login=None, passw=None, TOTP=None):
    if login == None or passw == None:
        webbrowser.open("https://account.ely.by/register")
    elif TOTP != None:
        auth_url = f"https://authserver.ely.by/auth/authenticate"

        auth_data = {
            "username": login,
            "password": f'{passw}:{TOTP}'
        }
        response = requests.post(auth_url, json=auth_data)
            
        uuid = response.json()['selectedProfile']['id']
        settings(new_uuid=uuid, use_uuid=True)
        
    else:
        auth_url = f"https://authserver.ely.by/auth/authenticate"

        auth_data = {
            "username": login,
            "password": passw
        }
        response = requests.post(auth_url, json=auth_data)

        if response.status_code == 401: return 'требуется TOPT токен'
        if response.status_code != 200: return 'ошибка при входе'
            
        uuid = response.json()['selectedProfile']['id']
        settings(new_username=response.json()['selectedProfile']['name'], new_uuid=uuid, use_uuid=True)




def start(version):
    dir, username, uuid, uuid_use = read_settings()
    options = {
        'username': username,
        'uuid': uuid if uuid_use == 'True' else ''
    }
    try:
        subprocess.call(mll.command.get_minecraft_command(version=version, minecraft_directory=dir, options=options))
    except mll.exceptions.VersionNotFound:
        download_version(version)
        subprocess.call(mll.command.get_minecraft_command(version=version, minecraft_directory=dir, options=options))
    return 1
    

def download_version(version='1.21.4', core='vanila'):
    dir, username, uuid, uuid_use = read_settings()

    if core == 'vanila':
        print('начало загрузки')
        mll.install.install_minecraft_version(versionid=version, minecraft_directory=dir)
        print('успешно')
    return 1

    

def download_version(version='1.21.4', core='vanila'):
    max_value = [0]
    dir, username, uuid = read_settings()

    if core == 'vanila':
        print('начало загрузки')
        mll.install.install_minecraft_version(versionid=version, minecraft_directory=dir)
        print('успешно')

# first_launch('ely')
