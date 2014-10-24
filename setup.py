from setuptools import setup, find_packages

setup(
    name = 'portality',
    version = '0.1.1',
    packages = find_packages(),
    install_requires = [
        "Flask==0.10.1",
        "Flask-Login==0.2.7",
        "Flask-WTF==0.9.3",
        "Markdown==2.3.1",
        "WTForms==1.0.5",
        "Werkzeug==0.9.6",
        "requests==2.1.0",
        "lxml"
    ],
    url = 'http://cottagelabs.com',
    author = 'Cottage Labs',
    author_email = 'us@cottagelabs.com',
    description = 'Open Access button infrastructure',
    license = 'Copyheart',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Copyheart',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
