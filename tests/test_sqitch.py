# -*- coding: utf-8 -*-
import pytest_sqitch
from pytest_sqitch.client import mysql

def test_help_message(mysql):
    print("hello world")

