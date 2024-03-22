import subprocess
from argparse import ArgumentParser
from typing import Optional


def _parse_args():
    """
    Parses user command line arguments.
    """

    parser = ArgumentParser(
        description="Create JIRA issue using jira-cli. See https://github.com/ankitpokhrel/jira-cli."
    )
    parser.add_argument("--title", "-t", required=True, help="Title of the story")
    parser.add_argument("--body", "-b", required=True, help="Description of the story")
    parser.add_argument(
        "--project",
        "-p",
        required=True,
        help="Project board, e.g. 'AIR' or 'LPO'",
    )
    parser.add_argument(
        "--story-points",
        "-s",
        type=int,
        required=True,
        help="Use fibonacci sequence, e.g 1, 2, 3, 5, 8, 13.",
    )
    parser.add_argument("--assignee", "-a", required=False, default="aalfieri")
    parser.add_argument("--reporter", "-r", required=False, default="aalfieri")
    parser.add_argument("--component", required=False, help="Component of the story, e.g. DataRepo")
    args = parser.parse_args()
    return args


def main(
    title: str,
    body: str,
    story_points: int,
    project: str,
    assignee: str,
    reporter: str,
    component: Optional[str] = None,
):
    command = [
        "jira",
        "issue",
        "create",
        "--type",
        "Story",
        "-s",
        title,
        "--body",
        body,
        "--assignee",
        assignee,
        "--reporter",
        reporter,
        "--custom=story-points=" + str(story_points),
        "--project",
        project,
        # "--no-input",
    ]
    if component:
        command.extend(["--component", component])
    print(" ".join(command))
    subprocess.run(command)


if __name__ == "__main__":
    args = _parse_args()
    print(args)
    main(**vars(args))
