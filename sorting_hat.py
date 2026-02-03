import random
import time
import os
import tkinter as tk
from tkinter import ttk, messagebox
import pygame
import threading
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt

console = Console()

# Initialize pygame mixer for music
pygame.mixer.init()

# Define the four Hogwarts houses
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

# House descriptions and colors
house_info = {
    "Gryffindor": {
        "traits": "Brave, daring, and chivalrous!",
        "color": "red",
        "emoji": "🦁",
        "founder": "Godric Gryffindor"
    },
    "Hufflepuff": {
        "traits": "Loyal, patient, and hardworking!",
        "color": "yellow",
        "emoji": "🦡",
        "founder": "Helga Hufflepuff"
    },
    "Ravenclaw": {
        "traits": "Wise, witty, and clever!",
        "color": "blue",
        "emoji": "🦅",
        "founder": "Rowena Ravenclaw"
    },
    "Slytherin": {
        "traits": "Ambitious, cunning, and resourceful!",
        "color": "green",
        "emoji": "🐍",
        "founder": "Salazar Slytherin"
    }
}

# ASCII Art Characters for each house
house_characters = {
    "Gryffindor": """
    ╔═══════════════════════════════════════╗
    ║                                       ║
    ║           🦁 GRYFFINDOR 🦁           ║
    ║                                       ║
    ║        ⚔️  BRAVE & DARING  ⚔️         ║
    ║                                       ║
    ║            .---.                      ║
    ║           /     \\                     ║
    ║          | () () |                    ║
    ║           \\  ^  /                     ║
    ║            |||||                      ║
    ║           |||||                       ║
    ║                                       ║
    ║    "Their daring, nerve, and          ║
    ║     chivalry set Gryffindors          ║
    ║     apart" - Sorting Hat              ║
    ║                                       ║
    ╚═══════════════════════════════════════╝
    """,
    "Hufflepuff": """
    ╔═══════════════════════════════════════╗
    ║                                       ║
    ║          🦡 HUFFLEPUFF 🦡            ║
    ║                                       ║
    ║       🌻  LOYAL & TRUE  🌻           ║
    ║                                       ║
    ║            .---.                      ║
    ║           /     \\                     ║
    ║          | ^   ^ |                    ║
    ║           \\  w  /                     ║
    ║            |||||                      ║
    ║           |||||                       ║
    ║                                       ║
    ║    "Those patient Hufflepuffs         ║
    ║     are true and unafraid             ║
    ║     of toil" - Sorting Hat            ║
    ║                                       ║
    ╚═══════════════════════════════════════╝
    """,
    "Ravenclaw": """
    ╔═══════════════════════════════════════╗
    ║                                       ║
    ║           🦅 RAVENCLAW 🦅            ║
    ║                                       ║
    ║        📚  WISE & WITTY  📚          ║
    ║                                       ║
    ║            .---.                      ║
    ║           /     \\                     ║
    ║          | *   * |                    ║
    ║           \\  -  /                     ║
    ║            |||||                      ║
    ║           |||||                       ║
    ║                                       ║
    ║    "Where those of wit and            ║
    ║     learning will always find         ║
    ║     their kind" - Sorting Hat         ║
    ║                                       ║
    ╚═══════════════════════════════════════╝
    """,
    "Slytherin": """
    ╔═══════════════════════════════════════╗
    ║                                       ║
    ║           🐍 SLYTHERIN 🐍            ║
    ║                                       ║
    ║      💎  AMBITIOUS & CUNNING  💎     ║
    ║                                       ║
    ║            .---.                      ║
    ║           /     \\                     ║
    ║          | -   - |                    ║
    ║           \\  ~  /                     ║
    ║            |||||                      ║
    ║           |||||                       ║
    ║                                       ║
    ║    "Those cunning folk use            ║
    ║     any means to achieve              ║
    ║     their ends" - Sorting Hat         ║
    ║                                       ║
    ╚═══════════════════════════════════════╝
    """
}

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_title():
    """Display the game title with style"""
    clear_screen()
    
    title_art = """
    ╦ ╦╔═╗╔═╗╦ ╦╔═╗╦═╗╔╦╗╔═╗  ╔═╗╔═╗╦═╗╔╦╗╦╔╗╔╔═╗  ╦ ╦╔═╗╔╦╗
    ╠═╣║ ║║ ╦║║║╠═╣╠╦╝ ║ ╚═╗  ╚═╗║ ║╠╦╝ ║ ║║║║║ ╦  ╠═╣╠═╣ ║ 
    ╩ ╩╚═╝╚═╝╚╩╝╩ ╩╩╚═ ╩ ╚═╝  ╚═╝╚═╝╩╚═ ╩ ╩╝╚╝╚═╝  ╩ ╩╩ ╩ ╩ 
    """
    
    title_text = Text(title_art, style="bold magenta")
    subtitle = Text("✨ The Magical Sorting Ceremony ✨", style="bold yellow")
    
    console.print(Align.center(title_text))
    console.print(Align.center(subtitle))
    console.print("\n")

