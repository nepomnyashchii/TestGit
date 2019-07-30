from pyassert import assert_that


def get_int():
    return 1

# https://github.com/pyclectic/pyassert


def test1():
    assert_that(get_int()).is_equal_to(1)


def test2():
    assert_that(get_int()).is_not_none()


def test3():
    assert_that(get_int()).is_instance_of(int)
