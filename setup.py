from setuptools import setup, find_packages
import io
import re

longdesc = ''

with io.open('README.md', 'rt', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        if len(re.findall('align="*', line)) == 0:
            longdesc += line


setup(
    name='zhouyuanzhen',
    license='Apache License 2.0',
    version='0.1.0',
    maintainer='Yuanzhen Zhou',
    maintainer_email='szrednick@gmail.com',
    packages=find_packages(include=['zyz', 'zyz.*']),
    zip_safe=False,
    include_package_data=True,
    url='https://github.com/zhouyuanzhen/py-zhouyuanzhen',
    author='Yuanzhen Zhou',
    author_email='szrednick@gmail.com',
    description='A PyPI project of zhouyuanzhen',
    long_description=longdesc,
    install_requires=[],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
