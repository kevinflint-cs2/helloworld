# src/helloworld/hello.py


class HelloWorld:
    """
    A simple HelloWorld class that can return greetings.
    """

    def __init__(self) -> None:
        """
        Initialize a new HelloWorld instance.
        """
        pass

    def greet(self, name: str = "nobody") -> str:
        """
        Generate a personalized greeting.

        Args:
            name (str): The name of the person to greet. Defaults to 'nobody'.

        Returns:
            str: A greeting string, e.g., 'Hello Alice'.
        """
        self.name = name
        return f"Hello {self.name}"

    def hello(self) -> str:
        """
        Return the classic "Hello, world!" message.

        Returns:
            str: The string "Hello, world!!".
        """
        return "Hello, world!!"


if __name__ == "__main__":
    hw = HelloWorld()
    print(hw.hello())
