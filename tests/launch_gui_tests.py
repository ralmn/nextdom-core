#!/usr/bin/env python3

"""Launch NextDom GUI tests
"""
import sys
from tests.libs.tests_funcs import *

NEXTDOM_URL = 'http://127.0.0.1:8765'
NEXTDOM_LOGIN = 'admin'
NEXTDOM_PASSWORD = 'nextdom-test'

def first_use_tests():
    """Starts gui tests related to the first use page
    """
    print_subtitle('First use page')
    container = start_test_container('firstuse')
    run_test('tests/first_use_page.py', [NEXTDOM_URL])
    container.remove()

def migration_tests():
    """Starts gui tests related to the migration page
    """
    print_subtitle('Migration')
    container = start_test_container('migration', NEXTDOM_PASSWORD)
    container.copy_to('data/backup-Jeedom-3.2.11-2018-11-17-23h26.tar.gz', '/var/lib/nextdom/backup/')  #pylint: disable=line-too-long
    container.run('sudo -u www-data php /usr/share/nextdom/install/restore.php file=/var/lib/nextdom/backup/backup-Jeedom-3.2.11-2018-11-17-23h26.tar.gz') #pylint: disable=line-too-long
    container.set_password("nextdom-test")
    run_test('tests/migration_page.py', [NEXTDOM_URL, NEXTDOM_LOGIN, NEXTDOM_PASSWORD])
    container.remove()

def custom_js_css_tests():
    """Starts gui tests related to the Custom JS and CSS page
    """
    print_subtitle('Custom JS/CSS')
    container = start_test_container('custom-js-css', NEXTDOM_PASSWORD)
    run_test('tests/custom_js_css_page.py', [NEXTDOM_URL, NEXTDOM_LOGIN, NEXTDOM_PASSWORD])
    container.remove()

def plugins_tests():
    """Starts gui tests related to the plugin page
    """
    print_subtitle('Plugins')
    container = start_test_container('plugins', NEXTDOM_PASSWORD)
    container.run('/bin/cp -fr /usr/share/nextdom/tests/data/plugin4tests /usr/share/nextdom/plugins') #pylint: disable=line-too-long
    container.run('/bin/chown www-data:www-data -R /usr/share/nextdom/plugins')
    container.exec_query_file('/usr/share/nextdom/tests/data/plugin_test.sql')
    run_test('tests/plugins_page.py', [NEXTDOM_URL, NEXTDOM_LOGIN, NEXTDOM_PASSWORD])
    container.remove()

def others_tests():
    """Starts others gui tests
    """
    print_subtitle('Others tests')
    container = start_test_container('others', NEXTDOM_PASSWORD)
    print_subtitle('Connection page')
    run_test('tests/connection_page.py', [NEXTDOM_URL, NEXTDOM_LOGIN, NEXTDOM_PASSWORD])
    print_subtitle('Administrations pages')
    run_test('tests/administrations_page.py', [NEXTDOM_URL, NEXTDOM_LOGIN, NEXTDOM_PASSWORD])
    print_subtitle('Rescue pages')
    run_test('tests/rescue_page.py', [NEXTDOM_URL, NEXTDOM_LOGIN, NEXTDOM_PASSWORD])
    container.remove()

if __name__ == "__main__":
    TESTS_LIST = {
        'first_use': first_use_tests,
        'migration': migration_tests,
        'custom_js_css': custom_js_css_tests,
        'plugins': plugins_tests,
        'others': others_tests
    }
    init_docker()
    if len(sys.argv) == 1:
        start_all_tests('GUI Tests', TESTS_LIST)
    else:
        start_specific_test(sys.argv[1], TESTS_LIST)
