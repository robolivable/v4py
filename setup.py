from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='v4py',
      version='0.1a0',
      description='Video tool set for Python.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: C++',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Video',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Terminals',
        'Topic :: Utilities',
      ],
      keywords='',
      url='https://github.com/robolivable/v4py',
      author='Robert Oliveira',
      author_email='oliveira.rlde@gmail.com',
      license='MIT',
      packages=['v4py'],
      scripts=[],
      install_requires=[])
