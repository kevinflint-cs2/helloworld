# tests/test_helloworld.py

from helloworld.hello import HelloWorld


def test_hello():
    """
    hello() should return the classic
    'Hello, world!' greeting with punctuation.
    """
    hw = HelloWorld()
    result = hw.hello()
    assert result == "Hello, world!", f"hello() returned {result!r}"


def test_greet():
    """
    greet() should default to 'nobody' when no name is passed.
    """
    hw = HelloWorld()
    result = hw.greet()
    expected = "Hello nobody"
    msg = f"greet() returned {result!r}, " f"expected {expected!r}"
    assert result == expected, msg
