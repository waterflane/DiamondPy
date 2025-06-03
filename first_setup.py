import flet as ft
import minecraft_launcher_lib as mcl
from threading import Timer
import start_mine as mine
import launcher_main
english_yay = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
def create_image_card(url, caption="ёу"):
    return ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Image(
                        src=url,
                        width=120,
                        height=120,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(5)
                    ),
                ),
                ft.Container(
                    content=ft.Text(caption, size=19, text_align=ft.TextAlign.CENTER),
                    opacity=1,
                    margin=ft.margin.only(top=0),
                ),
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=ft.padding.only(top=5, bottom=5),
        opacity=0,
        animate_opacity=ft.Animation(600, ft.AnimationCurve.EASE),
        margin=ft.margin.only(top=-100)
    )

def hello_page(page: ft.Page):
    page.title = "DiamondPy"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.center()
    
    hello_txt = ft.Text('Добро пожаловать в DiamondPy!', size=45)
    
    # Создаем карточки
    image_frame1 = create_image_card("resource/images/ely.jpg", "Войти через ely.by")
    image_frame2 = create_image_card("resource/images/anonym.jpg", "Войти без пароля")
    
    button_style = ft.ButtonStyle(
        padding=10,
        bgcolor=ft.Colors.BLUE_600,
        color=ft.Colors.WHITE,          # Белый текст
        animation_duration=500,
        elevation=0,
        shape=ft.RoundedRectangleBorder(radius=50)
    )

    # Функция для обработки наведения
    def on_hover(e):
        if e.data == "true":  # При наведении
            e.control.style.bgcolor = ft.Colors.BLUE_900
            e.control.style.side = None  # Убираем границу
        else:  # При уходе курсора
            e.control.style.bgcolor = ft.Colors.BLUE_600
        e.control.update()

    # Создаем кнопки с обработчиком on_hover
    ely_button = ft.ElevatedButton(
        "Выбрать",
        style=button_style,
        scale=0.9,
        on_hover=on_hover
    )
    
    offline_button = ft.ElevatedButton(
        "Выбрать",
        style=button_style,
        scale=0.9,
        on_hover=on_hover
    )
    
    # Создаем отдельные контейнеры для кнопок
    ely_button_container = ft.Container(
        ely_button,
        margin=ft.margin.only(top=10),
        clip_behavior=ft.ClipBehavior.NONE
    )
    
    offline_button_container = ft.Container(
        offline_button,
        margin=ft.margin.only(top=5),
        clip_behavior=ft.ClipBehavior.NONE
    )
    
    # Контейнер для карточек и кнопок
    ely_card = ft.Column(
        [
            image_frame1,
            ely_button_container
        ],
        spacing=0,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    offline_card = ft.Column(
        [
            image_frame2,
            offline_button_container
        ],
        spacing=0,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    # Контейнер для карточек
    images_row = ft.Row(
        [ely_card, offline_card],
        spacing=70,
        alignment=ft.MainAxisAlignment.CENTER,
        opacity=0,
        animate_opacity=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
    )
    
    main_container = ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=hello_txt,
                    margin=ft.margin.only(top=-30),
                    scale=ft.Scale(scale=1),
                    animate=ft.Animation(420, ft.AnimationCurve.EASE),
                    animate_scale=ft.Animation(500, ft.AnimationCurve.EASE_OUT_BACK),
                    animate_opacity=ft.Animation(420, ft.AnimationCurve.EASE)
                ),
                ft.Container(
                    content=ft.ElevatedButton("Начать!", on_click=lambda e: animate_text(e), scale=1.5),
                    margin=ft.margin.only(top=40),
                    opacity=1,
                    animate_opacity=ft.Animation(200, ft.AnimationCurve.EASE),
                    animate=ft.Animation(420, ft.AnimationCurve.EASE)
                ),
                images_row
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        ),
        height=600,
        alignment=ft.alignment.center,
        clip_behavior=ft.ClipBehavior.NONE
    )
    
    page.add(main_container)
    # Обработчики для кнопок
    def select_ely(e):
        print("Выбрана авторизация через ely.by")
        # Здесь будет переход на страницу авторификации
        
    def select_offline(e,animated = False):
        def is_valid_string(s: str) -> bool:
                allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")
                return all(char in allowed_chars for char in s)
        def nickname_choose(e):
            setup_nickname_TextField.read_only = True
            if len(setup_nickname_TextField.value) > 0 and is_valid_string(setup_nickname_TextField.value) == True:
                nickname_container.opacity = 0
                setup_nickname_done_container.opacity = 1
                setup_text_d.opacity = 0
                setup_text.opacity = 0
                setup_nickname_done_container.opacity = 0
                setup_nickname_done_container.update()
                setup_text_d.update()
                setup_text.update()
                nickname_container.update()
                setup_nickname_done_container.update()
                def close_anchor(e):
                    selected_version = e.control.data  # Получаем ID версии из data
                    version_select_setup = str(selected_version).split()[0]
                    print(f"Выбрана версия: {version_select_setup}")
                    versions_setup.close_view(selected_version)  # Закрываем view с выбором

                def handle_submit(e):
                    print(f"Выполнен поиск: {e.data}")


                def handle_tap(e):
                    print("Открываем выбор версии")
                    versions_setup.open_view()  # Показываем список версий

                # Получаем версии Minecraft
                # Создаем SearchBar
                versions_setup = ft.SearchBar(
                    view_elevation=4,
                    divider_color=ft.Colors.AMBER,
                    bar_hint_text="Выбери версию",
                    view_hint_text="Выбери версию майна",
                    on_submit=handle_submit,
                    on_tap=handle_tap,
                    controls=[ft.ListTile(title=ft.Text(f'{i}'),on_click=close_anchor, data=i) for i in mine.get_available_versions()]  # Пока пустой список
                )
                # versions_container = ft.Container(
                #     content=versions_setup,
                #     alignment=ft.alignment.bottom_center,
                #     expand=True,
                #     opacity=1,
                #     scale=ft.Scale(scale=1),
                #     margin=ft.margin.only(top=0),
                #     animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT_BACK),
                #     animate_scale=ft.Animation(400, ft.AnimationCurve.EASE_OUT_BACK),
                #     animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE)
                # )
                def setup_version_click_done(e): #!end оф туториал
                    # page.clean()
                    nickname = open('resource/launcher_data/settings/nickname.txt', "w")
                    nickname.write(setup_nickname_TextField.value)
                    nickname.close()
                    tutorial = open('resource/launcher_data/settings/tutorial.txt', "w")
                    tutorial.write('tutorial completed')
                    settings = open('resource/launcher_data/settings/version.txt', "w")
                    settings.write(versions_setup.value)
                    settings.close()
                    tutorial.close()
                    nickname.close()
                    import launcher_main
                    launcher_main.main_launcher(launcher=page)
                setup_version_done = ft.Button('Выбрать',on_click=setup_version_click_done)
                # Обновляем интерфейс
                page.clean()
                page.add(versions_setup,setup_version_done)
            else:
                setup_nickname_TextField.read_only = False

            
        print("Выбран оффлайн режим")
        
        # Очищаем страницу
        page.clean()
        
        # Создаем новый контейнер для текста
        setup_text = ft.Text(
            "Давай всё настроим под тебя!", 
            size=45,
            text_align=ft.TextAlign.CENTER
        )
        def on_change_textfield(e):
            if len(setup_nickname_TextField.value) == 0 or is_valid_string(setup_nickname_TextField.value) == False:
                setup_text_d.value = f'{setup_nickname_TextField.value} - некоректный ник!'
                setup_nickname_done_container.opacity = 0
                setup_nickname_done_container.update()
            else:
                setup_text_d.value = f'Ваш ник: {setup_nickname_TextField.value}'
                setup_nickname_done_container.opacity = 1
                setup_nickname_done_container.update()
            page.update()
        setup_nickname_TextField = ft.TextField(label="Мой никнейм", width=300, autocorrect=False, on_change=on_change_textfield)
        nickname_container = ft.Container(
            content=setup_nickname_TextField,
            alignment=ft.alignment.bottom_center,
            margin=ft.margin.only(top=0),
            opacity=0,
            animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE_IN),
            animate=ft.Animation(150, ft.AnimationCurve.EASE_OUT_BACK)
        )
        setup_nickname_done = ft.ElevatedButton(
            "Далее",
            style=button_style,
            scale=0.9,
            opacity=1,
            on_hover=on_hover,
            animate_opacity=ft.Animation(150, ft.AnimationCurve.EASE_IN),
            on_click=nickname_choose
        )
        setup_nickname_done_container = ft.Container(
            setup_nickname_done,
            margin=ft.margin.only(top=0),
            alignment=ft.alignment.bottom_center,
            clip_behavior=ft.ClipBehavior.NONE,
            opacity=0,
            animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE_IN),
            animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT_BACK)
        )
        setup_container = ft.Container(
            content=setup_text,
            alignment=ft.alignment.center,
            expand=True,
            opacity=0,
            scale=ft.Scale(scale=0.2),
            margin=ft.margin.only(top=-160),
            animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT_BACK),
            animate_scale=ft.Animation(400, ft.AnimationCurve.EASE_OUT_BACK),
            animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE)
        )
        def animate_setup():
            setup_container.opacity = 1
            setup_container.scale = ft.Scale(scale=1.0)
            setup_container.update()
        def animate_setup_up():
            setup_container.margin = ft.margin.only(top=-650)
            nickname_container.opacity = 1
            
            nickname_container.margin = ft.margin.only(top=280)
            setup_nickname_done_container.opacity = 0
            setup_nickname_done_container.margin = ft.margin.only(top=15)
            nickname_container.update()
            setup_nickname_done_container.update()
            setup_container.update()
        # Добавляем контейнер на страницу
        setup_text_d = ft.Text(value='',scale=1.5,text_align=ft.TextAlign.CENTER)
        setup_text_d_container = ft.Container(
            content=setup_text_d,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=10),
            animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE_IN)
        )
        setup_text_d.value = ''
        page.add(nickname_container,setup_text_d_container,setup_nickname_done_container,setup_container)
        Timer(0.2, animate_setup).start()
        Timer(1, animate_setup_up).start()

    
    ely_button.on_click = select_ely
    offline_button.on_click = select_offline
    
    def animate_text(e):
        # Анимация кнопки "Начать!"
        main_container.content.controls[1].opacity = 0
        main_container.content.controls[1].margin = ft.margin.only(top=100)
        
        # Показываем картинки с анимацией
        main_container.content.controls[2].opacity = 1
        page.update()
        
        # Поочередное появление карточек
        Timer(0.1, lambda: set_opacity(image_frame1, 1)).start()
        Timer(0.3, lambda: set_opacity(image_frame2, 1)).start()

def set_opacity(container, opacity):
    container.opacity = opacity
    container.update()

ft.app(hello_page)