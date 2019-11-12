#!/usr/bin/env python3
"""Run all tests of specific pages
"""
import unittest
import sys
from time import sleep
from libs.base_gui_test import BaseGuiTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class OtherPages(BaseGuiTest):
    """Test all specifics pages
    """
    @classmethod
    def setUpClass(cls):
        """Init chrome driver
        """
        cls.init_driver(True)

    def test_display_page(self):
        """Test display page
        """
        self.goto('index.php?v=d&p=display')
        self.assertIsNotNone(self.get_link_by_title('Retour'))
        self.assertIsNotNone(self.get_element_with_text('h3', 'My Room'))
        self.get_element_by_id('bt_removeHistory').click()
        sleep(2)
        self.assertIsNotNone(self.get_element_by_id('bt_emptyRemoveHistory'))
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        sleep(1)
        self.assertEqual(0, len(self.get_js_logs()))

    def test_interact_page(self):
        """Test interact page
        """
        self.goto('index.php?v=d&p=interact')
        self.assertIsNotNone(self.get_link_by_title('Retour'))
        self.assertIsNotNone(self.get_element_by_id('bt_regenerateInteract'))
        self.get_element_by_id('bt_testInteract').click()
        sleep(2)
        self.assertIsNotNone(self.get_element_by_id('in_testInteractQuery'))
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        sleep(1)
        self.assertEqual(0, len(self.get_js_logs()))

# Entry point
if __name__ == "__main__":
    OtherPages.parse_cli_args()
    # unittest use sys.argv
    del sys.argv[1:]
    # failfast=True pour arrêter à la première erreur
    unittest.main(failfast=True)
