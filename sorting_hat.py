import random
import time
import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt

console = Console()

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

if __name__ == "__main__":
    while True:
        sorting_hat()
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