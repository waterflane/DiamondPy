import minecraft_launcher_lib as mll
import subprocess
import elyby_api
import os

# Для SettingInfo.txt:
#     1 - директория майна
#     2 - ник
#     3 - uuid
#     4 - use api&

def read_settings():
    file = open("resource/data/SettingInfo", "r")
    Nl = []
    for i in range(len(file)):
        Nl = file.readline(i)
    return Nl

def first_launch(system_launch, username='Player'):
    minecraft_directory = mll.utils.get_minecraft_directory()

    if system_launch == 'offline':
        file = open("resource/data/SettingInfo", "w") 
        #-----------------дирректория-----------ник------uuid---use uuid 
        file.write(f'{minecraft_directory}\n{username}\n{None}\n{False}')
    if system_launch == 'ely':
        uuid = 0

        file = open("resource/data/SettingInfo", "w")
        #-----------------дирректория-----------ник------uuid---use uuid 
        file.write(f'{minecraft_directory}\n{username}\n{uuid}\n{True}')

def settings(new_dir=None, new_username=None, new_uuid=None, use_uuid=None):
    ...

def start(version):
    dir, username, uuid, uuid_use = read_settings()
    options = {
        'username': username,
        'uuid': uuid if uuid_use == 'True' else ''
    }

    subprocess.call(mll.command.get_minecraft_command(version=version, minecraft_directory=dir, options=options))
    

def download_version(version='1.21.4', core='vanila'):
    max_value = [0]
    dir, username, uuid = read_settings()

    if core == 'vanila':
        print('начало загрузки')
        mll.install.install_minecraft_version(versionid=version, minecraft_directory=dir)
        print('успешно')

# first_launch('ely')
