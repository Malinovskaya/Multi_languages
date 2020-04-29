link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button_exists(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector(".add-to-basket>[type='submit']")
    value = button.get_attribute("value")
    assert button, 'There is no button "Add to bucket" on the page!'
    print(f'Button exists, its value is "{value}"')



