import flet as ft
from threading import Timer
import start_mine as mine
import minecraft_launcher_lib as mll
print(__name__)
uuid_use_ely = False
nickname_ely_by_yay = None
with open('resource/data/SettingInfo', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    if len(lines) >= 2:
        nickname_ely_by_yay = lines[1].strip()
    if len(lines) >= 4:
        uuid_use_ely = lines[3].strip() == "True"  # Преобразует строку в bool
    else:
        uuid_use_ely = False  # Значение по умолчанию, если строк меньше 4
print(nickname_ely_by_yay)
print(uuid_use_ely)  # Выведет True (если в файле было "True")
def main_launcher(launcher: ft.Page):
    launcher.window.maximized = False
    def is_valid_string(s: str) -> bool:
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")
        return all(char in allowed_chars for char in s)
    launcher.vertical_alignment = None
    launcher.horizontal_alignment = None
    launcher.title = "DiamondPy"
    launcher.window.center()
    launcher.clean()
    version_file = open('resource/launcher_data/settings/version.txt', 'r')
    player_name_txt = open('resource/launcher_data/settings/nickname.txt', 'r')
    version_mine = version_file.read()
    version_file.close()
    player_name = player_name_txt.read()
    player_name_txt.close()
    ooooooooooooooooooo = open('resource/launcher_data/settings/ely_by_use.txt', 'a+')
    uuuuuuuuwwwwwuuuuuuuuu = (ooooooooooooooooooo.read() == 'True')
    ooooooooooooooooooo.close()
    if uuid_use_ely == False:
        hello_txt = ft.Text(f'\n       Привет, {player_name}!', size=35, no_wrap=True, overflow=ft.TextOverflow.VISIBLE)
    elif uuid_use_ely and uuuuuuuuwwwwwuuuuuuuuu:
        hello_txt = ft.Text(f'\n       Привет, {nickname_ely_by_yay}!', size=35, no_wrap=True, overflow=ft.TextOverflow.VISIBLE)
    elif uuid_use_ely and uuuuuuuuwwwwwuuuuuuuuu == False:
        hello_txt = ft.Text(f'\n       Привет, {player_name}!', size=35, no_wrap=True, overflow=ft.TextOverflow.VISIBLE)
    version_text_choose = ft.Text(f'Версия:', size=18, overflow=ft.TextOverflow.VISIBLE)
    def close_version_choose(e):
        selected_version = e.control.data  # Получаем ID версии из data
        version_select_setup = str(selected_version).split()[0]
        temp_version_f = open('resource/launcher_data/settings/version.txt', 'w')
        temp_version_f.write(version_select_setup)
        temp_version_f.close()
        print(f"Выбрана версия: {version_select_setup}")
        version_choose.close_view(selected_version)  # Закрываем view с выбором
    def close_version_choose_loader(e):
        loader_choose.close_view(e.control.data)  # Закрываем view с выбором
    def handle_submit_version_choose(e):
        print(f"Выполнен поиск: {e.data}")


    def handle_tap_version_choose(e):
        print("Открываем выбор версии")
        
        version_choose.update()
        version_choose.open_view()
    def handle_tap_version_choose_loader(e):
        print("Открываем выбор лоадеров")
        
        loader_choose.update()
        loader_choose.open_view()
    def handle_change_version_choose(e):
        pass

    version_choose = ft.SearchBar(
        view_elevation=1,
        full_screen=False,
        width=100,
        bar_hint_text="Выбери версию",
        view_hint_text="Выбери версию майна",
        on_submit=handle_submit_version_choose,
        on_tap=handle_tap_version_choose,
        on_change=handle_change_version_choose,
        controls=[ft.ListTile(title=ft.Text(i), on_click=close_version_choose, data=i) for i in mine.get_available_versions()]
    )
    loader_choose = ft.SearchBar(
        view_elevation=1,
        full_screen=False,
        width=400,
        height=60,
        bar_hint_text="Выбери версию",
        view_hint_text="Выбери версию майна",
        on_submit=handle_submit_version_choose,
        on_tap=handle_tap_version_choose_loader,
        on_change=handle_change_version_choose,
        controls=[ft.ListTile(title=ft.Text(i), on_click=close_version_choose_loader, data=i) for i in ["Vanila", "Forge", "Fabric"]]
    )
    loader_choose_cont = ft.Container(
        content=loader_choose,
        height=60,
        opacity=1,
        scale=ft.Scale(scale=1),
        margin=ft.margin.only(top=20,left=70),
        animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE_IN),
        animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT_BACK)
    )
    version_choose.value = version_mine
    version_choose_cont = ft.Container(
        content=version_choose,
        alignment=ft.alignment.bottom_left,
        expand=True,
        opacity=1,
        width=400,
        scale=ft.Scale(scale=1),
        margin=ft.margin.only(top=0,left=10),
        animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE_IN),
        animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT_BACK)
    )

    def change_nickname(e):
        if is_valid_string(nickname_set_TextField.value) == True and len(nickname_set_TextField.value) > 0:
            nickname_set_TextField.error_text = None
            nickname_set_TextField.helper_text = ''
            nickname_set_TextField.update()
            nickname_file = open('resource/launcher_data/settings/nickname.txt', 'w')
            nickname_file.write(nickname_set_TextField.value)
            nickname_file.close()
        elif len(nickname_set_TextField.value) == 0:
            nickname_set_TextField.helper_text = 'Так не пойдет, пустой ник это слишком скучно!'
            nickname_set_TextField.error_text = None
            nickname_set_TextField.update()
        else:
            nickname_set_TextField.helper_text = ''
            nickname_set_TextField.error_text = 'Разрешенные символы: A-z, -, _'
            nickname_set_TextField.update()
        if use_ely_by_account.value == False:
            hello_txt.value = f'\n       Привет, {nickname_set_TextField.value}!'
            hello_txt.update()
        elif use_ely_by_account.value == True and use_ely_by_account.value == True:
            hello_txt.value = f'\n       Привет, {nickname_ely_by_yay}!'
            hello_txt.update()
    nickname_set_TextField = ft.TextField(label='Ваш ник:',value=player_name,on_change=change_nickname,max_length=16)
    def slider_ram_on_change(e):
        print(mine.get_ram_in_mb())
    slider_ram = ft.Slider(
        value=0,
        on_change=slider_ram_on_change,

    )
    nickname_set_cont = ft.Container(
        content=nickname_set_TextField,
        opacity=1,
        width=350,
        scale=ft.Scale(scale=1),
        margin=ft.margin.only(top=60,left=80),
        animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE_IN),
        animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT_BACK)
    )
    

    version_choose_cont = ft.Container(
        content=version_choose,
        opacity=1,
        width=400,
        scale=ft.Scale(scale=1),
        margin=ft.margin.only(top=0,left=70,bottom=3),
        animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE_IN),
        # animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT_BACK),
    )
    launcher.window.resizable =False
    launcher.window.full_screen = False
    version_text_choose_cont = ft.Container(
        content=version_text_choose,
        opacity=1,
        width=400,
        margin=ft.margin.only(top=10,left=90),
        animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE_IN),
        animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT_BACK)
    )
    hello_txt_contai = ft.Container(
        content=hello_txt,
        opacity=1,
        width=400,
        scale=ft.Scale(scale=1),
        margin=ft.margin.only(top=0,left=0),
        animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE_IN),
        animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT_BACK)
    )
    def start_mine_yay(e):
        launcher.window.visible = True
        
        temp_version_f = open('resource/launcher_data/settings/version.txt', 'r')
        start_version = temp_version_f.read()
        temp_version_f.close()
        file = open("resource/data/SettingInfo", "r")
        if len(file.read()) < 2:
            mine.first_launch(system_launch="offline",username_if_offline=player_name)
        if start_version in mine.get_available_versions():
            mine.start(start_version, use_ely_by=use_ely_by_account.value)
        else:
            mine.download_version(version=start_version)
            mine.start(start_version, use_ely_by=use_ely_by_account.value)
        file.close()
    start_minecraft = ft.ElevatedButton(
        text='Играть!',
        scale=ft.Scale(scale=1.5),
        on_click=start_mine_yay 
    )
    start_minecraft_container = ft.Container(
        content=start_minecraft,
        opacity=1,
        margin=ft.margin.only(top=0,left=120)
    )
    version_choose.value = version_mine
    def change_page(e):
        print(e)
        print("Selected destination:", e.control.selected_index)
        if e.control.selected_index == 0:
            with open('resource/data/SettingInfo', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if len(lines) >= 2:
                    nickname_ely_by_yay = lines[1].strip()
                if len(lines) >= 4:
                    uuid_use_ely = lines[3].strip() == "True"
            launcher.clean()
            def use_ely_on_change(e):
                if uuid_use_ely == False:
                    use_ely_by_account.disabled = True
                elif uuid_use_ely == True:
                    use_ely_by_account.disabled = False
                if use_ely_by_account.value == False:
                    hello_txt.value = f'\n       Привет, {nickname_set_TextField.value}!'
                    nickname_set_TextField.visible = True
                elif use_ely_by_account.value:
                    hello_txt.value = f'\n       Привет, {nickname_ely_by_yay}!'
                    nickname_set_TextField.visible = False
                nickname_set_TextField.update()
                hello_txt.update()
                launcher.update()
                temps = open("resource\launcher_data\settings\ely_by_use.txt", "w")
                temps.write(str(use_ely_by_account.value))
                temps.close()
            temps = open("resource\launcher_data\settings\ely_by_use.txt", "a+")
            if uuid_use_ely:
                use_ely_by_account_file = (temps.read() == 'True')
            else:
                use_ely_by_account_file = False
            temps.close()
            use_ely_by_account = ft.Checkbox(label="Использовать ely.by аккаунт", value=use_ely_by_account_file,on_change=use_ely_on_change)
            if uuid_use_ely == False:
                use_ely_by_account.value = False
                use_ely_by_account.visible = False
            elif uuid_use_ely == True:
                use_ely_by_account.visible = True
            if use_ely_by_account.value == False:
                hello_txt.value = f'\n       Привет, {nickname_set_TextField.value}!'
                nickname_set_TextField.visible = True
            elif use_ely_by_account.value:
                hello_txt.value = f'\n       Привет, {nickname_ely_by_yay}!'
                nickname_set_TextField.visible = False
            launcher.add(
            ft.Row(
                    [
                        rail_menu,
                        ft.VerticalDivider(width=1),
                        ft.Column(
                            [hello_txt_contai,nickname_set_cont,version_text_choose_cont,version_choose_cont,loader_choose_cont,use_ely_by_account_container,start_minecraft_container],
                            alignment=ft.MainAxisAlignment.START,
                            expand=True,
                        ),
                    ],
                    expand=True,
                )
            )
            print(uuid_use_ely, use_ely_by_account.value)
        elif e.control.selected_index == 3:
            launcher.clean()
            hello_txt.value = f'\n       Здесь ничего нет :('
            launcher.add(
            ft.Row(
                    [
                        rail_menu,
                        ft.VerticalDivider(width=1),
                        ft.Column(
                            [hello_txt_contai],
                            alignment=ft.MainAxisAlignment.START,
                            expand=True,
                        ),
                    ],
                    expand=True,
                )
            )
        elif e.control.selected_index == 1:
            with open('resource/data/SettingInfo', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if len(lines) >= 2:
                    nickname_ely_by_yay = lines[1].strip()
                if len(lines) >= 4:
                    uuid_use_ely = lines[3].strip() == "True"
            launcher.clean()
            hello_txt.value = f'\n       Настройка Аккаунтов'
            ely_by_text = ft.Text(
                value="               --------------------------------\n                Настройка привязки ely.by",
                size=23,
            )
            status_ely_by_account = ft.Text(
                value=f"                             Статус привязки: {uuid_use_ely}",
                size=18,
            )
            nickname_ely_by_text_settings = ft.Text(
                value=f"{' '*(42-(len(nickname_ely_by_yay)-2))}Ник: {nickname_ely_by_yay}",
                size=18,
            )
            if uuid_use_ely == False:
                nickname_ely_by_text_settings.value = f"{' '*42}Ник: "
            def change_nickname_ely_by_on(e):
                import webbrowser
                webbrowser.open_new_tab('https://account.ely.by/profile/change-username')
            change_nickname_ely_by = ft.ElevatedButton(
                text="Изменить ник",
                on_click=change_nickname_ely_by_on,
            )
            change_nickname_ely_by_container = ft.Container(
                content=change_nickname_ely_by,
                margin=ft.margin.only(left=186,top=5)
            )
            def logout_ely_by(e):
                with open("resource/data/SettingInfo", 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                if len(lines) >= 4:
                    lines[2] = "\n"
                    lines[3] = "False\n" 
                    # Перезаписываем файл
                    with open("resource/data/SettingInfo", 'w', encoding='utf-8') as file:
                        file.writelines(lines)
                    print("Выход из ely by аккаунта")
                    launcher.close(remove_ely_by)
                    main_launcher(launcher)
                    launcher.open(ft.SnackBar(ft.Text(f"Вы вышли из аккаунта {nickname_ely_by_yay}"),show_close_icon=True))

            remove_ely_by = ft.AlertDialog(
            modal=True,
            title=ft.Text("Выйти из аккаунта?"),
            content=ft.Text("Точно? Вам придется заново входить в аккаунт!"),
            actions=[
                ft.TextButton("Да", on_click=logout_ely_by),
                ft.TextButton("Не, я пошутил", on_click=lambda e: launcher.close(remove_ely_by)),
            ],
            
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
            )
            remove_account_ely_by = ft.ElevatedButton(
                text="Выйти из аккаунта ely.by",
                on_click=lambda e: launcher.open(remove_ely_by)
            )
            remove_account_ely_by_container = ft.Container(
                content=remove_account_ely_by,
                margin=ft.margin.only(left=153,top=5)
            )
            def login_in_ely_by(e):
                launcher.vertical_alignment = ft.MainAxisAlignment.CENTER
                launcher.horizontal_alignment = ft.CrossAxisAlignment.CENTER
                def back_to_main_menu_on_click(e):
                    launcher.clean()
                    main_launcher(launcher)
                    return 0
                back_to_main_menu = ft.ElevatedButton(
                    text="Назад",
                    on_click=back_to_main_menu_on_click,
                )
                setup_text = ft.Text(
                    "Вход в ely.by", 
                    size=45,
                    text_align=ft.TextAlign.CENTER
                )
                setup_text_contai = ft.Container(
                    content=setup_text,
                    margin=ft.margin.only(top=-90)
                )
                login_ely_textfield = ft.TextField(
                    value='',
                    width=250,
                    label="Логин",
                    border_color=ft.Colors.BLUE_ACCENT_100,
                )
                login_ely_textfield_contai = ft.Container(
                    content=login_ely_textfield,
                    margin=ft.margin.only()
                )
                password_ely_textfield = ft.TextField(
                    value='',
                    width=250,
                    label="Пароль", password=True, can_reveal_password=True,
                    border_color=ft.Colors.BLUE_ACCENT_100,
                )
                password_ely_textfield_contai = ft.Container(
                    content=password_ely_textfield,
                    margin=ft.margin.only()
                )
                def page_2FA():
                    launcher.clean()
                    launcher.add(text_2FA_nada_contain,textfield_2FA,try_2FA_button_ely,back_button_ely)
                def try_to_login_on_click(e):
                    try_login_ely = mine.ely_by_auth(login=login_ely_textfield.value,passw=password_ely_textfield.value)
                    if try_login_ely == "2FA protect":
                        page_2FA()
                    elif try_login_ely == "Invalid username or password":
                        launcher.open(ft.SnackBar(ft.Text(f"Ошибка входа, проверьте логин/пароль"),show_close_icon=True))
                    else:
                        launcher.open(ft.SnackBar(ft.Text(f"Вы успешно вошли под ником {login_ely_textfield.value}"),show_close_icon=True))
                        main_launcher(launcher)
                try_to_login_button = ft.ElevatedButton(
                    text="Войти",
                    color=ft.Colors.BLUE_ACCENT_100,
                    on_click=try_to_login_on_click,
                )
                text_2FA_nada = ft.Text(
                    "Введите 2FA код:", 
                    size=45,
                    text_align=ft.TextAlign.CENTER
                )
                text_2FA_nada_contain = ft.Container(
                    content=text_2FA_nada,
                    margin=ft.margin.only(top=-90)
                )
                textfield_2FA = ft.TextField(
                    value='',
                    width=250,
                    border_color=ft.Colors.BLUE_ACCENT_100,
                )
                def back_to_ely_by(e):
                    launcher.clean()
                    launcher.add(setup_text_contai,login_ely_textfield_contai,password_ely_textfield_contai,try_to_login_button)
                def try_to_login_2FA_on_click(e):
                    temp = mine.ely_by_auth(login=login_ely_textfield.value,passw=password_ely_textfield.value,TOTP=textfield_2FA.value.replace(" ",""))
                    if temp == "2FA correct":
                        launcher.clean()
                        launcher.vertical_alignment = None
                        launcher.horizontal_alignment = None
                        main_launcher(launcher)
                    elif temp == "2FA invalid":
                        launcher.open(ft.SnackBar(ft.Text(f"Неправильный 2FA ключ"),show_close_icon=True))
                try_2FA_button_ely = ft.ElevatedButton(
                    text="Подтвердить",
                    color=ft.Colors.BLUE_ACCENT_100,
                    on_click=try_to_login_2FA_on_click,
                )
                back_button_ely = ft.ElevatedButton(
                    text="Назад",
                    color=ft.Colors.BLUE_ACCENT_100,
                    on_click=back_to_ely_by,
                )
                launcher.clean()
                launcher.add(setup_text_contai,login_ely_textfield_contai,password_ely_textfield_contai,try_to_login_button,back_to_main_menu)
            login_in_account_ely = ft.ElevatedButton(
                text="Войти в ely.by",
                on_click=login_in_ely_by,
            )
            login_in_account_ely_container = ft.Container(
                content=login_in_account_ely,
                margin=ft.margin.only(left=184,top=5)
            )
            if uuid_use_ely == True:
                launcher.add(
                ft.Row(
                        [
                            rail_menu,
                            ft.VerticalDivider(width=1),
                            ft.Column(
                                [hello_txt_contai,ely_by_text,status_ely_by_account,nickname_ely_by_text_settings,change_nickname_ely_by_container,remove_account_ely_by_container],
                                alignment=ft.MainAxisAlignment.START,
                                expand=True,
                            ),
                        ],
                        expand=True,
                    )
                )
            else:
                launcher.add(
                ft.Row(
                        [
                            rail_menu,
                            ft.VerticalDivider(width=1),
                            ft.Column(
                                [hello_txt_contai,ely_by_text,status_ely_by_account,nickname_ely_by_text_settings,login_in_account_ely_container],
                                alignment=ft.MainAxisAlignment.START,
                                expand=True,
                            ),
                        ],
                        expand=True,
                    )
                )
        elif e.control.selected_index == 2:
            launcher.clean()
            hello_txt.value = '\n       Настройки'
            launcher.add(
            ft.Row(
                    [
                        rail_menu,
                        ft.VerticalDivider(width=1),
                        ft.Column(
                            [hello_txt_contai,slider_ram],
                            alignment=ft.MainAxisAlignment.START,
                            expand=True,
                        ),
                    ],
                    expand=True,
                ),
            )
    def use_ely_on_change(e):
        if uuid_use_ely == False:
                use_ely_by_account.value = False
                use_ely_by_account.visible = False
        elif uuid_use_ely == True:
            use_ely_by_account.visible = True
        if use_ely_by_account.value == False:
            hello_txt.value = f'\n       Привет, {nickname_set_TextField.value}!'
            nickname_set_TextField.visible = True
        elif use_ely_by_account.value:
            hello_txt.value = f'\n       Привет, {nickname_ely_by_yay}!'
            nickname_set_TextField.visible = False
        nickname_set_TextField.update()
        launcher.update()
        temps = open("resource\launcher_data\settings\ely_by_use.txt", "w")
        temps.write(str(use_ely_by_account.value))
        temps.close()
    temps = open("resource\launcher_data\settings\ely_by_use.txt", "r")
    use_ely_by_account_file = (temps.read() == 'True')
    temps.close()   
    
    use_ely_by_account = ft.Checkbox(label="Использовать ely.by аккаунт", value=use_ely_by_account_file, disabled=(uuid_use_ely == False),on_change=use_ely_on_change)
    use_ely_by_account_container = ft.Container(
        ft.Container(
            content=use_ely_by_account,
            margin=ft.margin.only(left=80,bottom=5)
        )
    )
    
    if uuid_use_ely == True and use_ely_by_account.value:
        nickname_set_TextField.visible = False
    elif use_ely_by_account.value == False:
        nickname_set_TextField.visible == True
    rail_menu = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=60,
        opacity=1,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME,
                label="Главная",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.MANAGE_ACCOUNTS_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.MANAGE_ACCOUNTS),
                label_content=ft.Text("Аккаунты"),
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.SETTINGS),
                label_content=ft.Text("Настройки"),
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.BOOKMARK_BORDER),
                selected_icon=ft.Icon(ft.Icons.BOOKMARK),
                label="Сборки",
            )
        ],
        on_change=change_page,
    )

    launcher.add(
            ft.Row(
                    [
                        rail_menu,
                        ft.VerticalDivider(width=1),
                        ft.Column(
                            [hello_txt_contai,nickname_set_cont,version_text_choose_cont,version_choose_cont,loader_choose_cont,use_ely_by_account_container,start_minecraft_container],
                            alignment=ft.MainAxisAlignment.START,
                            expand=True,
                        ),
                    ],
                    expand=True,
                )
            )

if __name__ == "__main__":
    ft.app(main_launcher)