from invoke import Collection, task


@task
def lint(c):
    """
    Run all lint checks: Black, isort, and Flake8.
    Usage: invoke lint
    """
    # Black (check-only)
    c.run("poetry run black .", pty=True)
    # isort (check-only)
    c.run("poetry run isort .", pty=True)
    # Flake8
    c.run("poetry run flake8 .", pty=True)


@task
def test(c):
    """
    Run the full pytest suite.
    Usage: invoke test
    """
    c.run("poetry run pytest", pty=True)


# Create a namespace and add tasks
ns = Collection()
ns.add_task(lint)
ns.add_task(test)


@task(default=True)
def help(c):
    """
    Show available tasks
    """
    print("Available tasks:\n")
    for name, task_obj in ns.tasks.items():
        print(f"  {name:10} — {task_obj.__doc__.strip()}")


ns.add_task(help)
