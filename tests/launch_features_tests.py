#!/usr/bin/env python3

"""Launch NextDom features tests
"""
import sys
from tests.libs.tests_funcs import *

def scenarios_tests():
    """Starts tests related to the scenarios
    """
    print_subtitle('Scenarios')
    container = start_test_container('scenarios')
    container.exec_query_file("/usr/share/nextdom/tests/data/smallest_scenario.sql")
    run_test('tests/scenarios.py')
    container.remove()

def plugins_tests():
    """Starts tests related to the plugins
    """
    print_subtitle('Plugins')
    container = start_test_container('plugins')
    container.run('/bin/cp -fr /usr/share/nextdom/tests/data/plugin4tests /usr/share/nextdom/plugins') #pylint: disable=line-too-long
    container.run('/bin/chown www-data:www-data -R /usr/share/nextdom//plugins')
    container.exec_query_file("/usr/share/nextdom/tests/data/plugin_test.sql")
    run_test('tests/plugins.py')
    container.remove()

if __name__ == "__main__":
    TESTS_LIST = {
        'scenarios': scenarios_tests,
        'plugins': plugins_tests
    }
    init_docker()
    if len(sys.argv) == 1:
        start_all_tests('Features', TESTS_LIST)
    else:
        start_specific_test(sys.argv[1], TESTS_LIST)
