from playwright.sync_api import sync_playwright, expect
import random
import logging

import config


logger = logging.getLogger(__name__)


def execute(n: int = 1):
    """This workflow adds some products to the cart and then checks out."""
    with sync_playwright() as p:
        browser = p.chromium.launch()

        context = browser.new_context()
        context.set_default_timeout(5000)

        iterations = 0

        while iterations < n:
            page = context.new_page()
            page.goto(config.get_app_url())

            product_list = page.locator('css=[data-cy="product-list"]')
            logging.debug("Got products list")

            product_card = product_list.locator("a").nth(random.randrange(0, 4))
            product_url = product_card.get_attribute("href")
            logging.debug("Selected a product card: %s", product_url)

            page.goto(f'{config.get_app_url()}{product_url}') 
            page.locator('css=[data-cy="product-add-to-cart"]').click()
            logging.debug(f"Added product to cart")

            page.locator('css=[data-cy="checkout-place-order"]').click()
            logging.debug('Checked out')

            iterations += 1

        browser.close()

