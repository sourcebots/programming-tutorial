from test_helper import run_common_tests, failed, passed, get_answer_placeholders, import_task_file

from robot.robot import Robot


def check_robot():
    task = import_task_file()
    if not hasattr(task, 'robot'):
        return failed("No variable called 'robot'")
    if isinstance(task.robot, Robot):
        return passed()
    return failed("robot is not a Robot")

if __name__ == '__main__':
    run_common_tests()
    check_robot()


