from setuptools import setup

setup(
    name="prompt_llm",
    version="0.1.0",
    py_modules=["src.main"],
    install_requires=["typer", "langchain-core", "langchain-openai", "langchain-mistralai"],
    entry_points={
        "console_scripts": [
            "prompt_llm=src.main:app",
        ],
    },
)
