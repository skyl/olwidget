from setuptools import setup, find_packages

version = '0.1'

LONG_DESCRIPTION = """
=====================================
django-olwidget
=====================================

Reusable app for Django (http://djangoproject.com )
for creating maps with openlayers.
http://olwidget.org/olwidget/doc/django-olwidget.html


"""

setup(
    name='django-olwidget',
    version=version,
    description="django-olwidget",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='django,openlayers,',
    author='Charlie DeTarr',
    author_email='skylar.saveland@gmail.com',
    url='http://github.com/yourcelf/olwidget',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=['setuptools_git'],
)
