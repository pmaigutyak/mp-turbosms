
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='turbosms',
    version='1.0.0',
    description='Turbosms.ua django integration app',
    long_description=open('README.md').read(),
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url='https://github.com/pmaigutyak/mp-turbosms',
    packages=['turbosms'],
    license='MIT'
)
