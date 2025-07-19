from pathlib import Path

from dotenv import load_dotenv
from invoke import Collection, task

# load .env from project root
project_root = Path(__file__).parent
load_dotenv(project_root / ".env")


@task
def bump(c):
    """
    Determine next version, update pyproject.toml & CHANGELOG, commit & tag.
    Usage: invoke bump
    """
    c.run("poetry run semantic-release version", pty=True)


@task(bump)
def build(c):
    """
    Build sdist and wheel for the newly bumped version.
    Usage: invoke build
    """
    c.run("poetry build", pty=True)


@task(build)
def publish(c):
    """
    Push commits & tags, create GitHub Release, and upload dists.
    Usage: invoke publish
    """
    c.run("poetry run semantic-release publish", pty=True)


@task
def version(c):
    """
    Run semantic‑release in no‐op mode to show the next version.
    Usage: invoke version
    """
    # now GH_TOKEN is loaded from .env
    c.run("poetry run semantic-release --noop version --print", pty=True)


@task
def fmt(c):
    """
    Auto‑format code: reorder imports with isort and apply Black formatting.
    Usage: invoke fmt
    """
    # reorder imports in place
    c.run("poetry run isort .", pty=True)
    # format code with Black
    c.run("poetry run black .", pty=True)


@task
def lint(c):
    """
    Run all lint checks: Black, isort, and Flake8.
    Usage: invoke lint
    """
    # Black in check‐only mode (won’t reformat)
    c.run("poetry run black --check .", pty=True)
    # isort in check‐only mode (won’t reorder)
    c.run("poetry run isort --check .", pty=True)
    # flake8 always only reports problems
    c.run("poetry run flake8 .", pty=True)


# … rest of your tasks/namespace setup …
@task
def test(c):
    """
    Run the full pytest suite.
    Usage: invoke test
    """
    c.run("poetry run pytest", pty=True)


# Create a namespace and add tasks
ns = Collection()
ns.add_task(version)
ns.add_task(bump)
ns.add_task(publish)
ns.add_task(fmt)
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
