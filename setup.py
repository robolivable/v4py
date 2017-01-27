from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='v4py',
      version='0.1a0',
      description='Video toolset for Python.',
      long_description=readme(),
      classifiers=[],
      url='https://github.com/robolivable/v4py',
      author='Robert Oliveira',
      author_email='oliveira.rlde@gmail.com',
      packages=['v4py'],
      scripts=[],
      install_requires=[])
