from dataclasses import asdict, dataclass
from flask import Flask
import json

app = Flask(__name__)

@dataclass
class Cell:
    clue: str
    answer: str
    answered: bool

cell = Cell(
    "This is a clue",
    "What is the question",
    False
)

@dataclass
class Category:
    name: str
    cells: [Cell]

bogus = [cell for x in range(10)]

@dataclass
class Player:
    name: str
    balance: int

@dataclass
class Game:
    categories: [Category]
    values: [int]
    players: [Player]

game = Game(
    categories = [
        Category("Flatulence", bogus),
        Category("Loud Noises", bogus),
        Category("Backhanded Complements", bogus)
    ],
    values = [100, 200, 300, 400, 800, 1000],
    players = [
        Player("Stu Pidassle", 0),
        Player("Seeymour Butts", 0),
        Player("Amanda Huyginchiss", 0)
    ]
)

@app.route("/state")
def state():
    global game
    return json.dumps(asdict(game))

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
