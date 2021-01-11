import os
from functools import cached_property
from .common import BaseWizard
from cloud_demo.aws.ssm import S3BucketUpdater, SSMPackageBuilder, SSMPackageUpdater
from cloud_demo.solution_templates import aws_ssm_package_template


class AwsSsmDistributorPackage(BaseWizard):
    """
    Wizard that automates creation of Distributor Package within AWS Systems Manager.

    Distributor package can then used to deploy falcon sensor.
    """
    def __init__(self, installer_type=None, aws_region=None, package_name=None, s3_bucket_name=None):
        self.package_type = self._ask(
            'installer_type', """

Downloading installer is small AWS SSM Package that downloads the latest greatest
Falcon sensor from CrowdStrike platform. Downloading installer requires falcon API
keys to be stored in AWS SSM Parameter Store.

Bundled installer is slightly bigger AWS SSM Package that contains all Falcon Sensor
packages bundled. That means you may want to refresh this package periodically.
Suitable for bigger environments as it does not hit download limits

Type""", installer_type, options=('downloading', 'bundled'))
        self.aws_region = self._ask(
            'aws_region', 'package will appear in this region',
            aws_region)
        self.package_name = self._ask(
            'package_name', 'will appear in AWS SSM Distributor',
            package_name, default='falcon-agent')
        self.s3_bucket_name = self._ask(
            's3_bucket_name', 'package contents will be uploaded here',
            s3_bucket_name, default='falcon-agent')
        if installer_type == 'bundled':
            raise NotImplementedError("Installer type bundled is not yet implemented")

    def run(self):
        files = self.build_package()
        self.upload_package(files)
        self.upload_parametes()

    def build_package(self):
        return SSMPackageBuilder().build(self._dir)

    def upload_package(self, files):
        S3BucketUpdater(self.aws_region).update(self.s3_bucket_name, files)
        SSMPackageUpdater(self.aws_region).update(
            self.package_name, self.s3_bucket_name, os.path.join(self._dir, "manifest.json"))

    @cached_property
    def _dir(self):
        return aws_ssm_package_template()

