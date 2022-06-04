from selenium.webdriver.common.by import By

from .base import RecipeBaseFuntionalTest


class RecipeHomePageFunctionalTest(RecipeBaseFuntionalTest):
    def test_recipe_home_page_without_recipes_error_not_found_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No Recipes found here', body.text)
