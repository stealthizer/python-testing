"""
python-testing examples
"""

from setuptools import setup, find_packages


setup(
    name='python-testing',
    description='Some example tests for python',
    url='',
    author='stealthizer',
    author_email='stealthizer@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
    keywords='testing examples',
    packages=find_packages(exclude=['tests']),
    include_package_data=True
)
