from setuptools import setup


long_description = '\n'.join((
    open('README.rst').read(),
    open('CHANGELOG.rst').read(),
    ''
))

setup(
    name='portolano',
    long_description=long_description,

    packages=['portolano'],
    include_package_data=True,

    install_requires=[
        'connexion',
        'flask_fs[all]',
    ],
)
