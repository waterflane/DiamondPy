# # import flet as ft
# import psutil

# def main(page: ft.Page):
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.theme_mode = ft.ThemeMode.DARK

#     def handle_change_start(e):
#         slider_status.value = "Sliding"
#         page.update()

#     def handle_change(e):
#         slider_value.value = str(e.control.value)
#         page.update()

#     def handle_change_end(e):
#         slider_status.value = "Finished sliding"
#         page.update()
#     page.add(
#         slider_value := ft.Text("0.0"),
#         ft.CupertinoSlider(
#             max=100,
#             active_color=ft.colors.PURPLE,
#             thumb_color=ft.colors.PURPLE,
#             on_change_start=handle_change_start,
#             on_change_end=handle_change_end,
#             on_change=handle_change,
#         ),
#         slider_status := ft.Text(),
#     )


# ft.app(main)

# def get_ram_in_mb():
#     memory = psutil.virtual_memory()
#     total_memory_mb = memory.total / (1024 * 1024)
#     return round(total_memory_mb)

# if __name__ == "__main__":
#     ram_mb = get_ram_in_mb()
#     print(f"Объем оперативной памяти: {ram_mb} МБ")
# import flet as ft
# import flet_webview as ftwv


# def main(page: ft.Page):
#     wv = ftwv.WebView(
#         url="https://flet.dev",
#         on_page_started=lambda _: print("Page started"),
#         on_page_ended=lambda _: print("Page ended"),
#         on_web_resource_error=lambda e: print("Page error:", e.data),
#         expand=True,
#     )
#     page.add(wv)


# ft.app(main)
def find_versions(search_term):
    versions = [
        '19w08a (snapshot) [не установленно]', 
        '19w07a (snapshot) [не установленно]',
        # ... (весь ваш список)
        'rd-132211 (old_alpha) [не установленно]'
    ]
    
    results = []
    for version in versions:
        if search_term in version:
            results.append(version)
            
    return results

if __name__ == "__main__":
    search = input("Введите строку для поиска: ")
    found = find_versions(search)
    
    if not found:
        print("Совпадений не найдено")
    else:
        print(f"Найдено версий: {len(found)}")
        for item in found:
            print(item)