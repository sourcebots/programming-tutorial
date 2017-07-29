from test_helper import run_common_tests, failed, passed, import_task_file

def test_zone():
    task = import_task_file()
    zone = task.zone
    if zone == 1:
        return passed()
    return failed("Incorrect zone")

if __name__ == '__main__':
    run_common_tests()
    test_zone()


