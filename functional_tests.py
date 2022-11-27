from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Edge()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_later(self):
        # Open the homepage
        self.browser.get('http://localhost:8000')

        # Check the title and header for To-Do List
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # Checks ability to add new to-do items
        inputBox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputBox.get_attribute('placeholder'),
                         'Enter a to-do item')

        # Creates new list item
        inputBox.send_keys('Buy peacock feathers')

        # adds list item to list and tests that it is there
        inputBox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            'New to-do item did not appear in table'
        )

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main()
