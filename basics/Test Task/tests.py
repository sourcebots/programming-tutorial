from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder.lower() in ["\"hello world\"", "'hello world'"]:
        passed()
    else:
        failed("You didn't print \"Hello World\"")z


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()

