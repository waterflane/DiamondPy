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
# def download_version() - скачивает версии поданной версии и ядра, вернет: 1 если успешно установдена, 2 если уже установлена


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
    if not os.path.exists('.minecraft'):
        os.makedirs('.minecraft')
    minecraft_directory = '.minecraft'

    file = open("resource/data/SettingInfo", "w") 
    #-----------------дирректория------------------ник----------uuid---use uuid 
    file.write(f'{minecraft_directory}\n{username_if_offline}\n{None}\n{False}')
    file.close()

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




def start(version, core='vanila'):
    dir, username, uuid, uuid_use = read_settings()
    options = {
        'username': username,
        'uuid': uuid if uuid_use == 'True' else ''
    }
    if core == 'vanila':
        try:
            subprocess.call(mll.command.get_minecraft_command(version=version, minecraft_directory=dir, options=options))
        except mll.exceptions.VersionNotFound:
            download_version(version)
            subprocess.call(mll.command.get_minecraft_command(version=version, minecraft_directory=dir, options=options))
        return 1
    elif core == 'forge':
        installed_versions = mll.utils.get_installed_versions(dir)
        forge_version = ''

        for i in installed_versions:
            if version in i['id'] and '-forge-' in i['id']:
                forge_version = i['id']
                break

        if forge_version == '':
            download_version(version, 'forge')
            for i in installed_versions:
                if version in i['id'] and '-forge-' in i['id']:
                    forge_version = i['id']
                    break
            subprocess.call(mll.command.get_minecraft_command(forge_version, dir, options))

        subprocess.call(mll.command.get_minecraft_command(forge_version, dir, options))
    elif core == 'fabric':
        installed_versions = mll.utils.get_installed_versions(dir)
        fabric_loader_version = mll.fabric.get_latest_loader_version()
        print(installed_versions)

        fabric_version_name = f"fabric-loader-{fabric_loader_version}-{version}"

        fabric_installed = any(i["type"] == "fabric" and version in i["id"] for i in installed_versions)
        if fabric_installed == True:
            subprocess.call(mll.command.get_minecraft_command(fabric_version_name, dir, options))
        else:
            print(download_version(version, 'fabric'))

            fabric_version_name = f"fabric-loader-{fabric_loader_version}-{version}"
            subprocess.call(mll.command.get_minecraft_command(fabric_version_name, dir, options))

def download_version(version='1.20.1', core='vanila'):
    dir, username, uuid, uuid_use = read_settings()

    if core == 'vanila':
        installed_versions = mll.utils.get_installed_versions(dir)
        for i in installed_versions:
            if i['id'] == version:
                return 2
            
        print('начало загрузки')

        mll.install.install_minecraft_version(versionid=version, minecraft_directory=dir)

        print('успешно')
        return 1
    elif core == 'forge':
        installed_versions = mll.utils.get_installed_versions(dir)
        version_is_install = False
        for i in installed_versions:
            if i['id'] == version:
                version_is_install = True
            elif f'{version}-forge-' in i['id']:
                return 2

        if version_is_install == False:
            print('начало загрузки')
            mll.install.install_minecraft_version(versionid=version, minecraft_directory=dir)
            print('успешно')

        forge_versions = mll.forge.list_forge_versions()

        forge_version = ''
        for i in forge_versions:
            if i.startswith(version):
                forge_version = i
                break

        if forge_version is None:
            return f'нет forge для {version}' 
        else:
            print(f"Установка Forge {forge_version} для {version}")
            try:
                mll.forge.install_forge_version(forge_version, dir)
            except FileNotFoundError:
                return 'нет java'
            print('успешно')
            return 1
    elif core == 'fabric':
        installed_versions = mll.utils.get_installed_versions(dir)
        version_is_install = False
        for i in installed_versions:
            if i['id'] == version:
                version_is_install = True
            elif f'fabric_loader-' in i['id'] and version in i['id']:
                return 2

        if version_is_install == False:
            print('начало загрузки')
            mll.install.install_minecraft_version(versionid=version, minecraft_directory=dir)
            print('успешно')

        fabric_versions = mll.fabric.get_all_minecraft_versions()
        is_fabric_versions = False

        for i in fabric_versions:
            if version in i['version'] and i['version'] == True:
                is_fabric_versions = True
                break

        if is_fabric_versions:
            return f'нет fabric для {version}' 
        else:
            fabric_loader_version = mll.fabric.get_latest_loader_version()
            print(f"Установка Fabric {fabric_loader_version} для {version}")
            mll.fabric.install_fabric(version, dir, fabric_loader_version,)
            print("успешно")
            return 1
    return 1
    
