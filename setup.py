from setuptools import find_packages, setup


version = '0.1.0'


setup(
    name='django-api-examples',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='Test helpers for django rest api examples.',
    long_description=open('README.md').read(),
    author='Incuna',
    author_email='admin@incuna.com',
    url='https://github.com/incuna/django-api-examples/',
    install_requires=[],
    zip_safe=False,
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Testing',
    ],
)
