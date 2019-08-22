import setuptools
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


# I took it from catalyst setup.py https://github.com/catalyst-team/catalyst/blob/master/setup.py
def load_version():
    context = {}
    with open(os.path.join(PROJECT_ROOT, "geom_tools", "version.py")) as f:
        exec(f.read(), context)
    return context["__version__"]


setuptools.setup(
    name="geom_tools",
    version=load_version(),
    author="Daiver",
    author_email="ra22341@ya.ru",
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(exclude=("tests",)),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
