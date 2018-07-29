from test_helper import run_common_tests, failed, passed, get_answer_placeholders, import_task_file


def test_marker_list():
    task = import_task_file()
    if type(task.markers) == list:
        return passed()
    return failed("You didn't get any markers")

if __name__ == '__main__':
    run_common_tests()



