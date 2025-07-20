# src/helloworld/__main__.py

from .hello import HelloWorld


def main() -> None:
    """Entry point for `python -m helloworld`."""
    hw = HelloWorld()
    print(hw.hello())


if __name__ == "__main__":
    main()
