import random

# ASCII art
rock = '''
    _______
---'   ____ )
      (_____ )
      (_____ )
      (____ )
---.__(___ )
'''

paper = '''
    _______
---'   ____ )____
          ______ )
          _______ )
         _______ )
---.__________ )
'''

scissors = '''
    _______
---'   ____ )____
          ______ )
       __________ )
      (____ )
---.__(___ )
'''

choices = [rock, paper, scissors]
emoji_choices = ['🪨 Rock', '📄 Paper', '✂️ Scissors']

# Score counters
player_score = 0
computer_score = 0
draws = 0

print("🎮 Welcome to Rock Paper Scissors with Emojis!")

while True:
    # Get user input
    try:
        x = int(input("\nWhat do you choose? Type 0 for Rock 🪨, 1 for Paper 📄, or 2 for Scissors ✂️: "))
    except ValueError:
        print("❌ Invalid input. Please enter a number (0, 1, or 2).")
        continue

    if x < 0 or x > 2:
        print("❌ Invalid choice. Please enter 0, 1, or 2.")
        continue

    print(f"\n🧍 You chose: {emoji_choices[x]}")
    print(choices[x])

    # Computer choice
    computer_choice = random.randint(0, 2)
    print(f"💻 Computer chose: {emoji_choices[computer_choice]}")
    print(choices[computer_choice])

    # Result logic
    if x == computer_choice:
        print("🤝 It's a draw!")
        draws += 1
    elif (x == 0 and computer_choice == 2) or (x == 1 and computer_choice == 0) or (x == 2 and computer_choice == 1):
        print("✅ You win!")
        player_score += 1
    else:
        print("❌ You lose!")
        computer_score += 1

    # Show current score
    print(f"\n📊 Score:\n🧍 You: {player_score} | 💻 Computer: {computer_score} | 🤝 Draws: {draws}")

    # Ask to play again
    play_again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\n🏁 Thanks for playing! Final Score:")
        print(f"🧍 You: {player_score} | 💻 Computer: {computer_score} | 🤝 Draws: {draws}")
        break
