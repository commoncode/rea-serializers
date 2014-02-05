from setuptools import setup, find_packages

setup( name='rea-serializers',
    version = '0.0.1',
    description = 'Serializers for REA',
    author = 'Daryl Antony',
    author_email = 'daryl@commoncode.com.au',
    url = 'https://github.com/commoncode/rea-serializers',
    keywords = ['django',],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    dependency_links = [
        'http://github.com/commoncode/rea/tarball/master#egg=rea-0.0.2',
    ],
    install_requires = [
        'rea',
        'djangorestframework',
    ]
)
