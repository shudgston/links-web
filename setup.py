from setuptools import find_packages, setup


setup(
    name='links-web',
    version='0.0.1',
    author='Sean Hudgston',
    packages=find_packages(),
    # read MANIFEST.in
    include_package_data=True,
    install_requires=[
        'clean-architecture-python==0.0.1',
        'Flask==0.12.1',
        'Flask-Bootstrap==3.3.7.1',
        'Flask-WTF==0.14.2',
        'Flask-Login==0.4.0',
        'gunicorn==19.7.1'
    ]
)
