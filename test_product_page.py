from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, ProductPage.PRODUCT_PAGE_LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_product_in_basket()
