from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

requirements = [
    'npyscreen'
]

entry_points = {
    'console_scripts': [
        'pennyworth = pennyworth.__main__:main'
    ]
}

setup(
    name='pennyworth',
    keywords='pennyworth',
    version='0.0.1',
    author='Josh Crank',
    author_email='joshuatcrank@gmail.com',
    description='A task management TUI',
    long_description=long_description,
    long_description_type='text/markdown',
    url='https://github.com/jtcrank/pennyworth',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: :: MIT License',
        'Operating System :: OS Independent'
    ],
    install_requires=requirements,
    packages=find_packages(),
    include_package_data=True,
    entry_points=entry_points,
)


