from setuptools import setup, find_packages
import io

with io.open('README.md', 'rt', encoding='utf8') as f:
    lines = f.read()
    longdesc = lines

setup(
    name='zhouyuanzhen',
    license='Apache License 2.0',
    version='0.4.1',
    keywords='zyz, zhouyuanzhen, development',
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
    python_requires='>=3.5, <4',
    install_requires=[],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
