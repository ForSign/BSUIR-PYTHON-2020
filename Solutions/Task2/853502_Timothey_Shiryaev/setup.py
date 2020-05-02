import setuptools

with open("README.md", "r") as f:
    description = f.read()

setuptools.setup(
    name="lab_2_Timothey_Shiryaev",
    version="1.2",
    author="Shiryaev_Timothey",
    author_email="tim.shiryaev@gmail.com",
    description="testing setup py : )",
    long_description=description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.8.2',
)