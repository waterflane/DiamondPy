import flet as ft
from threading import Timer
import start_mine as mine
print(__name__)
def main_launcher(launcher: ft.Page):
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

    def handle_submit_version_choose(e):
        print(f"Выполнен поиск: {e.data}")


    def handle_tap_version_choose(e):
        print("Открываем выбор версии")
        version_choose.open_view()

    version_choose = ft.SearchBar(
        view_elevation=1,
        full_screen=False,
        width=100,
        divider_color=ft.Colors.AMBER,
        bar_hint_text="Выбери версию",
        view_hint_text="Выбери версию майна",
        on_submit=handle_submit_version_choose,
        on_tap=handle_tap_version_choose,
        controls=[ft.ListTile(title=ft.Text(f'{i}'),on_click=close_version_choose, data=i) for i in mine.get_available_versions()]  # Пока пустой список
    )
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
                icon=ft.Icon(ft.Icons.BOOKMARK_BORDER),
                selected_icon=ft.Icon(ft.Icons.BOOKMARK),
                label="Сборки",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
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
        hello_txt.value = f'\n       Привет, {nickname_set_TextField.value}!'
        hello_txt.update()
    nickname_set_TextField = ft.TextField(label='Ваш ник:',value=player_name,on_change=change_nickname,max_length=16)
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
        margin=ft.margin.only(top=0,left=70),
        animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE_IN),
        animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT_BACK)
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
        temp_version_f = open('resource/launcher_data/settings/version.txt', 'r')
        start_version = temp_version_f.read()
        temp_version_f.close()
        launcher.clean()
        txt_start = ft.Text(value=f'Запуск Майнкрафта {start_version}...', size=45,overflow=ft.TextOverflow.VISIBLE)
        invible_object = ft.Text(value='', size=45,overflow=ft.TextOverflow.VISIBLE)
        launcher.vertical_alignment = ft.MainAxisAlignment.CENTER
        launcher.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        launcher.add()
        launcher.add(txt_start,invible_object)
        file = open("resource/data/SettingInfo", "r")
        if len(file.read()) < 2:
            mine.first_launch(system_launch="offline",username_if_offline=player_name)
        if start_version in mine.get_available_versions():
            mine.start(start_version)
        else:
            mine.download_version(version=start_version)
            mine.start(start_version)
        file.close()
    start_minecraft = ft.Button(
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
    launcher.add(
    ft.Row(
            [
                rail_menu,
                ft.VerticalDivider(width=1),
                ft.Column(
                    [hello_txt_contai,nickname_set_cont,version_text_choose_cont,version_choose_cont,start_minecraft_container],
                    alignment=ft.MainAxisAlignment.START,
                    expand=True,
                ),
            ],
            expand=True,
        )
    )

if __name__ == "__main__":
    ft.app(main_launcher)