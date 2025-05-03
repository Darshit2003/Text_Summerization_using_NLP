import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    

__version__ = "0.0.0"
REPO_NAME = "Text_Summerization_using_NLP"
AUTHOR_USER_NAME = "Darshit2003"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "darshitsheth333@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
