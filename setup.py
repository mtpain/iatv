from distutils.core import setup

required_packages = [
    'appnope==0.1.0',
    'backports.shutil-get-terminal-size==1.0.0',
    'beautifulsoup4==4.4.1',
    'breadability==0.1.20',
    'chardet>=2.3.0',
    'cookies==2.2.1',
    'cssutils==1.0.1',
    'decorator==4.0.10',
    'docopt==0.6.2',
    'enum34==1.1.6',
    'funcsigs==1.0.2',
    'future==0.15.2',
    'lxml>=3.6.1',
    'mock==2.0.0',
    'nltk==3.2.1',
    'nose==1.3.7',
    'numpy>=1.11.1',
    'pathlib2==2.1.0',
    'pbr==1.10.0',
    'pexpect==4.2.1',
    'pickleshare==0.7.4',
    'progressbar2==3.10.1',
    'prompt-toolkit>=1.0.7',
    'ptyprocess==0.5.1',
    'py==1.4.31',
    'pycaption==1.0.0',
    'pytest==3.0.4',
    'python-dateutil==2.5.3',
    'python-utils==2.0.0',
    'requests>=2.10.0',
    'responses==0.5.1',
    'simplegeneric==0.8.1',
    'six==1.10.0',
    'sumy==0.4.1',
    'wcwidth==0.1.7'
]

setup(
    name='iatv',
    version='0.1',
    description='Tools for scraping archive.org\'s TV News Archive',
    author='Matthew Turner',
    author_email='maturner01@gmail.com',
    install_requires=required_packages,
    packages=['iatv']
)
