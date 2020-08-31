

from setuptools import setup, find_packages

REQUIREMENTS = [
    'Django>=1.11',
    'django-admin-sortable2>=0.6.10',
    'django-cms>=3.3',
]

# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
]

setup(
    name='cmsplugin-socialsharekit',
    version="0.2.0",
    description='Allows embeding Social Share Kit into the site',
    author='Mathieu Meylan',
    author_email='m.meylan@gmail.com',
    url='https://github.com/matinfo/cmsplugin-socialsharekit',
    packages=find_packages(),
    license='LICENSE',
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False,
)

