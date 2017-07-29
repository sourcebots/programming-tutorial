from test_helper import run_common_tests, failed, passed, import_task_file

from robot import TOKEN
from robot.marker import Marker

def test_marker():
    task = import_task_file()
    token = task.token
    if token is None:
        return failed("You forgot to store the token!")
    if not isinstance(token, Marker):
        return failed("You haven't stored a marker!")
    if token.id not in TOKEN:
        return failed("This isnt a token marker!")
    return passed()


if __name__ == '__main__':
    run_common_tests()
    test_marker()


