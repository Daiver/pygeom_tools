import setuptools
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


# I took it from catalyst setup.py https://github.com/catalyst-team/catalyst/blob/master/setup.py
def load_version():
    context = {}
    with open(os.path.join(PROJECT_ROOT, "geom_tools", "version.py")) as f:
        exec(f.read(), context)
    return context["__version__"]


class GetPybindInclude(object):
    """Helper class to determine the pybind11 include path
    The purpose of this class is to postpone importing pybind11
    until it is actually installed, so that the ``get_include()``
    method can be invoked. """

    def __init__(self, user=False):
        self.user = user

    def __str__(self):
        import pybind11
        return pybind11.get_include(self.user)


ext_modules = [
    setuptools.Extension(
        'geom_tools.obj_import_cpp',
        ['geom_tools/csrc/obj_import_cpp.cpp'],
        include_dirs=[
            GetPybindInclude(),
            GetPybindInclude(user=True)
        ],
        language='c++',
        extra_compile_args=['-std=c++17'],
    ),
]

setuptools.setup(
    name="geom_tools",
    version=load_version(),
    author="Daiver",
    author_email="ra22341@ya.ru",
    description="Simple tools for wavefront obj IO and processing.",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/Daiver/pygeom_tools",
    packages=setuptools.find_packages(exclude=["tests", ]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    ext_modules=ext_modules,
    install_requires=['wheel', 'pybind11>=2.4', 'numpy>=1.14'],
    setup_requires=['pybind11>=2.4'],
)
