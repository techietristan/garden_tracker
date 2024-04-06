import sys

def prompt(prompt: str) -> str:
    response: str = input(prompt)
    if response.lower() in ['q', 'quit', 'e', 'exit']:
        sys.exit(0)
    return response