"""Launch NextDom Plugins tests
"""
import sys
from tests.libs.tests_funcs import *

NEXTDOM_URL = 'http://127.0.0.1:8765'
NEXTDOM_LOGIN = 'admin'
NEXTDOM_PASSWORD = 'nextdom-test'

def migration_tests():
    """Starts gui tests related to the migration page
    """
    container_name = 'migration'
    print_subtitle('Migration')
    start_test_container(container_name, NEXTDOM_PASSWORD)
    # Copy minimal Jeedom backup in the container
    copy_file_in_container(container_name, 'data/backup-Jeedom-3.2.11-2018-11-17-23h26.tar.gz', '/var/www/html/backup/') #pylint: disable=line-too-long
    # Execute the migration
    exec_command_in_container(container_name, 'php /var/www/html/install/restore.php backup=/var/www/html/backup/backup-Jeedom-3.2.11-2018-11-17-23h26.tar.gz > /dev/null 2>&1') #pylint: disable=line-too-long
    # Reset admin password
    exec_command_in_container(container_name, '/usr/bin/mysql -u root nextdomdev -e "UPDATE user SET password = SHA2(\'nextdom-test\', 512)"') #pylint: disable=line-too-long
    run_test('tests/migration_page.py', [NEXTDOM_URL, NEXTDOM_LOGIN, NEXTDOM_PASSWORD])
    remove_test_container(container_name)



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
