from setuptools import setup, find_packages

setup(
    name="itinerary_creator",
    version="0.1",
    packages=find_packages(),
    description="Helps prints itineraries for some given flights",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Bhavish Pahwa",
    author_email="bhavishpahwa@gmail.com",
    url="https://github.com/bp-high/itinerary_creator",
    license="MIT",
    install_requires=['pytest==8.0.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

