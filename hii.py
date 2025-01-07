from collections import Counter

#Sample text
text="""
Python is an amazing programming language."""

#Split text into words and count frequency

words = text.lower().split()
word_count = Counter(words)

#Display word Frequency

print("Word frequencies: ")
for word, count in word_count.items():
    print(f"{word}: {count}")



from queue import Queue

#Create a task queue
task_queue = Queue()

#Add tasks to the queue

tasks = ["Task 1: Clean the room", "Task 2: Write Python code", "Task 3: Read a book"]
for task in tasks:
    task_queue.put(task)

#Process tasks

print("Processing Tasks: ")
while not task_queue.empty():
    print(task_queue.get())




from collections import deque
import random

#Initialize deck of cards

deck = deque([f"{value} of {suit}" for value in
              ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"] 
              for suit in ["Hearts","Diamonds", "Clubs", "Spades"]])

#Shuffle the deck

random.shuffle(deck)

#players and their hands

player1 = []
player2 = []

#Draw 3 cards for each player

for _ in range(3):
    player1.append(deck.popleft())
    player2.append(deck.popleft())

#Display player's hands

print("Player 1's Hand: ")
print(player1)
print("\nPlayer 2's Hand: ")
print(player2)


