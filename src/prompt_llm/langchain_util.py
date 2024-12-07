import os
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from .models import Configuration

def get_model_to_invoke(config: dict):
    model, api_key, provider, temperature = config["model"], config["api_key"], config["provider"], config["temperature"]
    model_to_invoke = None

    if provider == 'openai':
        os.environ["OPENAI_API_KEY"] = api_key
        model_to_invoke = ChatOpenAI(model=model, temperature=temperature)
    elif provider == 'mistralai':
        os.environ["MISTRAL_API_KEY"] = api_key
        model_to_invoke = ChatMistralAI(model=model, temperature=temperature)

    return model_to_invoke


def call(prompt: str, config: dict):
    model_to_invoke = get_model_to_invoke(config)

    # Messages
    messages_langchain = []
    messages_langchain.append(SystemMessage(content=config["system"]))
    messages_langchain.append(HumanMessage(content=prompt))

    response = model_to_invoke.invoke(messages_langchain)

    return response
