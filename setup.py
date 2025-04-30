from setuptools import setup, find_packages

setup(
    name="gp",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "gp = gp.__main__:main"
        ]
    },
    include_package_data=True,
    description="Python project generator CLI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Udit Saxena",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
