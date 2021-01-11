import os
from functools import cached_property
from git import Repo
from cloud_demo import constants


class Git():
    def __init__(self, name, repo_url):
        self.name = name
        self.repo_url = repo_url

    def path(self, subdir):
        return os.path.join(self._dir, subdir)

    @cached_property
    def _dir(self):
        os.makedirs(constants.CACHE_DIR, mode=0o700, exist_ok=True)
        d = os.path.join(constants.CACHE_DIR, self.name)
        if os.path.exists(d):
            repo = Repo.init(d)
            assert repo.__class__ is Repo
            origin = repo.remotes.origin
            origin.fetch()
            origin.pull()
        else:
            repo = Repo.clone_from(self.repo_url, self.d)
        return d


cloud_aws = Git(constants.AWS_CLOUD_SOLUTIONS_REPO_NAME, constants.AWS_CLOUD_SOLUTIONS_REPO_GIT)


def aws_ssm_package_template():
    return cloud_aws.path('systems-manager/Packaging utilities')
