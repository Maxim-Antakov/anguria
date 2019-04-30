import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='anguria',
     version='0.1',
     scripts=['anguria'] ,
     author="Maxim Antakov",
     author_email="maxim.antakov@gmail.com",
     description="Specrun report smart parser",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Maxim-Antakov/anguria",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
