import flet as ft
import start_mine
from threading import Timer
# ! Дальше бога нет!!!!!
def create_image_card(url, caption="ёу", on_click=None):
    caption_container = ft.Container(
        content=ft.Text(caption, size=19, text_align=ft.TextAlign.CENTER),
        opacity=1,
        animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE)
    )
    
    return ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Image(
                        src=url,
                        width=100,
                        height=100,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(5)
                    ),
                    border=ft.border.all(2, ft.Colors.GREY_400),
                    border_radius=ft.border_radius.all(10),
                    padding=3,
                ),
                caption_container
            ],
            spacing=3,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=10,
        opacity=0,
        animate_opacity=ft.Animation(600, ft.AnimationCurve.EASE),
        margin=ft.margin.only(top=-270)
    )


def hello_page(page: ft.Page):
    page.title = "DiamondPy"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    hello_txt = ft.Text('Добро пожаловать в DiamondPy!', size=45)
    def go_to_page1(e):
        page.clean()
        page.add(ft.Text("страница 1", size=30))
    
    def go_to_page2(e):
        page.clean()
        page.add(ft.Text("страница 2", size=30))
    
    image_frame1 = create_image_card("resource\images\ely.jpg", "ely.by", on_click=go_to_page1)
    image_frame2 = create_image_card("resource\images/anonym.jpg", "Офлайн аккаунт", on_click=go_to_page2)
    
    images_row = ft.Row(
        [image_frame1, image_frame2],
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
                    margin=ft.margin.only(top=0),
                    scale=ft.Scale(scale=1),
                    animate=ft.Animation(420, ft.AnimationCurve.EASE),
                    animate_scale=ft.Animation(500, ft.AnimationCurve.EASE),
                    animate_opacity=ft.Animation(420, ft.AnimationCurve.EASE)
                ),
                ft.Container(
                    content=ft.ElevatedButton("Начать!", on_click=lambda e: animate_text(e), scale=1.5),
                    margin=ft.margin.only(top=20),
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
        alignment=ft.alignment.center
    )
    
    page.add(main_container)
    
    def animate_text(e):
        main_container.content.controls[1].opacity = 0
        main_container.content.controls[1].margin = ft.margin.only(top=290)
        main_container.content.controls[2].opacity = 1
        page.update()
        Timer(0.1, lambda: set_opacity(image_frame1, 1)).start()
        Timer(0.3, lambda: set_opacity(image_frame2, 1)).start()

def set_opacity(container, opacity):
    container.opacity = opacity
    container.update()

ft.app(hello_page)