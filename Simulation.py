from character import Character

# Create your world
characters = [
    Character("Alex", "curious explorer"),
    Character("Luna", "quiet artist who observes everything"),
    Character("Max", "energetic builder")
]

print("=== Game Box Started ===\n")

# Autonomous loop (they do their own thing)
for _ in range(3):  # Run a few turns
    for char in characters:
        print(char.act())

# You interact
user_input = input("\nWhat do you say/do? ")
for char in characters:
    print(f"\n{char.name} replies: {char.talk_to(user_input)}")
