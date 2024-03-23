from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_correct_promo_url()
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_btn.click()

    def check_product_in_basket(self):
        self.should_be_book_name()
        self.should_be_book_price()

    def should_be_correct_promo_url(self):
        assert "promo=newYear" in self.browser.current_url, \
            "Promo URL incorrect"
        
    def should_be_book_name(self):
        product_name = self.get_element_present(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == self.get_element_present(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text, \
            "Book name is wrong"

    def should_be_book_price(self):
        product_price = self.get_element_present(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == self.get_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text, \
            "Book price is wrong"
