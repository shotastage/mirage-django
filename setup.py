# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages
from mirageframework.version import __version__ as ver
import sys


sys.path.append('./mirageframework')
sys.path.append('./miragecore')
sys.path.append('./console')
sys.path.append('./tests')


if __name__ == "__main__":
    setup(
        name = "mirageframework",
        version = ver,
        author = "Shota Shimazu",
        author_email = "hornet.live.mf@gmail.com",
        classifiers=[
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
        ],
        packages = find_packages(exclude=('tests', 'shell')),
        include_package_data = True,
        zip_safe = False,
        install_requires = [
            "django"
        ],
        entry_points = {
            'console_scripts':[
                'mgc = console.mirage:main',
            ],
        },
        description = "Extended Django framework",
        long_description = "Advanced extended command line tool for Django.",
        url = "https://github.com/shotastage/mirageframework",
        license = "Apache",
        platforms = ["POSIX", "Windows", "Mac OS X"],
        # test_suite = "mirageframework_test.suite",
    )
