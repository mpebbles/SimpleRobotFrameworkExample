import os.path
import subprocess

class SimpleRPN(object):

    def __init__(self):
        self._sut_path = os.path.join(os.path.dirname(__file__),
                                      '..', 'sut', 'simple_rpn')
        self._result = ''

    def run_program_without_input(self):
        self._run_command()

    def run_program_with_input(self, user_input):
        self._run_command(user_input)

    def result_should_contain(self, usage_message):
        if usage_message not in self._result:
            raise AssertionError("Expected output to contain '%s' but instead found '%s'."
                                                 % (usage_message, self._result))

    def result_should_be(self, result_str):
        if result_str != self._result:
            raise AssertionError("Expected output to be '%s' but instead found '%s'."
                                                % (result_str, self._result))

    def _run_command(self, *args):
        command = ["/bin/bash", self._sut_path] + list(args)
        process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        self._result = process.communicate()[0].strip()

