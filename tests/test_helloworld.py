# tests/test_helloworld.py

from helloworld.hello import HelloWorld


def test_greet():
    hw = HelloWorld()
    assert hw.greet() == "Hello, world! Woo Hoo!"
