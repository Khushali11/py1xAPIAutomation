# pip install python-dotenv
from dotenv import load_dotenv
import os
import pytest


def test_auth():
    load_dotenv()

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username, password)
