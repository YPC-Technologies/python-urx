from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
            packages=['urx'],
            package_dir={'': './'},
            install_requires=["numpy", "math3d"],
        )

setup(**setup_args)