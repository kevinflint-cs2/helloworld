from pathlib import Path

from dotenv import load_dotenv
from invoke import Collection, task

# load .env from project root
project_root = Path(__file__).parent
load_dotenv(project_root / ".env")

msg_help_bump = "Which part to bump: 'patch', 'minor', or 'major' (default: patch)"


@task(help={"level": msg_help_bump})
def bump(c, level="patch"):
    """
    Bump the project version (pyproject.toml), commit, tag, and push.

    Usage:
      invoke bump           # does a patch bump
      invoke bump --level=minor
      invoke bump --level=major
    """
    # 1) bump version in pyproject.toml and capture the new version
    result = c.run(f"poetry version {level}", hide="both")
    new_version = result.stdout.strip()
    print(f"📦 Bumped version to {new_version}")

    # 2) commit the change
    run_git_commit = f'git commit -m "chore(release): bump version to {new_version}"'
    c.run("git add pyproject.toml", pty=True)
    c.run(run_git_commit, pty=True)

    # 3) create the tag
    c.run(f"git tag v{new_version}", pty=True)

    # 4) push commit & tags
    c.run("git push --follow-tags", pty=True)
    print("🚀 Pushed commit and tags to origin")


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
    Run all lint checks: Black, isort, and Flake8 (ignoring E501).
    Usage: invoke lint
    """
    # Black in check‐only mode (won’t reformat)
    c.run("poetry run black --check .", pty=True)
    # isort in check‐only mode (won’t reorder)
    c.run("poetry run isort --check .", pty=True)
    # flake8 ignoring line-too-long errors
    c.run("poetry run flake8 . --ignore=E501", pty=True)


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
ns.add_task(bump)
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
