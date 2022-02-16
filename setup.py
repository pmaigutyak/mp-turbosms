
from setuptools import setup, find_packages


__version__ = '3.5.2'


with open('requirements.txt') as f:
    requires = f.read().splitlines()


url = 'https://github.com/pmaigutyak/mp-turbosms'


setup(
    name='django-turbosms',
    version=__version__,
    description='Turbosms.ua django integration app',
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url=url,
    download_url='{}/archive/{}.tar.gz'.format(url, __version__),
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    install_requires=requires
)
