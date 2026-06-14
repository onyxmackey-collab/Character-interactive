import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class Character:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality
        self.memory = []

    def act(self):
        # Character does something autonomously
        prompt = f"You are {self.name}. Personality: {self.personality}. What do you do next in the game box?"
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
        action = response.choices[0].message.content
        self.memory.append(action)
        return f"{self.name} does: {action}"

    def talk_to(self, user_message):
        prompt = f"You are {self.name}. Personality: {self.personality}. Previous memories: {self.memory[-3:]}. User says: {user_message}. Respond naturally."
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
        reply = response.choices[0].message.content
        self.memory.append(f"User: {user_message} | You: {reply}")
        return reply

# Example usage
if __name__ == "__main__":
    char = Character("Alex", "curious explorer who loves building things")
    print(char.act())