def animate_thinking():
    """Show thinking animation"""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]The Sorting Hat is thinking...", total=100)
        for i in range(100):
            time.sleep(0.02)
            progress.update(task, advance=1)

def display_house_result(house, name):
    """Display the house result with character art"""
    clear_screen()
    
    # Display character art with house color
    color = house_info[house]["color"]
    character = house_characters[house]
    
    console.print(character, style=f"bold {color}")
    
    # Create result panel
    result_text = Text()
    result_text.append(f"\n🎉 CONGRATULATIONS, {name.upper()}! 🎉\n\n", style="bold white")
    result_text.append(f"You have been sorted into ", style="white")
    result_text.append(f"{house.upper()}", style=f"bold {color}")
    result_text.append(f"!\n\n", style="white")
    result_text.append(f"{house_info[house]['emoji']} ", style=color)
    result_text.append(f"Traits: {house_info[house]['traits']}\n", style=f"{color}")
    result_text.append(f"Founded by: {house_info[house]['founder']}\n", style=f"dim {color}")
    
    panel = Panel(
        Align.center(result_text),
        border_style=color,
        padding=(1, 2)
    )
    
    console.print(panel)
    console.print()

def sorting_hat():
    """Main function to sort a student into a house"""
    show_title()
    
    # Create welcome panel
    welcome_text = Text()
    welcome_text.append("🎩 WELCOME TO HOGWARTS 🎩\n\n", style="bold gold1")
    welcome_text.append("The Sorting Hat will determine\n", style="white")
    welcome_text.append("which house you belong to...\n", style="white")
    
    welcome_panel = Panel(
        Align.center(welcome_text),
        border_style="bright_magenta",
        padding=(1, 4)
    )
    
    console.print(welcome_panel)
    console.print()
    
    # Get user's name
    name = Prompt.ask("[bold cyan]Enter your name[/bold cyan]", default="Student")
    
    console.print(f"\n[italic yellow]Hmm... {name}...[/italic yellow]")
    time.sleep(1)
    console.print("[italic yellow]Difficult. Very difficult...[/italic yellow]")
    time.sleep(1)
    console.print()
    
    # Show thinking animation
    animate_thinking()
    
    # Randomly select a house
    selected_house = random.choice(houses)
    
    time.sleep(0.5)
    
    # Dramatic reveal
    console.print("\n" * 2)
    console.print(Align.center(Text(f"⚡ {selected_house.upper()}! ⚡", style=f"bold {house_info[selected_house]['color']}")))
    time.sleep(1.5)
    
    # Display full result
    display_house_result(selected_house, name)

def play_again():
    """Ask if user wants to sort another student"""
    choice = Prompt.ask(
        "\n[bold cyan]Sort another student?[/bold cyan]",
        choices=["yes", "no"],
        default="yes"
    )
    return choice.lower() == "yes"

