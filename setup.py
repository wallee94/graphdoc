import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="graphdoc",
    version="0.3.0",
    author="Walther Lee",
    author_email="walthere.lee@gmail.com",
    description="Generate HTML docs for your GraphQL API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wallee94/graphdoc",
    packages=setuptools.find_packages(),
    package_data={'graphdoc': ['templates/*.html']},
    install_requires=[
        'graphql-core>=2.1.0,<4',
        'Jinja2>=2',
        'markdown2>=2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
