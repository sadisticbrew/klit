import os


class KlitDen(object):
    """A klit repository"""

    worktree = None
    klitdir = None
    conf = None

    def __init__(self, path, force=False):
        self.worktree = path
        self.klitdir = os.path.join(path, ".klit")

        if not (force or os.path.isdir(self.klitdir)):
            raise Exception(f"Not a Klit den {path}")

        if not force:
            vers = int(self.conf.get("core", "repositoryformatversion"))
            if vers != 0:
                raise Exception(f"unsupported repositoryformatversion: {vers}")


def den_file(repo, *path, mkdir=False):
    """Same as repo_path but create dirname(*path) if absent. Example, repo_file(r, \"refs\", \"remotes\", \"origin\", \"HEAD\") will create .git/refs/remotes/origin."""

    if repo_dir(repo, *path[:-1], mkdir=mkdir):
        return repo_path(repo, *path)


def repo_path(repo, *path):
    """Compute path under repo's gitdir."""
    return os.path.join(repo.klitdir, *path)


def repo_dir(repo, *path, mkdir=False):
    """Same as repo_path, but mkdir *path if absent if mkdir."""

    path = repo_path(repo, *path)

    if os.path.exists(path):
        if os.path.isdir(path):
            return path
        else:
            return Exception(f"Not a directory {path}")

    if mkdir:
        os.makedirs(path)
        return path
    else:
        return None


def repo_create(path):
    """Create a new repository at path."""

    repo = KlitDen(path, True)

    # First, we make sure the path either doesn't exist or is an empty dir.

    if os.path.exists(repo.worktree):
        if not os.path.isdir(repo.worktree):
            raise Exception(f"{path} is not a directory!")
        if os.path.exists(repo.klitdir) and os.listdir(repo.klitdir):
            raise Exception(f"{path} is not empty!")
    else:
        os.makedirs(repo.worktree)

    assert repo_dir(repo, "branches", mkdir=True)
    assert repo_dir(repo, "objects", mkdir=True)
    assert repo_dir(repo, "refs", "tags", mkdir=True)
    assert repo_dir(repo, "refs", "heads", mkdir=True)

    # .git/description
    with open(den_file(repo, "description"), "w") as f:
        f.write(
            "Unnamed repository; edit this file 'description' to name the repository.\n"
        )

    # .git/HEAD
    with open(den_file(repo, "HEAD"), "w") as f:
        f.write("ref: refs/heads/master\n")

    return repo


repo_create("/Users/palashkubsad/git_project/klit/")
