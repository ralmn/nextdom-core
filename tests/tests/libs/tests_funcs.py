"""Functions used by tests
"""
import subprocess
import os
import sys
import time

RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
BLUE = '\033[0;34m'
NC = '\033[0m'

def print_title(title):
    """Print title with decoration
    :param title: Title to show
    """
    nb_stars = len(title) + 8
    print(BLUE + ('*' * nb_stars) + NC)
    print(BLUE + '*** ' + RED + title + ' ' + BLUE + '***' + NC)
    print(BLUE + ('*' * nb_stars) + NC)

def print_subtitle(subtitle):
    """Print subtitle with decoration
    :param subtitle: Subtitle to show
    """
    print('>>> ' + RED + subtitle + NC)

def print_info(information_msg):
    """Print information message with decoration
    :param information_msg: Information to show
    """
    print('>>>>> ' + GREEN + information_msg + NC)

def print_warning(warning_msg):
    """Print warning message with decoration
    :param warning_msg: Warning to show
    """
    print(YELLOW + '/!\\ ' + warning_msg + NC)

def print_error(error_msg):
    """Print error message with decoration
    :param error_msg: Error to show
    """
    print(RED + '!!! ' + error_msg + NC)

def get_root():
    """Return nextdom root directory
    """
    filepath = os.path.realpath(__file__)
    libs = os.path.dirname(filepath)
    tests = os.path.dirname(os.path.dirname(libs))
    return os.path.dirname(tests)

def ask_y_n(question, default='y'):
    """Ask for a question which answer is yes or no
    :param question: Question to show
    :param default:  Default answer
    :type question:  str
    :type default:   str
    :return:         Answer
    :rtype:          str
    """
    choices = 'Y/n'
    if default != 'y':
        choices = 'y/N'
    choice = input('%s [%s] : ' % (question, choices)).lower()
    if choice in (default, ''):
        return default
    return choice


def run_command(command, output=False, ignore_error=False):
    """Execute a command
    :param command:        command to execute
    :type container_name:  str
    :type command:         str
    """
    redirect = subprocess.PIPE
    if output:
        redirect = sys.stdout
    proc = subprocess.Popen(command,
                            stdout=redirect,
                            stderr=subprocess.STDOUT,
                            shell=True)

    stdout, _ = proc.communicate()
    status = proc.wait()
    if not ignore_error and (status != 0):
        raise BaseException("error while running command: %s\n%s" % (command, stdout))


def get_command_output(command):
    """Execute command and get the ouput
    :param command: Command to execute
    :type command:  str
    :return:        (command output, return value)
    :rtype:         tuble
    """
    cmd_process = subprocess.Popen(command,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   shell=True)
    std_out, _ = cmd_process.communicate()
    status = cmd_process.wait()
    return std_out.decode('utf-8'), status

def is_docker_image_initialized():
    """Test if docker image is initialized
    :return: True if the docker image nextdom-test-snap exists
    :rtype:  bool
    """
    output, status = get_command_output('docker images -q nextdom-test-snap:latest')
    if status == 0 and output == '':
        return False
    return True

def create_docker():
    """Create docker image for tests
    """
    print_info('Create docker image for tests')
    clear_docker()
    os.system('./scripts/prepare_docker.sh')

def clear_docker():
    """Remove and kill all containers used for tests
    """
    run_command('./docker/compose test kill', ignore_error=True)
    run_command('./docker/compose test down', ignore_error=True)

def init_docker():
    """Create docker image or ask for reset it. Avoid in travis environment.
    """
    quiet = False
    if "-n" in sys.argv:
        quiet = True
        sys.argv.remove("-n")
    if 'travis' not in os.uname().nodename:
        if not is_docker_image_initialized():
            create_docker()
        elif not quiet:
            reset_answer = ask_y_n('Reset base test container', 'n')
            if reset_answer == 'y':
                create_docker()
        clear_docker()

