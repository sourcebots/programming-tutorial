from test_helper import run_common_tests, failed, passed, import_task_file

from robot import GameMode

def test_mode():
    task = import_task_file()
    mode = task.mode
    if mode == GameMode.COMPETITION:
        return passed()
    return failed("Incorrect mode")

if __name__ == '__main__':
    run_common_tests()
    test_mode()