def play_background_music():
    """Play Harry Potter theme music in loop"""
    try:
        # Try to load and play the music file
        # You can download Harry Potter theme music and save as 'harry_potter_theme.mp3'
        if os.path.exists('E:\HP Game\Harry_Potter_-_Theme_Song_Hedwig_s_Theme_(mp3.pm).mp3'):
            pygame.mixer.music.load('E:\HP Game\Harry_Potter_-_Theme_Song_Hedwig_s_Theme_(mp3.pm).mp3')
            pygame.mixer.music.set_volume(0.3)  # 30% volume
            pygame.mixer.music.play(-1)  # Loop indefinitely
        elif os.path.exists('harry_potter_theme.wav'):
            pygame.mixer.music.load('harry_potter_theme.wav')
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)
    except Exception as e:
        print(f"Could not load background music: {e}")

def stop_background_music():
    """Stop the background music"""
    pygame.mixer.music.stop()

class SortingHatGUI:
    """GUI Application for the Sorting Hat"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Hogwarts Sorting Hat Ceremony")
        self.root.geometry("700x600")
        self.root.configure(bg="#1a1a2e")
        
        # Music state
        self.music_playing = False
        
        # House colors for GUI
        self.house_colors = {
            "Gryffindor": "#740001",
            "Hufflepuff": "#FFD700",
            "Ravenclaw": "#0E1A40",
            "Slytherin": "#1A472A"
        }
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Title Frame
        title_frame = tk.Frame(self.root, bg="#1a1a2e")
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame,
            text="🎩 HOGWARTS SORTING HAT 🎩",
            font=("Helvetica", 24, "bold"),
            fg="#FFD700",
            bg="#1a1a2e"
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="✨ The Magical Sorting Ceremony ✨",
            font=("Helvetica", 12, "italic"),
            fg="#FFFFFF",
            bg="#1a1a2e"
        )
        subtitle_label.pack()
        
        # Music Control Frame
        music_frame = tk.Frame(self.root, bg="#1a1a2e")
        music_frame.pack(pady=10)
        
        self.music_button = tk.Button(
            music_frame,
            text="🎵 Play Music",
            command=self.toggle_music,
            font=("Helvetica", 10),
            bg="#4a4a6e",
            fg="white",
            relief=tk.RAISED,
            padx=20,
            pady=5
        )
        self.music_button.pack()
        
        # Welcome Message
        welcome_frame = tk.Frame(self.root, bg="#2e2e4e", relief=tk.RIDGE, borderwidth=3)
        welcome_frame.pack(pady=20, padx=40, fill=tk.BOTH)
        
        welcome_text = tk.Label(
            welcome_frame,
            text="Welcome to Hogwarts!\n\nThe Sorting Hat will determine\nwhich house you belong to...\n\n🦁 Gryffindor  🦡 Hufflepuff\n🦅 Ravenclaw  🐍 Slytherin",
            font=("Helvetica", 12),
            fg="white",
            bg="#2e2e4e",
            justify=tk.CENTER,
            pady=15
        )
        welcome_text.pack()
        
        # Name Entry Frame
        entry_frame = tk.Frame(self.root, bg="#1a1a2e")
        entry_frame.pack(pady=20)
        
        name_label = tk.Label(
            entry_frame,
            text="Enter your name:",
            font=("Helvetica", 12),
            fg="white",
            bg="#1a1a2e"
        )
        name_label.pack()
        
        self.name_entry = tk.Entry(
            entry_frame,
            font=("Helvetica", 14),
            width=30,
            justify=tk.CENTER
        )
        self.name_entry.pack(pady=10)
        self.name_entry.insert(0, "Student")
        
        # Sort Button
        self.sort_button = tk.Button(
            self.root,
            text="🎩 BEGIN SORTING 🎩",
            command=self.start_sorting,
            font=("Helvetica", 14, "bold"),
            bg="#8B0000",
            fg="white",
            relief=tk.RAISED,
            padx=30,
            pady=15
        )
        self.sort_button.pack(pady=20)
        
        # Result Frame (initially hidden)
        self.result_frame = tk.Frame(self.root, bg="#1a1a2e")
        
        self.result_label = tk.Label(
            self.result_frame,
            text="",
            font=("Helvetica", 18, "bold"),
            fg="white",
            bg="#1a1a2e",
            pady=20
        )
        self.result_label.pack()
        
        # Restart Button
        restart_button = tk.Button(
            self.root,
            text="🔄 Sort Another Student",
            command=self.restart,
            font=("Helvetica", 11),
            bg="#4a4a6e",
            fg="white",
            relief=tk.RAISED,
            padx=20,
            pady=10
        )
        restart_button.pack(pady=10)
    
    def toggle_music(self):
        """Toggle background music on/off"""
        if self.music_playing:
            stop_background_music()
            self.music_button.config(text="🎵 Play Music")
            self.music_playing = False
        else:
            threading.Thread(target=play_background_music, daemon=True).start()
            self.music_button.config(text="🔇 Stop Music")
            self.music_playing = True
    
    def start_sorting(self):
        """Start the sorting process"""
        name = self.name_entry.get().strip()
        if not name:
            name = "Student"
        
        # Disable button during sorting
        self.sort_button.config(state=tk.DISABLED)
        
        # Show thinking message
        self.result_label.config(text=f"🤔 Hmm... {name}...\nDifficult. Very difficult...")
        self.result_frame.pack(pady=10)
        
        # Perform sorting after delay
        self.root.after(3000, lambda: self.show_result(name))
    
    def show_result(self, name):
        """Show the sorting result"""
        # Randomly select house
        house = random.choice(houses)
        color = self.house_colors[house]
        emoji = house_info[house]["emoji"]
        traits = house_info[house]["traits"]
        founder = house_info[house]["founder"]
        
        # Update result display
        result_text = f"🎉 CONGRATULATIONS, {name.upper()}! 🎉\n\n"
        result_text += f"You have been sorted into\n\n"
        result_text += f"{emoji} {house.upper()} {emoji}\n\n"
        result_text += f"Traits: {traits}\n"
        result_text += f"Founded by: {founder}"
        
        self.result_label.config(text=result_text)
        
        # Change background color based on house
        self.result_frame.config(bg=color)
        self.result_label.config(bg=color)
        
        # Re-enable button
        self.sort_button.config(state=tk.NORMAL)
    
    def restart(self):
        """Restart the sorting process"""
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, "Student")
        self.result_frame.pack_forget()
        self.result_label.config(text="", bg="#1a1a2e")
        self.result_frame.config(bg="#1a1a2e")

def run_gui():
    """Run the GUI version of the game"""
    root = tk.Tk()
    app = SortingHatGUI(root)
    root.mainloop()

def run_terminal():
    """Run the terminal version of the game"""
    try:
        while True:
            sorting_hat()
            if not play_again():
                clear_screen()
                farewell = Text()
                farewell.append("\n🎓 Thank you for visiting Hogwarts! 🎓\n", style="bold yellow")
                farewell.append("May magic be with you always! ✨\n", style="italic cyan")
                
                farewell_panel = Panel(
                    Align.center(farewell),
                    border_style="bright_magenta",
                    padding=(1, 4)
                )
                
                console.print(farewell_panel)
                break
    except KeyboardInterrupt:
        console.print("\n\n[bold red]Sorting ceremony interrupted! Goodbye! 👋[/bold red]")

if __name__ == "__main__":
    # Ask user which version to run
    print("\n" + "="*50)
    print("   HOGWARTS SORTING HAT CEREMONY")
    print("="*50)
    print("\nChoose your experience:")
    print("1. GUI Version (with background music option)")
    print("2. Terminal Version (classic)")
    print("="*50)
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    if choice == "1":
        run_gui()
    else:
        run_terminal()