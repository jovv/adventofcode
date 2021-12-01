from typing import List
import os


def day(module: str) -> str:
    return module.split('.')[0]


def day_input(file) -> List[str]:
    with open(os.path.abspath(file)) as f:
        content = f.readlines()
    return content
