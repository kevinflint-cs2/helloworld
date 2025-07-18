# src/helloworld/hello.py


class HelloWorld:
    """Simple example class."""

    def greet(self) -> str:
        return "Hello, world! Woo Hoo!"


if __name__ == "__main__":
    hw = HelloWorld()
    print(hw.greet())
