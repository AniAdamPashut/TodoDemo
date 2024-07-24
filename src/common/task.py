from dataclasses import dataclass


@dataclass
class Task:
    name: str
    is_completed: bool