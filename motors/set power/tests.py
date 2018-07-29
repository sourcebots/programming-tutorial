from test_helper import run_common_tests, failed, passed, import_task_file


def test_voltage():
    task = import_task_file()
    if task.board.m0._voltage == 0.5:
        return passed()
    return failed("Voltage was not set to half speed forwards")


if __name__ == '__main__':
    run_common_tests()
    test_voltage()
