import pytest


def always_returns_true():
    print("This will always return True")
    return True


def test_always_returns_true():
    assert always_returns_true()
