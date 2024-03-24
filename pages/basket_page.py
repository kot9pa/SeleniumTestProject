from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_content_empty(self):
        assert bool(self.is_element_present(*BasketPageLocators.BASKET_CONTENT)), \
            "Basket content is not empty"
        
    def should_be_text_basket_empty(self):
        basket = self.is_element_present(*BasketPageLocators.BASKET_CONTENT)
        if not basket:
            self.should_be_basket_content_empty()        
        assert basket.text, \
            f"Basket content is empty, but text is {basket.text}"
