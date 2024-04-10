from dataclasses import dataclass

@dataclass

class User:
    name: str
    email: str
    password: str


krishna = User('krishna', 'krishna@gmail.com', 'krishna123')

print(krishna.name)