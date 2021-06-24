from setuptools import setup, find_packages

setup(
    name="progen",
    packages=find_packages(),
    version="0.0.2",
    license="MIT",
    description="ProGen",
    author="Phil Wang",
    author_email="",
    url="https://github.com/lucidrains/progen",
    keywords=[
        "artificial intelligence",
        "deep learning",
        "protein language model"
    ],
    install_requires=[
        "biopython",
        "click",
        "click-option-group",
        "einops>=0.3",
        "dm-haiku",
        "humanize",
        "jax",
        "jaxlib",
        "optax",
        "torch",
        "tqdm"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
)
