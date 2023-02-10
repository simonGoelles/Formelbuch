from setuptools import find_packages, setup
setup(
    name="kalender",
    version="1.0.0",
    author="Simon Gölles",
    author_email="goelle190028@sr.htlweiz.at",
    description="Formelheft",
    url="https://upstream",
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License"
          "Operating System :: OS Independent",
         ],
         package_dir={'': '.'},
         packages=find_packages(where='.'),
         python_requires='>=3.6',
        )