import pytest


@pytest.mark.smoke
def test_my():
    pass


@pytest.mark.skip('Функционал сломан')
@pytest.mark.acceptance
def test_my1():
    assert False

