"""
Tasks:
Setup and Initialization:
Create a program that asks the user to name their pet.
Initialize the pet’s attributes:
Hunger: 50
Happiness: 50
Energy: 50
(Values range from 0 to 100)
Pet Actions:
Implement functions for pet actions:
Feed: Increases hunger level.
Play: Increases happiness, decreases energy.
Rest: Increases energy, slightly decreases hunger.
Add interactive options to let the user choose an action.
Status Check:
Display the pet’s current stats after each action.
Game Rules:
If any attribute reaches 0, the pet gets "sick" and the game ends.
If all attributes are above 80 for three consecutive turns, the pet "wins" by becoming super happy and energetic.
Bonus Challenges:
Add a countdown timer for user input.
Include random events (e.g., the pet finds a toy that boosts happiness).
Create a save/load feature to resume the game later.
"""
import time
import random
import sys
import threading


PETT_FILE = "PETT.txt"


class MyPet:
    def __init__(self, name, hunger=50, happiness=50, energy=50, win_streak=0):
        self.pet_name = name
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.win_streak = win_streak

    def feed_pet(self):
        self.hunger = min(100, self.hunger + 20)
        if self.hunger <= 0:
            print("Game Over!!")
            sys.exit(0)
        print(f"\n{self.pet_name}'s hunger level increased to {self.hunger}")

    def play_pet(self):
        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 10)
        if self.happiness <= 0 or self.energy <= 0:
            print("Game Over!!")
            sys.exit(0)
        print(f"\n{self.pet_name}'s happiness increased to {self.happiness} and energy decreased to {self.energy}")

    def rest_pet(self):
        self.energy = min(100, self.energy + 20)
        self.hunger = max(0, self.hunger - 5)
        if self.hunger <= 0 or self.energy <= 0:
            print('Game Over!!!')
            sys.exit(0)
        print(f"\n{self.pet_name}'s energy increased to {self.energy} and hunger decreased to {self.hunger}")

    def check_win(self):
        if self.hunger > 80 and self.happiness > 80 and self.energy > 80:
            self.win_streak += 1
        
        if self.win_streak >= 3:
            print(f"\nCongratulations! {self.pet_name} is super happy and energetic! You win!")
            return True
        else:
            self.win_streak = 0
            return False

    def status_pet(self):
        print(f"\n{self.pet_name}'s Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")


def save_game(pet):
    with open(PETT_FILE, "w") as file:
        file.write(f"{pet.pet_name},{pet.hunger},{pet.happiness},{pet.energy},{pet.win_streak}")
        print("\nGame saved!")


def load_game():
    try:
        with open(PETT_FILE, "r") as file:
            data = file.read().split(",")
            
            pet = MyPet(data[0])
            pet.hunger = int(data[1])
            pet.happiness = int(data[2])
            pet.energy = int(data[3])
            pet.win_streak = int(data[4]) if len(data) > 4 else 0
            print("\nGame loaded successfully!")
            return pet

    except FileNotFoundError:
        print("\nNo saved game found.")
        return None


def random_event(pet):
    events = [
        ("found a treat", lambda: setattr(pet, "hunger", min(100, pet.hunger + 10))),
        ("discovered a new toy", lambda: setattr(pet, "happiness", min(100, pet.happiness + 10))),
        ("took a quick nap", lambda: setattr(pet, "energy", min(100, pet.energy + 10))),
    ]
    event, effect = random.choice(events)
    effect()
    print(f"\nRandom Event: {pet.pet_name} {event}!")


def decay_attributes(pet):
    pet.hunger = max(0, pet.hunger - 5)
    pet.energy = max(0, pet.energy - 5)


def timed_input(prompt, timeout):
    print(prompt)
    timer = threading.Timer(timeout, print, args=["\nTime's up!"])
    timer.start()
    try:
        user_input = input(f"(You have {timeout} seconds to respond): ")
    except TimeoutError:
        user_input = None
    timer.cancel()
    return user_input


def pet_game(pet):
    while True:
        print("\n== Update the pet ==")
        print("1. Feed the pet")
        print("2. Play with pet")
        print("3. Rest Time")
        print("4. Save and Exit to main menu")

        choice = timed_input("Choose an action (1-4): ", 10)

        if choice == "1":
            pet.feed_pet()
        elif choice == "2":
            pet.play_pet()
        elif choice == "3":
            pet.rest_pet()
        elif choice == "4":
            save_game(pet)
            print(f"\nReturning to the main menu, {pet.pet_name}!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        random_event(pet)
        decay_attributes(pet)
        pet.status_pet()
        if pet.check_win():
            save_game(pet)
            break


def main():
    pet = load_game()
    while True:
        print("\nWhat would you like to do?")
        print("1. Update the pet")
        print("2. View the status")
        print("3. Quit and save progress")

        choice = timed_input("Choose an option (1-3): " , 10)

        if choice == "1":
            if not pet:
                pet_name = input("Enter your pet's name: ").strip()
                pet = MyPet(pet_name)
            pet_game(pet)

        elif choice == "2":
            if pet:
                pet.status_pet()
            else:
                print("\nYou don't have a pet yet. Please create one first.")
        elif choice == "3":
            save_game(pet)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
