from setuptools import setup, find_packages

setup(
    name="math-quiz",  # Choose a unique name for your package
    version="0.1.0",
    description="A simple math quiz game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/your-repo",  # Replace with your repository URL
    license="MIT",
    packages=find_packages(where="src"),  # Specify package directory
    package_dir={"": "src"},
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
