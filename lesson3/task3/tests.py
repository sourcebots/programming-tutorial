from test_helper import run_common_tests, failed, passed, get_answer_placeholders, import_task_file


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0] != "m1":
        return failed("You set the wrong motor!")
    if placeholders[1] == "50":
        return failed("Dont set the value directly!")
    passed()


def test_voltage():
    task = import_task_file()
    if task.board.m1._voltage != 50:
        return failed("Got incorrect voltage value")
    passed()


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()
    test_voltage()


