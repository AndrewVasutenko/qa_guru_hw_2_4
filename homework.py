#Сделайте функцию, которая будет печатать читаемое имя переданной ей функции и значений аргументов.
#Вызовите ее внутри функций, описанных ниже
#Подсказка: Имя функции можно получить с помощью func.__name__

def print_name_arguments(func_name, *args):
    func_name = func_name.__name__.replace("_", " ").capitalize()
    print(func_name, *args)

def open_browser(browser_name):
    print_name_arguments(open_browser, browser_name)

def go_to_companyname_homepage(page_url):
    print_name_arguments(go_to_companyname_homepage , page_url)

def find_registration_button_on_login_page(page_url, button_text):
    print_name_arguments(find_registration_button_on_login_page , page_url, button_text)

open_browser("Chrome")
go_to_companyname_homepage("https://www.google.com")
find_registration_button_on_login_page("https://www.google.com", "Войти")