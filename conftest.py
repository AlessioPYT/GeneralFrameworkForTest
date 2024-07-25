import pytest
from driver import Driver


@pytest.fixture(scope=function, autouse=False)
def driver():
    Driver.start()
    workingWeb = Driver.open_browser()
    yield workingWeb
    Driver.stop()