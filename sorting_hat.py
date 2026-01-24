import random

# Define the four Hogwarts houses
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

# House descriptions
house_info = {
    "Gryffindor": "Brave, daring, and chivalrous!",
    "Hufflepuff": "Loyal, patient, and hardworking!",
    "Ravenclaw": "Wise, witty, and clever!",
    "Slytherin": "Ambitious, cunning, and resourceful!"
}

def sorting_hat():
    """Main function to sort a student into a house"""
    print("=" * 50)
    print("🎩 WELCOME TO HOGWARTS SORTING CEREMONY 🎩")
    print("=" * 50)
    print()
    
    # Get user's name
    name = input("Enter your name: ").strip()
    
    if not name:
        name = "Student"
    
    print(f"\nHmm... {name}...")
    print("Let me see...")
    print("Thinking...")
    
    # Randomly select a house
    selected_house = random.choice(houses)
    
    print("\n" + "=" * 50)
    print(f"⚡ {selected_house.upper()}! ⚡")
    print("=" * 50)
    print(f"\nCongratulations, {name}!")
    print(f"You have been sorted into {selected_house}!")
    print(f"Traits: {house_info[selected_house]}")
    print()

def play_again():
    """Ask if user wants to sort another student"""
    while True:
        choice = input("Sort another student? (yes/no): ").lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'")

if __name__ == "__main__":
    while True:
        sorting_hat()
        if not play_again():
            print("\n🎓 Thank you for visiting Hogwarts! Goodbye! 🎓")
            break
