from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0] in ["0", "\"SBABC\"", "'SBABC'"]:
        passed()
    else:
        failed("Incorrect board index")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


