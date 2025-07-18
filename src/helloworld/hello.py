# src/helloworld/hello.py


class HelloWorld:
    """Simple example class."""

    def greet(self) -> str:
        return "Hello, world!"


if __name__ == "__main__":
    hw = HelloWorld()
    print(hw.greet())
