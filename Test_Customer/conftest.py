# -*- coding:utf-8 -*-
# Author : Longhai
import pytest
from tools.ui.base_ui import BaseUI


@pytest.fixture(scope='session')
def driver():
    base = BaseUI()
    # 打开浏览器
    base.start_browser("headless")
    yield base
