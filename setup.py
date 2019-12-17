"""Distribution to pipy"""

from setuptools import setup, find_packages

with open("README.md") as readme:
    long_description = readme.read()

setup(
    name='tf_rl',
    version='1.0.0',
    long_description=long_description,
    url='https://github.com/dickreuter/tf_rl',
    author='Nicolas Dickreuter',
    author_email='dickreuter@gmail.com',
    license='MIT',
    description=('Framework for reinforcement learning.'),
    packages=find_packages(exclude=['tests', 'gym_env', 'tools']),
    install_requires=['pyglet', 'pytest', 'pandas', 'pylint', 'gym', 'numpy', 'matplotlib', 'tensorflow'],
    platforms='any',
)
