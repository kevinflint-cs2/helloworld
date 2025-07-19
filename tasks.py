from pathlib import Path

from dotenv import load_dotenv
from invoke import Collection, Context, task

# load .env from project root
project_root = Path(__file__).parent
load_dotenv(project_root / ".env")


@task  # type: ignore[misc]
def docstyle(c: Context) -> None:
    """
    Run pydocstyle to enforce docstring conventions.

    Usage: invoke docstyle
    """
    # point at your source (and tests if you like)
    c.run("poetry run pydocstyle src/helloworld tests", pty=True)


@task  # type: ignore[misc]
def fmt(c: Context) -> None:
    """
    Auto‑format code: reorder imports with isort and apply Black formatting.

    Usage: invoke fmt
    """
    # reorder imports in place
    c.run("poetry run isort .", pty=True)
    # format code with Black
    c.run("poetry run black .", pty=True)


@task  # type: ignore[misc]
def lint(c: Context) -> None:
    """
    Run all lint checks: Black, isort, and Flake8 (ignoring E501).

    Usage: invoke lint
    """
    # Black in check‐only mode (won’t reformat)
    c.run("poetry run black --check .", pty=True)
    # isort in check‐only mode (won’t reorder)
    c.run("poetry run isort --check .", pty=True)
    # flake8 ignoring line-too-long errors
    c.run("poetry run flake8 . --ignore=E501", pty=True)


@task  # type: ignore[misc]
def sync(c: Context) -> None:
    """
    Fully sync local main branch to origin/main, discarding all local changes.

    Usage: invoke sync
    """
    # ensure we’re on main
    c.run("git checkout main", pty=True)
    # fetch + prune deleted remotes
    c.run("git fetch origin --prune", pty=True)
    # hard reset to remote state
    c.run("git reset --hard origin/main", pty=True)
    # remove untracked files and dirs
    c.run("git clean -fd", pty=True)


@task  # type: ignore[misc]
def test(c: Context) -> None:
    """
    Run the full pytest suite.

    Usage: invoke test
    """
    c.run("poetry run pytest", pty=True)


@task  # type: ignore[misc]
def typecheck(c: Context) -> None:
    """
    Run MyPy static type checks.

    Usage: invoke typecheck
    """
    # Point at your source package directory (adjust as needed)
    c.run("poetry run mypy src/helloworld tests", pty=True)


# Create a namespace and add tasks
ns = Collection()
ns.add_task(docstyle)
ns.add_task(fmt)
ns.add_task(lint)
ns.add_task(sync)
ns.add_task(test)
ns.add_task(typecheck)


@task(default=True)  # type: ignore[misc]
def help(c: Context) -> None:
    """
    Show available tasks.

    Usage: invoke help
    """
    print("Available tasks:\n")
    for name, task_obj in ns.tasks.items():
        print(f"  {name:10} — {task_obj.__doc__.strip()}")


ns.add_task(help)
