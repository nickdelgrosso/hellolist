from setuptools import setup

setup(name='hellolist',
      version='1.0',
      description='Python Distribution Utilities',
      author='Greg Ward',
      author_email='gward@python.net',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['hellolist'],
      entry_points={
          'console_scripts': [
              'hellolist = hellolist.__main__:main',
            ]
      }

     )