def start_test_container(container_name, default_password=''):
    """Start a test container
    :param container_name:   Name of the container
    :param default_password: Default password of admin user
    :type container_name:    str
    :type default_password:  str
    """
    print_info('Setup')
    name = "nextdom-test-" + container_name
    port = 8765
    base = "nextdom-test-snap:latest"
    run_command("docker run -d -p %d:80 --name=%s %s /launch.sh" % (port, name, base))
    time.sleep(10)
    container = TestContainer(container_name)
    if default_password != '':
        container.disable_welcome_page()
        container.set_password(default_password)
    return container


def start_all_tests(title, tests_list, use_docker=True):
    """Start all tests
    :param title:      Title of the type of tests
    :param tests_list: List of all tests
    :param use_docker: True if docker is used during tests
    :type title:       str
    :type tests_list:  dict
    :type use_docker:  bool
    :return:           True if all tests pass
    :rtype:            bool
    """
    if use_docker:
        clear_docker()
    print_title(title)
    all_tests_pass = True
    for test in tests_list:
        if tests_list[test]():
            all_tests_pass = False
    return all_tests_pass

def start_specific_test(test_name, tests_list):
    """Start specific test choosed by the user
    :param test_name:  Name of the test
    :param tests_list: List of all tests
    :type test_name:   str
    :type tests_list:  dict
    """
    if test_name in tests_list:
        tests_list[test_name]()
    else:
        print_error('Tests ' + test_name + ' not found')

def run_test(path, parameters=None):
    """Run a test file. Stop script with error on fail.
    :param path:       Path of the test file
    :param parameters: Parameters for the tests
    :type path:        str
    :type parameters:  list
    """
    print_info('Run tests')
    test_cmd = 'python3 -W ignore ' + path
    if parameters is not None:
        test_cmd = test_cmd + ' ' + ' '.join(parameters)
    run_command(test_cmd, output=True)

class TestContainer:
    """Performs system actions on target test container
    """
    def __init__(self, name):
        self.name = name

    def run(self, command, output=False):
        """Run command inside container
        :param command: Command to execute
        :type command:  str
        """
        cmd = "docker exec -i nextdom-test-%s bash -c '%s'" % (self.name, command)
        run_command(cmd, output=output)

    def remove(self):
        """Remove a test container
        """
        print_info('Clear')
        run_command('docker kill nextdom-test-' + self.name, ignore_error=True)
        run_command('docker rm nextdom-test-' + self.name, ignore_error=True)

    def copy_to(self, src, dest):
        """Copy a file from host to test container
        :param src:  Source file
        :param dest: Destination directory
        :type src:   str
        :type dest:  str
        """
        run_command('docker cp ' + src + ' nextdom-test-' + self.name + ':' + dest)

    def copy_from(self, src, dest):
        """Copy a file from test container to host
        :param src:  Source file
        :param dest: Destination directory
        :type src:   str
        :type dest:  str
        """
        os.system("mkdir -p %s" % (os.path.dirname(dest)))
        run_command('docker cp nextdom-test-' + self.name + ':' + src + ' ' + dest)

    def exec_query(self, query):
        """
        Execute given sql query
        """
        command = "/usr/bin/mysql -u root nextdomdev -e \"%s\"" % query
        self.run(command)


    def exec_query_file(self, path):
        """
        Execute given sql file path
        """
        command = "/usr/bin/mysql -u root nextdomdev < %s" % path
        self.run(command)

    def disable_welcome_page(self):
        """
        Disable use of welcome page in target container
        """
        self.force_config_value("nextdom::firstUse", "1", "0")
        self.force_config_value("nextdom::Welcome", "1", "0")

    def force_config_value(self, key, old, new):
        """
        Change value of given configuration key in ini file and database
        """
        query = "UPDATE config SET value = %s WHERE \\`key\\` = \\\"%s\\\"" % (new, key)
        self.exec_query(query)
        self.sed("%s = %s" % (key, old),
                 "%s = %s" % (key, new),
                 "/var/lib/nextdom/config/default.config.ini")

    def set_password(self, password):
        """
        Set mysql password in target container
        """
        query = "UPDATE user SET password = SHA2(\\\"%s\\\", 512)" % password
        self.exec_query(query)

    def sed(self, pattern, replace, target):
        """
        Performs a sed-replace in target container
        """
        sed = "sed -i \"s#%s#%s#g\" %s" % (pattern, replace, target)
        self.run(sed)
