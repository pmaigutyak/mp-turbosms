
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='django-turbosms',
    version='1.1',
    description='Turbosms.ua django integration app',
    long_description=open('README.md').read(),
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url='https://github.com/pmaigutyak/mp-turbosms',
    download_url='https://github.com/pmaigutyak/mp-turbosms/archive/1.1.tar.gz',
    packages=['turbosms'],
    license='MIT'
)
