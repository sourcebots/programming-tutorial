from test_helper import run_common_tests, failed, passed, import_task_file


def check_position():
    task = import_task_file()
    if task.board.ports[0].position == -0.25:
        return passed()
    return failed("Position incorrect")


if __name__ == '__main__':
    run_common_tests()
    check_position()
