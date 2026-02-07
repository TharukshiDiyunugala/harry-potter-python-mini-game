import random
import time
import os
import tkinter as tk
from tkinter import ttk, messagebox
import pygame
import threading
import math
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
    """GUI Application for the Sorting Hat with Modern Professional UI"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Hogwarts Sorting Hat Ceremony")
        self.root.geometry("1000x750")
        
        # Configure window
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)
        
        # Music state
        self.music_playing = False
        
        # Animation variables
        self.particles = []
        self.glow_alpha = 0
        self.glow_direction = 1
        self.title_y = -100
        self.content_alpha = 0
        
        # Maze variables
        self.maze_active = False
        self.player_pos = [1, 1]
        self.maze = []
        self.maze_size = 15
        self.cell_size = 40
        
        # Mini character animation variables
        self.character_visible = False
        self.character_y_offset = 0
        self.character_bounce_direction = 1
        self.character_elements = []
        
        # House colors with gradients - Professional palette
        self.house_colors = {
            "Gryffindor": {"primary": "#9C1203", "secondary": "#F4C430", "glow": "#FFD700", "dark": "#6B0504"},
            "Hufflepuff": {"primary": "#F0C75E", "secondary": "#372E29", "glow": "#FFE55C", "dark": "#C19B3B"},
            "Ravenclaw": {"primary": "#0E1A40", "secondary": "#946B2D", "glow": "#5DADE2", "dark": "#0B1229"},
            "Slytherin": {"primary": "#1A472A", "secondary": "#AAAAAA", "glow": "#5DBE71", "dark": "#0F2A19"}
        }
        
        # Create canvas for custom drawing
        self.canvas = tk.Canvas(
            self.root,
            width=1000,
            height=750,
            bg="#1a1a2e",
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.create_widgets()
        self.start_animations()
    
    def create_widgets(self):
        """Create all GUI widgets with professional animation-ready structure"""
        
        # Background gradient effect
        self.create_gradient_background()
        
        # Animated particles
        self.create_particles()
        
        # === PERSISTENT MUSIC SPEAKER BUTTON (Top Right Corner) ===
        self.create_persistent_music_button()
        
        # Title with fade-in animation - Professional styling
        self.title_text = self.canvas.create_text(
            500, self.title_y,
            text="🎩 HOGWARTS SORTING HAT 🎩",
            font=("Copperplate Gothic Bold", 36, "bold"),
            fill="#F4C430",
            tags="title"
        )
        
        self.subtitle_text = self.canvas.create_text(
            500, 120,
            text="✨ The Magical Sorting Ceremony ✨",
            font=("Georgia", 16, "italic"),
            fill="#E8D7C3",
            tags="subtitle",
            state="hidden"
        )
        
        # Welcome frame with professional styling
        self.welcome_frame = tk.Frame(
            self.canvas,
            bg="#2d2d44",
            relief=tk.FLAT,
            borderwidth=0
        )
        self.welcome_window = self.canvas.create_window(
            500, 270,
            window=self.welcome_frame,
            tags="welcome",
            state="hidden"
        )
        
        # Add subtle glow effect to frame
        self.canvas.create_rectangle(
            200, 180, 800, 360,
            outline="#F4C430",
            width=2,
            tags=("welcome", "welcome_glow")
        )
        
        self.welcome_text = tk.Label(
            self.welcome_frame,
            text="Welcome to Hogwarts!\n\nThe Sorting Hat will determine\nwhich house you belong to...\n\n🦁 Gryffindor  🦡 Hufflepuff\n🦅 Ravenclaw  🐍 Slytherin",
            font=("Georgia", 13),
            fg="#E8D7C3",
            bg="#2d2d44",
            justify=tk.CENTER,
            pady=20,
            padx=40
        )
        self.welcome_text.pack()
        
        # Name entry with professional styling
        self.entry_frame = tk.Frame(self.canvas, bg="#1a1a2e")
        self.entry_window = self.canvas.create_window(
            500, 450,
            window=self.entry_frame,
            tags="entry",
            state="hidden"
        )
        
        self.name_label = tk.Label(
            self.entry_frame,
            text="Enter your name:",
            font=("Georgia", 14, "bold"),
            fg="#F4C430",
            bg="#1a1a2e"
        )
        self.name_label.pack(pady=5)
        
        # Custom styled entry with glow effect
        self.name_entry = tk.Entry(
            self.entry_frame,
            font=("Georgia", 18),
            width=22,
            justify=tk.CENTER,
            bg="#2d2d44",
            fg="#E8D7C3",
            insertbackground="#F4C430",
            relief=tk.FLAT,
            borderwidth=2,
            highlightthickness=2,
            highlightbackground="#F4C430",
            highlightcolor="#FFD700"
        )
        self.name_entry.pack(pady=10, ipady=10)
        self.name_entry.insert(0, "Student")
        
        # Bind focus events for character animation
        self.name_entry.bind("<FocusIn>", lambda e: self.show_mini_character())
        self.name_entry.bind("<FocusOut>", lambda e: self.hide_mini_character())
        self.name_entry.bind("<KeyRelease>", lambda e: self.character_react_to_typing())
        
        # Professional animated sort button
        self.sort_button = tk.Button(
            self.canvas,
            text="✨ BEGIN SORTING ✨",
            command=self.start_sorting,
            font=("Georgia", 16, "bold"),
            bg="#9C1203",
            fg="#FFD700",
            activebackground="#C41E0B",
            activeforeground="#FFE55C",
            relief=tk.FLAT,
            borderwidth=0,
            padx=50,
            pady=18,
            cursor="hand2"
        )
        self.sort_button_window = self.canvas.create_window(
            500, 570,
            window=self.sort_button,
            tags="sort_btn",
            state="hidden"
        )
        
        # Result frame with professional styling
        self.result_frame = tk.Frame(self.canvas, bg="#1a1a2e")
        self.result_window = self.canvas.create_window(
            500, 350,
            window=self.result_frame,
            tags="result",
            state="hidden"
        )
        
        self.result_label = tk.Label(
            self.result_frame,
            text="",
            font=("Georgia", 18, "bold"),
            fg="#E8D7C3",
            bg="#1a1a2e",
            justify=tk.CENTER,
            pady=35,
            padx=50
        )
        self.result_label.pack()
        
        # Professional maze button
        self.maze_button = tk.Button(
            self.canvas,
            text="🌟 MAZE CHALLENGE 🌟",
            command=self.start_maze,
            font=("Georgia", 14, "bold"),
            bg="#0E1A40",
            fg="#FFD700",
            activebackground="#1a2d5e",
            activeforeground="#FFE55C",
            relief=tk.FLAT,
            borderwidth=0,
            padx=35,
            pady=14,
            cursor="hand2"
        )
        self.maze_button_window = self.canvas.create_window(
            500, 600,
            window=self.maze_button,
            tags="maze_btn",
            state="hidden"
        )
        
        # Professional restart button
        self.restart_button = tk.Button(
            self.canvas,
            text="🔄 Sort Another Student",
            command=self.restart,
            font=("Georgia", 13, "bold"),
            bg="#2d2d44",
            fg="#F4C430",
            activebackground="#3d3d54",
            activeforeground="#FFE55C",
            relief=tk.FLAT,
            padx=30,
            pady=14,
            cursor="hand2"
        )
        self.restart_button_window = self.canvas.create_window(
            500, 670,
            window=self.restart_button,
            tags="restart_btn",
            state="hidden"
        )
        
        # Bind hover effects
        self.sort_button.bind("<Enter>", lambda e: self.on_button_hover(self.sort_button, "#C41E0B"))
        self.sort_button.bind("<Leave>", lambda e: self.on_button_leave(self.sort_button, "#9C1203"))
        self.restart_button.bind("<Enter>", lambda e: self.on_button_hover(self.restart_button, "#3d3d54"))
        self.restart_button.bind("<Leave>", lambda e: self.on_button_leave(self.restart_button, "#2d2d44"))
        self.maze_button.bind("<Enter>", lambda e: self.on_button_hover(self.maze_button, "#1a2d5e"))
        self.maze_button.bind("<Leave>", lambda e: self.on_button_leave(self.maze_button, "#0E1A40"))
    
    def create_persistent_music_button(self):
        """Create a persistent speaker icon button that shows on every window"""
        # Create a fixed position button frame in top-right corner
        button_frame = tk.Frame(
            self.canvas,
            bg="#2d2d44",
            relief=tk.FLAT,
            borderwidth=0
        )
        
        # Position in top-right corner
        self.persistent_music_window = self.canvas.create_window(
            950, 30,
            window=button_frame,
            tags="persistent_music",
            anchor="e"
        )
        
        # Speaker icon button - Professional styling
        self.persistent_music_button = tk.Button(
            button_frame,
            text="🔊",
            command=self.toggle_music,
            font=("Segoe UI Emoji", 28),
            bg="#2d2d44",
            fg="#F4C430",
            activebackground="#3d3d54",
            activeforeground="#FFE55C",
            relief=tk.FLAT,
            borderwidth=0,
            padx=12,
            pady=8,
            cursor="hand2",
            width=2,
            height=1
        )
        self.persistent_music_button.pack()
        
        # Add hover glow effect
        self.persistent_music_button.bind("<Enter>", lambda e: self.persistent_music_button.config(bg="#3d3d54", fg="#FFD700"))
        self.persistent_music_button.bind("<Leave>", lambda e: self.persistent_music_button.config(bg="#2d2d44", fg="#F4C430"))
        
        # Keep this button always visible
        self.canvas.tag_raise("persistent_music")
    
    def create_gradient_background(self):
        """Create professional animated gradient background"""
        # Create gradient rectangles for dark mystical theme
        for i in range(60):
            y = i * 12.5
            # Calculate color gradient from dark navy to darker purple
            r = 26 + int(i * 0.3)
            g = 26 + int(i * 0.2)
            b = 46 - int(i * 0.3)
            color = f"#{min(r, 45):02x}{min(g, 35):02x}{max(b, 30):02x}"
            self.canvas.create_rectangle(
                0, y, 1000, y + 12.5,
                fill=color,
                outline="",
                tags="gradient"
            )
    
    def create_particles(self):
        """Create floating magical particle effect"""
        for _ in range(40):
            x = random.randint(0, 1000)
            y = random.randint(0, 750)
            size = random.randint(1, 4)
            speed = random.uniform(0.3, 1.5)
            particle = {
                'id': self.canvas.create_oval(
                    x, y, x + size, y + size,
                    fill="#F4C430",
                    outline="",
                    tags="particle"
                ),
                'x': x,
                'y': y,
                'size': size,
                'speed': speed,
                'direction': random.choice([-1, 1])
            }
            self.particles.append(particle)
    
    def animate_particles(self):
        """Animate floating magical particles"""
        for particle in self.particles:
            # Move particle
            particle['y'] -= particle['speed']
            particle['x'] += particle['direction'] * 0.2
            
            # Reset if out of bounds
            if particle['y'] < 0:
                particle['y'] = 750
                particle['x'] = random.randint(0, 1000)
            
            if particle['x'] < 0 or particle['x'] > 1000:
                particle['direction'] *= -1
            
            # Update position
            self.canvas.coords(
                particle['id'],
                particle['x'],
                particle['y'],
                particle['x'] + particle['size'],
                particle['y'] + particle['size']
            )
            
            # Pulse glow effect for magical feel
            alpha_val = int(128 + 127 * math.sin(time.time() * 2 + particle['x']))
            try:
                # Golden magical particles
                r = 244
                g = max(196 - (255 - alpha_val) // 3, 140)
                b = 48
                self.canvas.itemconfig(particle['id'], fill=f"#{r:02x}{g:02x}{b:02x}")
            except:
                pass
        
        self.root.after(50, self.animate_particles)
    
    def start_animations(self):
        """Start all entrance animations"""
        self.animate_particles()
        self.animate_title_entrance()
    
    def animate_title_entrance(self):
        """Animate title sliding down with elegance"""
        if self.title_y < 60:
            self.title_y += 2.5
            self.canvas.coords(self.title_text, 500, self.title_y)
            self.root.after(20, self.animate_title_entrance)
        else:
            # Show subtitle after title
            self.canvas.itemconfig("subtitle", state="normal")
            self.fade_in_content()
    
    def fade_in_content(self):
        """Fade in the main content smoothly"""
        if self.content_alpha < 1:
            self.content_alpha += 0.04
            self.root.after(30, self.fade_in_content)
        else:
            # Show all elements
            self.canvas.itemconfig("welcome", state="normal")
            self.canvas.itemconfig("welcome_glow", state="normal")
            self.canvas.itemconfig("entry", state="normal")
            self.canvas.itemconfig("sort_btn", state="normal")
            self.pulse_glow_effect()
    
    def pulse_glow_effect(self):
        """Create professional pulsing glow effect around buttons"""
        self.glow_alpha += 0.04 * self.glow_direction
        
        if self.glow_alpha >= 1:
            self.glow_direction = -1
        elif self.glow_alpha <= 0:
            self.glow_direction = 1
        
        # Update button glow with smooth transitions
        glow_intensity_r = int(156 + 40 * self.glow_alpha)
        glow_intensity_g = int(18 + 10 * self.glow_alpha)
        try:
            self.sort_button.config(bg=f"#{glow_intensity_r:02x}{glow_intensity_g:02x}03")
        except:
            pass
        
        self.root.after(60, self.pulse_glow_effect)
    
    def show_mini_character(self):
        """Show animated mini character when typing name"""
        if not self.character_visible:
            self.character_visible = True
            
            # Create owl character elements
            # Owl body
            self.character_elements.append(
                self.canvas.create_text(
                    700, 450,
                    text="🦉",
                    font=("Segoe UI Emoji", 52),
                    tags="mini_char"
                )
            )
            
            # Professional speech bubble
            bubble_frame = tk.Frame(self.canvas, bg="#2d2d44", relief=tk.FLAT, borderwidth=0)
            bubble_window = self.canvas.create_window(
                820, 430,
                window=bubble_frame,
                tags="mini_char"
            )
            self.character_elements.append(bubble_window)
            
            bubble_text = tk.Label(
                bubble_frame,
                text="  Nice to\n  meet you!  ",
                font=("Georgia", 11, "italic", "bold"),
                fg="#F4C430",
                bg="#2d2d44",
                justify=tk.LEFT
            )
            bubble_text.pack(padx=8, pady=5)
            
            # Add glow outline to bubble
            self.canvas.create_rectangle(
                770, 410, 870, 450,
                outline="#F4C430",
                width=1,
                tags="mini_char"
            )
            
            # Star particles around character
            for i in range(6):
                angle = (i * 60) * (math.pi / 180)
                x = 700 + 45 * math.cos(angle)
                y = 450 + 45 * math.sin(angle)
                star = self.canvas.create_text(
                    x, y,
                    text="✨",
                    font=("Segoe UI Emoji", 14),
                    tags="mini_char"
                )
                self.character_elements.append(star)
            
            # Start bouncing animation
            self.animate_character_bounce()
    
    def hide_mini_character(self):
        """Hide mini character with fade out effect"""
        if self.character_visible:
            self.character_visible = False
            
            # Slide out animation before removal
            self.slide_out_character()
    
    def slide_out_character(self, offset=0):
        """Slide character out to the right"""
        if offset < 200:
            for element in self.character_elements:
                try:
                    coords = self.canvas.coords(element)
                    if len(coords) >= 2:
                        self.canvas.coords(element, coords[0] + 10, coords[1])
                except:
                    pass
            self.root.after(20, lambda: self.slide_out_character(offset + 10))
        else:
            # Remove all character elements
            self.canvas.delete("mini_char")
            self.character_elements.clear()
            self.character_y_offset = 0
    
    def animate_character_bounce(self):
        """Animate character bouncing up and down"""
        if self.character_visible:
            # Bounce animation
            self.character_y_offset += 0.25 * self.character_bounce_direction
            
            if self.character_y_offset > 8:
                self.character_bounce_direction = -1
            elif self.character_y_offset < -8:
                self.character_bounce_direction = 1
            
            # Move all character elements
            for element in self.character_elements:
                try:
                    coords = self.canvas.coords(element)
                    if len(coords) >= 2:
                        current_y = coords[1]
                        # Only apply vertical movement
                        self.canvas.coords(element, coords[0], 450 + self.character_y_offset if element == self.character_elements[0] else current_y)
                except:
                    pass
            
            self.root.after(30, self.animate_character_bounce)
    
    def character_react_to_typing(self):
        """Character reacts when user types with magical sparkles"""
        if self.character_visible and len(self.character_elements) > 0:
            # Create magical sparkle effect when typing
            x = 700 + random.randint(-35, 35)
            y = 450 + random.randint(-35, 35)
            sparkle = self.canvas.create_text(
                x, y,
                text=random.choice(["✨", "⭐", "💫", "🌟"]),
                font=("Segoe UI Emoji", 16),
                tags="sparkle"
            )
            
            # Fade out and remove sparkle
            self.fade_out_sparkle(sparkle, 0)
    
    def fade_out_sparkle(self, sparkle_id, step):
        """Fade out sparkle effect with smooth animation"""
        if step < 12:
            try:
                coords = self.canvas.coords(sparkle_id)
                if len(coords) >= 2:
                    # Move sparkle up and fade
                    self.canvas.coords(sparkle_id, coords[0], coords[1] - 2.5)
                self.root.after(45, lambda: self.fade_out_sparkle(sparkle_id, step + 1))
            except:
                pass
        else:
            try:
                self.canvas.delete(sparkle_id)
            except:
                pass
    
    def on_button_hover(self, button, color):
        """Button hover effect with professional styling"""
        button.config(bg=color)
    
    def on_button_leave(self, button, color):
        """Button leave effect"""
        button.config(bg=color)
    
    def toggle_music(self):
        """Toggle background music on/off with speaker icon update"""
        if self.music_playing:
            stop_background_music()
            self.persistent_music_button.config(text="🔊")
            self.music_playing = False
        else:
            threading.Thread(target=play_background_music, daemon=True).start()
            self.persistent_music_button.config(text="🔇")
            self.music_playing = True
        
        # Keep button always on top
        self.canvas.tag_raise("persistent_music")
    
    def start_sorting(self):
        """Start the sorting process with professional animations"""
        name = self.name_entry.get().strip()
        if not name:
            name = "Student"
        
        # Disable button during sorting
        self.sort_button.config(state=tk.DISABLED)
        
        # Hide input elements with fade out
        self.canvas.itemconfig("welcome", state="hidden")
        self.canvas.itemconfig("welcome_glow", state="hidden")
        self.canvas.itemconfig("entry", state="hidden")
        self.canvas.itemconfig("sort_btn", state="hidden")
        
        # Ensure music button stays visible
        self.canvas.tag_raise("persistent_music")
        
        # Show thinking animation
        self.show_thinking_animation(name)
    
    def show_thinking_animation(self, name):
        """Display professional animated thinking process"""
        thinking_frame = tk.Frame(self.canvas, bg="#2d2d44", padx=50, pady=35, relief=tk.FLAT, borderwidth=0)
        thinking_window = self.canvas.create_window(500, 380, window=thinking_frame, tags="thinking")
        
        # Add glow outline
        self.canvas.create_rectangle(
            250, 310, 750, 450,
            outline="#F4C430",
            width=2,
            tags="thinking"
        )
        
        thinking_label = tk.Label(
            thinking_frame,
            text=f"🤔 Hmm... {name}...\nDifficult. Very difficult...\n\n✨ Analyzing your traits... ✨",
            font=("Georgia", 17, "bold"),
            fg="#E8D7C3",
            bg="#2d2d44",
            justify=tk.CENTER
        )
        thinking_label.pack()
        
        # Ensure music button stays on top
        self.canvas.tag_raise("persistent_music")
        
        # Animated dots
        self.animate_thinking_dots(thinking_label, 0, name)
    
    def animate_thinking_dots(self, label, count, name):
        """Animate thinking dots with professional timing"""
        if count < 18:
            dots = "." * ((count % 4) + 1)
            label.config(text=f"🤔 Hmm... {name}...\nDifficult. Very difficult{dots}\n\n✨ Analyzing your traits... ✨")
            self.root.after(200, lambda: self.animate_thinking_dots(label, count + 1, name))
        else:
            # Remove thinking animation
            self.canvas.delete("thinking")
            # Show result with explosion animation
            self.show_result_with_animation(name)
    
    def show_result_with_animation(self, name):
        """Show sorting result with professional explosion animation"""
        # Randomly select house
        house = random.choice(houses)
        colors = self.house_colors[house]
        emoji = house_info[house]["emoji"]
        traits = house_info[house]["traits"]
        founder = house_info[house]["founder"]
        
        # Create explosion effect
        self.create_explosion_effect(colors["glow"])
        
        # Ensure music button stays on top during animation
        self.canvas.tag_raise("persistent_music")
        
        # Show result after explosion
        self.root.after(1000, lambda: self.display_final_result(name, house, colors, emoji, traits, founder))
    
    def create_explosion_effect(self, color):
        """Create professional particle explosion effect"""
        center_x, center_y = 500, 380
        explosion_particles = []
        
        for _ in range(60):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(4, 12)
            size = random.randint(4, 12)
            
            particle = self.canvas.create_oval(
                center_x, center_y,
                center_x + size, center_y + size,
                fill=color,
                outline="",
                tags="explosion"
            )
            
            explosion_particles.append({
                'id': particle,
                'x': center_x,
                'y': center_y,
                'vx': speed * math.cos(angle),
                'vy': speed * math.sin(angle),
                'size': size,
                'life': 25
            })
        
        self.animate_explosion(explosion_particles)
    
    def animate_explosion(self, particles):
        """Animate explosion particles"""
        active_particles = []
        
        for p in particles:
            if p['life'] > 0:
                p['x'] += p['vx']
                p['y'] += p['vy']
                p['vy'] += 0.5  # Gravity
                p['life'] -= 1
                
                self.canvas.coords(
                    p['id'],
                    p['x'], p['y'],
                    p['x'] + p['size'], p['y'] + p['size']
                )
                
                active_particles.append(p)
            else:
                self.canvas.delete(p['id'])
        
        if active_particles:
            self.root.after(30, lambda: self.animate_explosion(active_particles))
    
    def display_final_result(self, name, house, colors, emoji, traits, founder):
        """Display final sorting result with professional animation"""
        # Clear any existing result
        self.result_label.config(text="")
        
        # Configure result display with professional styling
        result_text = f"🎉 CONGRATULATIONS, {name.upper()}! 🎉\n\n"
        result_text += f"You have been sorted into\n\n"
        result_text += f"{emoji} {house.upper()} {emoji}\n\n"
        result_text += f"{traits}\n"
        result_text += f"Founded by: {founder}"
        
        self.result_frame.config(bg=colors["primary"], relief=tk.FLAT, borderwidth=0)
        self.result_label.config(
            text=result_text,
            bg=colors["primary"],
            fg="#FFE"  # Off-white for better readability
        )
        
        # Show the four house castles and animate student walking to selected house
        self.show_houses_and_walking_student(house)
        
        # Ensure music button stays visible
        self.canvas.tag_raise("persistent_music")
        
        # Show result with slide-in animation after walking animation
        self.root.after(4000, lambda: self.show_final_result_panel())
        
        # Re-enable button
        self.sort_button.config(state=tk.NORMAL)
    
    def slide_in_result(self, current_y, target_y):
        """Slide in result animation with smooth easing"""
        if current_y < target_y:
            current_y += 8
            self.canvas.coords(self.result_window, 500, current_y)
            self.root.after(20, lambda: self.slide_in_result(current_y, target_y))
        else:
            # Ensure music button stays on top
            self.canvas.tag_raise("persistent_music")
    
    def show_houses_and_walking_student(self, selected_house):
        """Display 4 house castles and animate student walking to selected house"""
        # Castle positions (left to right: Gryffindor, Hufflepuff, Ravenclaw, Slytherin)
        castle_positions = {
            "Gryffindor": 150,
            "Hufflepuff": 350,
            "Ravenclaw": 550,
            "Slytherin": 750
        }
        
        # Draw all 4 castles
        for house_name, x_pos in castle_positions.items():
            self.draw_castle(x_pos, 450, house_name, house_name == selected_house)
        
        # Create and animate student walking to selected house
        target_x = castle_positions[selected_house]
        self.create_walking_student(100, 500, target_x, selected_house)
    
    def draw_castle(self, x, y, house_name, is_selected):
        """Draw a castle representation for a house"""
        colors = self.house_colors[house_name]
        base_color = colors["primary"]
        glow_color = colors["glow"] if is_selected else colors["secondary"]
        emoji = house_info[house_name]["emoji"]
        
        # Castle base (larger rectangle)
        castle_base = self.canvas.create_rectangle(
            x - 40, y + 20, x + 40, y + 80,
            fill=base_color,
            outline=glow_color,
            width=3 if is_selected else 1,
            tags="castle"
        )
        
        # Castle towers (smaller rectangles on sides)
        left_tower = self.canvas.create_rectangle(
            x - 45, y, x - 20, y + 70,
            fill=base_color,
            outline=glow_color,
            width=2 if is_selected else 1,
            tags="castle"
        )
        
        right_tower = self.canvas.create_rectangle(
            x + 20, y, x + 45, y + 70,
            fill=base_color,
            outline=glow_color,
            width=2 if is_selected else 1,
            tags="castle"
        )
        
        # Tower tops (triangles)
        left_top = self.canvas.create_polygon(
            x - 50, y, x - 32.5, y - 20, x - 15, y,
            fill=glow_color,
            outline=glow_color,
            tags="castle"
        )
        
        right_top = self.canvas.create_polygon(
            x + 15, y, x + 32.5, y - 20, x + 50, y,
            fill=glow_color,
            outline=glow_color,
            tags="castle"
        )
        
        # Main tower roof
        main_roof = self.canvas.create_polygon(
            x - 45, y + 20, x, y - 10, x + 45, y + 20,
            fill=glow_color,
            outline=glow_color,
            tags="castle"
        )
        
        # Windows
        for i in range(3):
            window_y = y + 30 + (i * 15)
            self.canvas.create_rectangle(
                x - 10, window_y, x + 10, window_y + 10,
                fill="#FFD700" if is_selected else "#555555",
                outline="",
                tags="castle"
            )
        
        # House emoji/crest at top
        self.canvas.create_text(
            x, y - 25,
            text=emoji,
            font=("Helvetica", 24 if is_selected else 18),
            tags="castle"
        )
        
        # House name label
        self.canvas.create_text(
            x, y + 100,
            text=house_name.upper(),
            font=("Helvetica", 10, "bold"),
            fill=glow_color,
            tags="castle"
        )
        
        # Add glow effect for selected house
        if is_selected:
            # Create glowing aura around selected castle
            for i in range(3):
                self.canvas.create_oval(
                    x - 60 - i*5, y - 40 - i*5,
                    x + 60 + i*5, y + 110 + i*5,
                    outline=glow_color,
                    width=1,
                    tags="castle_glow"
                )
            
            # Animate the glow
            self.animate_castle_glow(0)
    
    def animate_castle_glow(self, step):
        """Animate glowing effect around selected castle"""
        if step < 40:
            # Pulse effect
            alpha = (math.sin(step * 0.3) + 1) / 2
            self.root.after(50, lambda: self.animate_castle_glow(step + 1))
    
    def create_walking_student(self, start_x, start_y, target_x, house):
        """Create and animate a 2D cartoon student walking to their house"""
        colors = self.house_colors[house]
        
        # Student elements (stored with identifiers for animation)
        student_elements = {
            'body': [],
            'legs': [],
            'static': []
        }
        
        # === CLOAK/ROBE (flowing, billowing design) ===
        # Main cloak body - large flowing shape
        cloak_main = self.canvas.create_polygon(
            start_x - 20, start_y + 25,  # bottom left
            start_x - 18, start_y - 5,   # left shoulder
            start_x - 8, start_y - 15,   # left neck
            start_x + 8, start_y - 15,   # right neck
            start_x + 18, start_y - 5,   # right shoulder
            start_x + 20, start_y + 25,  # bottom right
            fill=colors["primary"],
            outline=colors["glow"],
            width=2,
            tags="student"
        )
        student_elements['body'].append(cloak_main)
        
        # Cloak hood/cape flowing behind
        cloak_back = self.canvas.create_polygon(
            start_x - 15, start_y - 10,
            start_x - 20, start_y - 5,
            start_x - 22, start_y + 10,
            start_x - 15, start_y + 5,
            fill=colors["secondary"],
            outline="",
            tags="student"
        )
        student_elements['body'].append(cloak_back)
        
        # Cloak inner lining (lighter shade)
        cloak_inner = self.canvas.create_polygon(
            start_x - 15, start_y + 25,
            start_x - 10, start_y - 5,
            start_x + 10, start_y - 5,
            start_x + 15, start_y + 25,
            fill=colors["secondary"],
            outline="",
            tags="student"
        )
        student_elements['body'].append(cloak_inner)
        
        # === HEAD ===
        # Head (larger, more cartoon-like)
        head = self.canvas.create_oval(
            start_x - 10, start_y - 35,
            start_x + 10, start_y - 15,
            fill="#FFE4C4",
            outline="#D2B48C",
            width=1,
            tags="student"
        )
        student_elements['static'].append(head)
        
        # Eyes
        left_eye = self.canvas.create_oval(
            start_x - 6, start_y - 28,
            start_x - 3, start_y - 25,
            fill="#2C2C2C",
            outline="",
            tags="student"
        )
        student_elements['static'].append(left_eye)
        
        right_eye = self.canvas.create_oval(
            start_x + 3, start_y - 28,
            start_x + 6, start_y - 25,
            fill="#2C2C2C",
            outline="",
            tags="student"
        )
        student_elements['static'].append(right_eye)
        
        # Smile
        smile = self.canvas.create_arc(
            start_x - 5, start_y - 24,
            start_x + 5, start_y - 18,
            start=200, extent=140,
            style=tk.ARC,
            outline="#8B4513",
            width=2,
            tags="student"
        )
        student_elements['static'].append(smile)
        
        # === WIZARD HAT ===
        # Hat cone
        hat = self.canvas.create_polygon(
            start_x - 14, start_y - 35,
            start_x - 5, start_y - 50,
            start_x + 4, start_y - 35,
            fill="#2C2C2C",
            outline="#FFD700",
            width=1,
            tags="student"
        )
        student_elements['static'].append(hat)
        
        # Hat brim (wider, more visible)
        hat_brim = self.canvas.create_oval(
            start_x - 14, start_y - 37,
            start_x + 14, start_y - 31,
            fill="#2C2C2C",
            outline="#FFD700",
            width=1,
            tags="student"
        )
        student_elements['static'].append(hat_brim)
        
        # Star on hat
        hat_star = self.canvas.create_text(
            start_x - 3, start_y - 48,
            text="⭐",
            font=("Helvetica", 10),
            tags="student"
        )
        student_elements['static'].append(hat_star)
        
        # === LEGS (for walking animation) ===
        # Left leg
        left_leg = self.canvas.create_rectangle(
            start_x - 8, start_y + 20,
            start_x - 3, start_y + 35,
            fill="#4A4A4A",
            outline="",
            tags="student"
        )
        student_elements['legs'].append(left_leg)
        
        # Left foot
        left_foot = self.canvas.create_oval(
            start_x - 10, start_y + 33,
            start_x - 1, start_y + 38,
            fill="#1C1C1C",
            outline="",
            tags="student"
        )
        student_elements['legs'].append(left_foot)
        
        # Right leg
        right_leg = self.canvas.create_rectangle(
            start_x + 3, start_y + 20,
            start_x + 8, start_y + 35,
            fill="#4A4A4A",
            outline="",
            tags="student"
        )
        student_elements['legs'].append(right_leg)
        
        # Right foot
        right_foot = self.canvas.create_oval(
            start_x + 1, start_y + 33,
            start_x + 10, start_y + 38,
            fill="#1C1C1C",
            outline="",
            tags="student"
        )
        student_elements['legs'].append(right_foot)
        
        # === WAND ===
        wand = self.canvas.create_line(
            start_x + 12, start_y,
            start_x + 25, start_y - 10,
            fill="#8B4513",
            width=3,
            tags="student"
        )
        student_elements['static'].append(wand)
        
        # Wand tip glow
        wand_glow = self.canvas.create_oval(
            start_x + 23, start_y - 12,
            start_x + 27, start_y - 8,
            fill="#FFD700",
            outline="#FFA500",
            width=1,
            tags="student"
        )
        student_elements['static'].append(wand_glow)
        
        # Sparkles around wand (more magical)
        sparkle_positions = [
            (start_x + 28, start_y - 12),
            (start_x + 26, start_y - 15),
            (start_x + 30, start_y - 8),
            (start_x + 32, start_y - 11)
        ]
        for sx, sy in sparkle_positions:
            sparkle = self.canvas.create_text(
                sx, sy,
                text=random.choice(["✨", "⭐", "💫"]),
                font=("Helvetica", 10),
                tags="student"
            )
            student_elements['static'].append(sparkle)
        
        # === HOUSE SCARF (optional detail) ===
        scarf = self.canvas.create_rectangle(
            start_x - 8, start_y - 14,
            start_x + 8, start_y - 8,
            fill=colors["glow"],
            outline="",
            tags="student"
        )
        student_elements['body'].append(scarf)
        
        # Flatten all elements into a single list for animation
        all_elements = (student_elements['body'] + 
                       student_elements['legs'] + 
                       student_elements['static'])
        
        # Store leg elements separately for walking animation
        self.student_leg_elements = student_elements['legs']
        
        # Start walking animation
        self.animate_walking_student(all_elements, start_x, start_y, target_x, 0)
    
    def animate_walking_student(self, elements, current_x, y, target_x, step):
        """Animate 2D cartoon student walking to their house with leg movement"""
        if current_x < target_x - 50:
            # Move student to the right
            speed = 4
            current_x += speed
            
            # Bobbing effect while walking (more pronounced for cartoon style)
            bob_offset = math.sin(step * 0.4) * 4
            
            # Leg walking animation (alternating leg positions)
            if hasattr(self, 'student_leg_elements') and len(self.student_leg_elements) == 4:
                leg_swing = math.sin(step * 0.5) * 3
                
                # Animate left leg (elements 0 and 1)
                try:
                    # Left leg
                    left_leg_coords = self.canvas.coords(self.student_leg_elements[0])
                    if len(left_leg_coords) == 4:
                        # Swing forward/back
                        self.canvas.coords(self.student_leg_elements[0],
                            left_leg_coords[0] + speed,
                            left_leg_coords[1] + leg_swing,
                            left_leg_coords[2] + speed,
                            left_leg_coords[3])
                    
                    # Left foot
                    left_foot_coords = self.canvas.coords(self.student_leg_elements[1])
                    if len(left_foot_coords) == 4:
                        self.canvas.coords(self.student_leg_elements[1],
                            left_foot_coords[0] + speed,
                            left_foot_coords[1] + leg_swing,
                            left_foot_coords[2] + speed,
                            left_foot_coords[3] + leg_swing)
                    
                    # Right leg (opposite movement)
                    right_leg_coords = self.canvas.coords(self.student_leg_elements[2])
                    if len(right_leg_coords) == 4:
                        self.canvas.coords(self.student_leg_elements[2],
                            right_leg_coords[0] + speed,
                            right_leg_coords[1] - leg_swing,
                            right_leg_coords[2] + speed,
                            right_leg_coords[3])
                    
                    # Right foot
                    right_foot_coords = self.canvas.coords(self.student_leg_elements[3])
                    if len(right_foot_coords) == 4:
                        self.canvas.coords(self.student_leg_elements[3],
                            right_foot_coords[0] + speed,
                            right_foot_coords[1] - leg_swing,
                            right_foot_coords[2] + speed,
                            right_foot_coords[3] - leg_swing)
                except:
                    pass
            
            # Update all other student element positions (body, head, cloak, etc.)
            for element in elements:
                if element not in getattr(self, 'student_leg_elements', []):
                    try:
                        elem_type = self.canvas.type(element)
                        
                        if elem_type == "polygon":
                            coords = self.canvas.coords(element)
                            new_coords = []
                            for i in range(0, len(coords), 2):
                                new_coords.append(coords[i] + speed)
                                new_coords.append(coords[i + 1] + bob_offset * 0.3)
                            self.canvas.coords(element, *new_coords)
                            
                        elif elem_type in ["oval", "rectangle"]:
                            coords = self.canvas.coords(element)
                            if len(coords) == 4:
                                self.canvas.coords(element, 
                                    coords[0] + speed, coords[1] + bob_offset * 0.3,
                                    coords[2] + speed, coords[3] + bob_offset * 0.3)
                                    
                        elif elem_type == "line":
                            coords = self.canvas.coords(element)
                            if len(coords) == 4:
                                self.canvas.coords(element,
                                    coords[0] + speed, coords[1] + bob_offset * 0.3,
                                    coords[2] + speed, coords[3] + bob_offset * 0.3)
                                    
                        elif elem_type in ["text", "arc"]:
                            coords = self.canvas.coords(element)
                            if len(coords) >= 2:
                                self.canvas.coords(element, 
                                    coords[0] + speed, coords[1] + bob_offset * 0.3)
                    except:
                        pass
            
            # Animate cloak flowing effect (add slight wave to cloak polygons)
            cloak_wave = math.sin(step * 0.6) * 2
            
            # Continue animation
            self.root.after(40, lambda: self.animate_walking_student(
                elements, current_x, y, target_x, step + 1))
        else:
            # Student reached the castle - make them disappear into it
            self.student_enter_castle(elements)
    
    def student_enter_castle(self, elements):
        """Animate student entering the castle"""
        # Fade out and shrink effect
        self.fade_out_student(elements, 0)
    
    def fade_out_student(self, elements, step):
        """Fade out student as they enter the castle"""
        if step < 10:
            # Scale down elements
            for element in elements:
                try:
                    if self.canvas.type(element) == "polygon" or self.canvas.type(element) == "oval":
                        coords = self.canvas.coords(element)
                        if len(coords) >= 4:
                            # Calculate center
                            if self.canvas.type(element) == "polygon":
                                center_x = sum(coords[i] for i in range(0, len(coords), 2)) / (len(coords) / 2)
                                center_y = sum(coords[i] for i in range(1, len(coords), 2)) / (len(coords) / 2)
                                # Shrink toward center
                                new_coords = []
                                for i in range(0, len(coords), 2):
                                    new_coords.append(center_x + (coords[i] - center_x) * 0.9)
                                    new_coords.append(center_y + (coords[i + 1] - center_y) * 0.9)
                                self.canvas.coords(element, *new_coords)
                            else:
                                center_x = (coords[0] + coords[2]) / 2
                                center_y = (coords[1] + coords[3]) / 2
                                width = (coords[2] - coords[0]) * 0.9
                                height = (coords[3] - coords[1]) * 0.9
                                self.canvas.coords(element,
                                    center_x - width/2, center_y - height/2,
                                    center_x + width/2, center_y + height/2)
                except:
                    pass
            
            self.root.after(50, lambda: self.fade_out_student(elements, step + 1))
        else:
            # Remove student elements
            self.canvas.delete("student")
    
    def show_final_result_panel(self):
        """Show the final result panel after walking animation"""
        # Show result with slide-in animation
        self.canvas.itemconfig("result", state="normal")
        self.canvas.itemconfig("restart_btn", state="normal")
        self.canvas.itemconfig("maze_btn", state="normal")
        
        # Ensure music button stays on top
        self.canvas.tag_raise("persistent_music")
        
        # Animate result sliding in
        self.slide_in_result(100, 200)
    
    def restart(self):
        """Restart the sorting process with professional fade out animation"""
        # Hide result elements
        self.canvas.itemconfig("result", state="hidden")
        self.canvas.itemconfig("restart_btn", state="hidden")
        
        # Clear castle and student animations
        self.canvas.delete("castle")
        self.canvas.delete("castle_glow")
        self.canvas.delete("student")
        
        # Reset and show input elements
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, "Student")
        
        self.result_frame.config(bg="#1a1a2e", relief=tk.FLAT, borderwidth=0)
        self.result_label.config(text="", bg="#1a1a2e")
        
        # Hide maze button
        self.canvas.itemconfig("maze_btn", state="hidden")
        
        # Fade in input elements
        self.canvas.itemconfig("welcome", state="normal")
        self.canvas.itemconfig("welcome_glow", state="normal")
        self.canvas.itemconfig("entry", state="normal")
        self.canvas.itemconfig("sort_btn", state="normal")
        
        # Ensure music button stays on top
        self.canvas.tag_raise("persistent_music")
    
    def start_maze(self):
        """Start the maze challenge"""
        # Hide all previous elements
        self.canvas.itemconfig("result", state="hidden")
        self.canvas.itemconfig("restart_btn", state="hidden")
        self.canvas.itemconfig("maze_btn", state="hidden")
        self.canvas.delete("castle")
        self.canvas.delete("castle_glow")
        
        # Ensure music button stays visible
        self.canvas.tag_raise("persistent_music")
        
        # Initialize maze
        self.maze_active = True
        self.generate_maze()
        self.draw_maze()
        
        # Bind arrow keys
        self.root.bind("<Up>", lambda e: self.move_player(0, -1))
        self.root.bind("<Down>", lambda e: self.move_player(0, 1))
        self.root.bind("<Left>", lambda e: self.move_player(-1, 0))
        self.root.bind("<Right>", lambda e: self.move_player(1, 0))
        
        # Show instructions
        self.show_maze_instructions()
    
    def generate_maze(self):
        """Generate a random maze using recursive backtracking"""
        # Initialize maze with walls
        size = self.maze_size
        self.maze = [[1 for _ in range(size)] for _ in range(size)]
        
        # Start from position (1, 1)
        start_x, start_y = 1, 1
        self.maze[start_y][start_x] = 0
        
        # Recursive backtracking
        stack = [(start_x, start_y)]
        
        while stack:
            x, y = stack[-1]
            neighbors = []
            
            # Check all 4 directions (2 cells away)
            for dx, dy in [(0, -2), (0, 2), (-2, 0), (2, 0)]:
                nx, ny = x + dx, y + dy
                if 1 <= nx < size - 1 and 1 <= ny < size - 1 and self.maze[ny][nx] == 1:
                    neighbors.append((nx, ny, dx, dy))
            
            if neighbors:
                nx, ny, dx, dy = random.choice(neighbors)
                # Remove wall between current cell and chosen neighbor
                self.maze[y + dy // 2][x + dx // 2] = 0
                self.maze[ny][nx] = 0
                stack.append((nx, ny))
            else:
                stack.pop()
        
        # Set start and end positions
        self.player_pos = [1, 1]
        self.maze[1][1] = 0
        self.maze[size - 2][size - 2] = 0  # Exit
        self.exit_pos = [size - 2, size - 2]
    
    def draw_maze(self):
        """Draw the maze on canvas with professional styling"""
        self.canvas.delete("maze")
        
        # Calculate offset to center maze
        maze_width = self.maze_size * self.cell_size
        offset_x = (1000 - maze_width) // 2
        offset_y = 100
        
        # Draw professional title
        self.canvas.create_text(
            500, 50,
            text="🌟 MAGICAL MAZE CHALLENGE 🌟",
            font=("Georgia", 22, "bold"),
            fill="#F4C430",
            tags="maze"
        )
        
        # Draw maze cells with professional colors
        for y in range(self.maze_size):
            for x in range(self.maze_size):
                x1 = offset_x + x * self.cell_size
                y1 = offset_y + y * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                if self.maze[y][x] == 1:
                    # Wall - dark brown
                    self.canvas.create_rectangle(
                        x1, y1, x2, y2,
                        fill="#3d2817",
                        outline="#2a1b0f",
                        tags="maze"
                    )
                else:
                    # Path - lighter tone
                    self.canvas.create_rectangle(
                        x1, y1, x2, y2,
                        fill="#4a4458",
                        outline="#3a3448",
                        tags="maze"
                    )
        
        # Draw exit with glow effect
        exit_x1 = offset_x + self.exit_pos[0] * self.cell_size
        exit_y1 = offset_y + self.exit_pos[1] * self.cell_size
        exit_x2 = exit_x1 + self.cell_size
        exit_y2 = exit_y1 + self.cell_size
        self.canvas.create_rectangle(
            exit_x1, exit_y1, exit_x2, exit_y2,
            fill="#5DBE71",
            outline="#F4C430",
            width=3,
            tags="maze"
        )
        self.canvas.create_text(
            exit_x1 + self.cell_size // 2,
            exit_y1 + self.cell_size // 2,
            text="🏆",
            font=("Segoe UI Emoji", 28),
            tags="maze"
        )
        
        # Ensure music button stays on top
        self.canvas.tag_raise("persistent_music")
        
        # Draw player
        self.draw_player()
    
    def draw_player(self):
        """Draw the player on the maze"""
        self.canvas.delete("player")
        
        maze_width = self.maze_size * self.cell_size
        offset_x = (1000 - maze_width) // 2
        offset_y = 100
        
        x = offset_x + self.player_pos[0] * self.cell_size + self.cell_size // 2
        y = offset_y + self.player_pos[1] * self.cell_size + self.cell_size // 2
        
        # Draw player as a wizard
        self.canvas.create_text(
            x, y,
            text="🧙",
            font=("Segoe UI Emoji", 32),
            tags="player"
        )
        
        # Ensure music button stays on top
        self.canvas.tag_raise("persistent_music")
    
    def move_player(self, dx, dy):
        """Move the player in the maze"""
        if not self.maze_active:
            return
        
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy
        
        # Check bounds and walls
        if (0 <= new_x < self.maze_size and 
            0 <= new_y < self.maze_size and 
            self.maze[new_y][new_x] == 0):
            
            self.player_pos[0] = new_x
            self.player_pos[1] = new_y
            self.draw_player()
            
            # Check if reached exit
            if self.player_pos == self.exit_pos:
                self.maze_completed()
    
    def show_maze_instructions(self):
        """Show professional maze instructions"""
        instructions = tk.Frame(self.canvas, bg="#2d2d44", relief=tk.FLAT, borderwidth=0)
        instructions_window = self.canvas.create_window(
            500, 720,
            window=instructions,
            tags="maze"
        )
        
        instructions_label = tk.Label(
            instructions,
            text="Use Arrow Keys ⬆️⬇️⬅️➡️ to navigate | Find the Trophy 🏆",
            font=("Georgia", 12, "bold"),
            fg="#F4C430",
            bg="#2d2d44",
            padx=25,
            pady=10
        )
        instructions_label.pack()
        
        # Add back button to return from maze
        back_button = tk.Button(
            self.canvas,
            text="⬅️ Back",
            command=self.return_from_maze,
            font=("Georgia", 11, "bold"),
            bg="#4a4458",
            fg="#FFD700",
            activebackground="#5a5468",
            activeforeground="#FFE55C",
            relief=tk.FLAT,
            padx=20,
            pady=10,
            cursor="hand2"
        )
        back_window = self.canvas.create_window(100, 720, window=back_button, tags="maze")
        
        # Ensure music button stays on top
        self.canvas.tag_raise("persistent_music")
    
    def maze_completed(self):
        """Handle maze completion with professional UI"""
        self.maze_active = False
        
        # Show congratulations with professional styling
        congrats_frame = tk.Frame(self.canvas, bg="#2d2d44", relief=tk.FLAT, borderwidth=0)
        congrats_window = self.canvas.create_window(500, 380, window=congrats_frame, tags="maze")
        
        # Add glow outline
        self.canvas.create_rectangle(
            200, 280, 800, 480,
            outline="#FFD700",
            width=3,
            tags="maze"
        )
        
        congrats_label = tk.Label(
            congrats_frame,
            text="🎉 CONGRATULATIONS! 🎉\n\nYou've successfully completed\nthe Magical Maze Challenge!\n\n⭐ Well Done, Young Wizard! ⭐",
            font=("Georgia", 18, "bold"),
            fg="#F4C430",
            bg="#2d2d44",
            justify=tk.CENTER,
            padx=50,
            pady=35
        )
        congrats_label.pack()
        
        # Add professional return button
        return_button = tk.Button(
            self.canvas,
            text="🔄 Return to Sorting Hat",
            command=self.return_from_maze,
            font=("Georgia", 13, "bold"),
            bg="#9C1203",
            fg="#FFD700",
            activebackground="#C41E0B",
            activeforeground="#FFE55C",
            relief=tk.FLAT,
            padx=30,
            pady=14,
            cursor="hand2"
        )
        return_window = self.canvas.create_window(500, 540, window=return_button, tags="maze")
        
        # Ensure music button stays on top
        self.canvas.tag_raise("persistent_music")
    
    def return_from_maze(self):
        """Return to the main screen"""
        self.canvas.delete("maze")
        self.canvas.delete("player")
        self.maze_active = False
        
        # Unbind arrow keys
        self.root.unbind("<Up>")
        self.root.unbind("<Down>")
        self.root.unbind("<Left>")
        self.root.unbind("<Right>")
        
        # Restart the sorting
        self.restart()

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