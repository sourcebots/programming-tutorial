from test_helper import run_common_tests, failed, passed, import_task_file


def test_voltage():
    task = import_task_file()
    if task.board.m0._voltage == 50:
        return passed()
    return failed("Voltage was not set to half")


if __name__ == '__main__':
    run_common_tests()
    test_voltage()


