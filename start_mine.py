# def start(name, version ....) #$ Кирилл, я тебе сделал этот файл, 
    # (запуск майна)            #$ тут весь бекенд фигачь
# def download_version(version, ....):
    # (ну ты понял)

# ещё одного кода от нейронки я не выдержу

import minecraft_launcher_lib as mll
import subprocess

def read_settings():
    file = open("resource/data/SettingInfo", "r")
    dir = file.readline(0)
    un = file.readline(1)
    return dir, un

def first_launch():
    minecraft_directory = mll.utils.get_minecraft_directory()
    username = '123' #Сделай тут юзернейм

    file = open("resource/data/SettingInfo", "w") 
    file.writelines(f'{minecraft_directory} \n')
    file.writelines(f'{username}')

def settings():
    ...

def start(version, uuid=''):
    dir, username = read_settings()
    options = {
        'username': username,
        'uuid': uuid
    }

    subprocess.call(mll.command.get_minecraft_command(version=version, minecraft_directory=dir, options=options))
    

def download_version(version='1.21.4', core='vanila'):
    # это прогрес бар(на начальное время) когда будешь делать свой пб то эти 2 функции удали
    def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
        if iteration == total:
            print()

    def maximum(max_value, value):
        max_value[0] = value

    max_value = [0]
    callback = {
            "setStatus": lambda text: print(text, end='r'),
            "setProgress": lambda value: printProgressBar(value, max_value[0]),
            "setMax": lambda value: maximum(max_value, value)
    }
    dir, username = read_settings()

    if core == 'vanila':
        print('начало загрузки')
        mll.install.install_minecraft_version(versionid=version, minecraft_directory=dir, callback=callback,)
        print('успешно')

# FirstLaunch()
# download_version()
start('1.21.4')