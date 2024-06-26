from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn.btn-default")
    BASKET_LINK_INVALID = (By.CSS_SELECTOR, ".basket-mini .btn.btn-invalid")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM_INVALID = (By.CSS_SELECTOR, "#login_form_invalid")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_INVALID = (By.CSS_SELECTOR, "#register_form_invalid")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    RETRY_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_TO_BASKET_BUTTON_INVALID = (By.CSS_SELECTOR, ".btn-add-to-basket-invalid")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")    
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner strong")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3) .alertinner strong")
    PRODUCT_NAME_PRICE_INVALID = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner invalid")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner")

class BasketPageLocators():
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner>p")
    