from setuptools import setup, find_packages

version = '1.1'

setup(name='lazy',
      version=version,
      description='Lazy attributes for Python objects',
      long_description=open('README.txt').read() + '\n' +
                       open('CHANGES.txt').read(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      keywords='decorator lazy attribute',
      author='Stefan H. Holek',
      author_email='stefan@epy.co.at',
      url='http://pypi.python.org/pypi/lazy',
      license='BSD',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      test_suite='lazy.tests',
      install_requires=[
          'setuptools',
      ],
      use_2to3=True,
)
