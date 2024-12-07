#!/usr/bin/env python

import typer
import json

from .utils import add_to_config, remove_from_config, load_config
from .langchain_util import call

app = typer.Typer()

@app.command()
def add_config(api_key: str='', system: str = '', temperature:float = None):
    if api_key:
        add_to_config('api_key', api_key)

    if system:
        add_to_config('system', system)
    
    if temperature is not None:
        add_to_config('temperature', temperature)

@app.command()
def rm_config(key: str):    
    remove_from_config(key)


@app.command()
async def mistralai(prompt: str):
    app_config = load_config()

    if prompt:
        app_config["provider"] = "mistralai"
        app_config["model"] = "mistral-large-latest"

        response = await call(prompt, app_config)

        print(response)

@app.command()
def openai(prompt: str):
    """Tool to prompt openai"""
    app_config = load_config()

    if prompt:
        app_config["provider"] = "openai"
        app_config["model"] = "gpt-4o"

        response = call(prompt, app_config)

        print(response.content)

if __name__ == "__main__":
    app()
