from setuptools import setup, find_packages

setup(
    name='CultureNet',
    version='0.1',
    description='CultureNet - сайт-платформа искусства и культуры',
    author='А.М. Синюхина, У.И. Загуменнов',
    author_email='sinyukhina.a.m@gmail.com',
    url='https://github.com/anmicksi/CultureNet',
    packages=find_packages(),
    install_requires=[
        'python-3.x',
        'Django==3.x',
        'djangorestframework',
        'psycopg2-binary',
    ],
    python_requires='>=3.6',
)
