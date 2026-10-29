"""
AI Number Guessing Game — 猜数字游戏
 
A clean, object-oriented Python game where the player tries to guess
a randomly generated number.  After each guess the game tells you
whether your guess was too high, too low, or exactly right.
 
Usage:
python guess_number.py           # interactive play
python guess_number.py --demo    # auto-run a demo round
"""
 
import random
import sys
 
 
class GuessNumberGame:
"""Core game logic.  Pure methods — no I/O — so it is easy to test."""
 
def __init__(self, low: int = 1, high: int = 100, max_attempts: int | None = None):
if low >= high:
raise ValueError("low must be less than high")
self.low = low
self.high = high
self.target = random.randint(low, high)
self.max_attempts = max_attempts
self.guess_count = 0
self.game_over = False
self.won = False
 
def guess(self, num: int) -> str:
"""Register one guess and return a hint string."""
if self.game_over:
return "Game is already over. Start a new one."
if num < self.low or num > self.high:
return f"Out of range! Pick a number between {self.low} and {self.high}."
 
self.guess_count += 1
 
if num == self.target:
self.game_over = True
self.won = True
return (
f"🎉 Correct! You guessed {self.target} in {self.guess_count} "
f"attempt{'s' if self.guess_count != 1 else ''}."
)
 
if self.max_attempts and self.guess_count >= self.max_attempts:
self.game_over = True
self.won = False
return (
f"💥 Out of attempts! The number was {self.target}."
)
 
hint = "too high ⬇️" if num > self.target else "too low ⬆️"
remaining = ""
if self.max_attempts:
remaining = f" ({self.max_attempts - self.guess_count} left)"
return f"Your guess is {hint}{remaining}. Try again."
 
def reset(self) -> None:
"""Start a fresh round with a new random target."""
self.target = random.randint(self.low, self.high)
self.guess_count = 0
self.game_over = False
self.won = False
 
 
def play(game: GuessNumberGame) -> None:
"""Interactive CLI loop."""
print(
f"🎯 Number Guessing Game — range {game.low}..{game.high}"
+ (
f"  (max {game.max_attempts} attempts)"
if game.max_attempts
else "  (unlimited attempts)"
)
)
print("Type 'quit' at any time to exit.\n")
 
while not game.game_over:
raw = input("Your guess: ").strip()
if raw.lower() in {"quit", "exit", "q"}:
print(f"👋 Quitting — the number was {game.target}.")
return
try:
n = int(raw)
except ValueError:
print("Please enter an integer.\n")
continue
print(game.guess(n))
print()
 
 
def demo() -> None:
"""Auto-run a few deterministic guesses against a fresh game."""
game = GuessNumberGame(low=1, high=10, max_attempts=5)
# Force target to a known value so the demo script is reproducible.
game.target = 7
print("=== DEMO MODE (target forced to 7) ===\n")
for attempt in [3, 9, 7]:
print(f"Guessing {attempt} → {game.guess(attempt)}")
print()
 
 
if __name__ == "__main__":
if "--demo" in sys.argv:
demo()
else:
# Default: interactive game with optional difficulty presets.
try:
play(GuessNumberGame(low=1, high=100))
except KeyboardInterrupt:
print("\n👋 Bye!")
