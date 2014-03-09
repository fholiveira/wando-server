from setuptools import setup

setup(
    name='wando',
    version='0.1.1',
    url='http://packages.python.org/flask-environments/',
    license='BSD',
    author='Fernando Oliveira',
    author_email='fernando@fholiveira.com',
    description='Environment tools and configuration for Flask applications',
    long_description=open('README.rst').read(),
    py_modules=['wando'],
    zip_safe=False,
    platforms='any',
    install_requires=['blessings', 'colorama', 'werkzeug'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
