import pytest
import os
import sys
import inspect
import lib


def test_fake_user():
    assert lib.get_user_flows("Fake Yser") == []

def test_empty_string():
    assert lib.get_user_flows("") == []

def test_alec():
    assert lib.get_user_flows("alec") == []

