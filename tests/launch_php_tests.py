#!/usr/bin/env python3

"""Launch NextDom GUI tests
"""
import sys
from tests.libs.tests_funcs import *

NEXTDOM_URL = 'http://127.0.0.1:8765'
NEXTDOM_LOGIN = 'admin'
NEXTDOM_PASSWORD = 'nextdom-test'

def php_tests():
    """Starts gui tests related to the Custom JS and CSS page
    """
    container = start_test_container('phpunit', NEXTDOM_PASSWORD)
    container.run('cp -fr /usr/share/nextdom/tests/data/plugin4tests /usr/share/nextdom/plugins')
    container.run('chown www-data:www-data -R /usr/share/nextdom/plugins')
    container.exec_query_file("/usr/share/nextdom/tests/data/phpunit_tests_fixtures.sql")
    container.run('service cron stop')
    container.run('apt-get install -y php-xdebug')
    container.run('cd /usr/share/nextdom/ && ./vendor/bin/phpunit --configuration tests/phpunit_tests/phpunit.xml --testsuite AllTests', output=True) #pylint: disable=line-too-long
    container.copy_from('/usr/share/nextdom/tests/coverage/clover.xml', 'coverage/')
    container.remove()

def main(tests_list):
    """Main function
    """
    init_docker()
    if len(sys.argv) == 1:
        start_all_tests('PHPUnit Tests', tests_list, False)
    else:
        start_specific_test(sys.argv[1], tests_list)

if __name__ == "__main__":
    TESTS_LIST = {
        'php': php_tests
    }
    main(TESTS_LIST)
