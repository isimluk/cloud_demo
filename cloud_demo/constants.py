import os

# This should really rather become config option
CACHE_DIR = os.path.join(os.path.expanduser('~'), '.cloud_demo/cache/')

AWS_CLOUD_SOLUTIONS_REPO_NAME = 'Cloud-AWS'
AWS_CLOUD_SOLUTIONS_REPO_GIT = 'https://github.com/CrowdStrike/' + AWS_CLOUD_SOLUTIONS_REPO_NAME
