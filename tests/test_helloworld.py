# tests/test_helloworld.py

from helloworld.hello import HelloWorld


def test_hello():
    hw = HelloWorld()
    assert hw.hello() == "Hello, world!"


def test_greet():
    hw = HelloWorld()
    assert hw.greet() == "Hello nobody"
