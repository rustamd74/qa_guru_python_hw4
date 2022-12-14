def func_print(func, *args):
    func = func.__name__.replace("_", " ")
    print(func, *args)

def open_browser(browser_name):
    func_print(open_browser, browser_name)

def go_to_company_name_homepage(page_url):
    func_print(go_to_company_name_homepage, page_url)

def find_registration_button_on_login_page(page_url, button_text):
    func_print(find_registration_button_on_login_page, page_url, button_text)

open_browser('Chrome')
go_to_company_name_homepage('https://www.linkedin.com')
find_registration_button_on_login_page('www.linkedin.com/home', 'Sign in')