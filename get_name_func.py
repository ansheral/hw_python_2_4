def get_name_function(function_name, *args):
    function_name = function_name.__name__.replace("_", " ").capitalize()
    print(f'{function_name}:', )
    for arg in args:
        print(f'"{arg}"')


def open_browser(browser_name):
    get_name_function(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    get_name_function(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    get_name_function(find_registration_button_on_login_page, page_url, button_text)


open_browser("Chrome")
go_to_companyname_homepage("https://www.google.com")
find_registration_button_on_login_page("https://www.google.com", "Поиск в Google")
