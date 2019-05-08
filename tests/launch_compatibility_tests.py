#!/usr/bin/env python3

"""Launch NextDom GUI tests
"""
import sys
from tests.libs.tests_funcs import *

NEXTDOM_URL = 'http://127.0.0.1:8765'
NEXTDOM_LOGIN = 'admin'
NEXTDOM_PASSWORD = 'nextdom-test'

def ajax_tests():
    """Starts gui tests related to the Custom JS and CSS page
    """
    print_subtitle('Ajax')
    container = start_test_container('compatibility', NEXTDOM_PASSWORD)
    container.exec_query_file("/usr/share/nextdom/tests/data/ajax_tests.sql")
    container.run('cd .. && ./vendor/bin/phpunit --configuration tests/compatibility/phpunit.xml --testsuite AllTests') #pylint: disable=line-too-long
    container.remove()

if __name__ == "__main__":
    TESTS_LIST = {
        'ajax': ajax_tests
    }
    init_docker()
    if len(sys.argv) == 1:
        if not start_all_tests('Compatibility Tests', TESTS_LIST):
            sys.exit(1)
    else:
        start_specific_test(sys.argv[1], TESTS_LIST)
