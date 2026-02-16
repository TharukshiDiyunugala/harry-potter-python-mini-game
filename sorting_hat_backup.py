import random
import time
import os
import tkinter as tk
from tkinter import ttk, messagebox
import pygame
import threading
import math
from PIL import Image, ImageTk, ImageEnhance, ImageFilter
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
    
    
    
    title_text = Text(style="bold magenta")
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
        self.root.title("⚡ Hogwarts Sorting Hat Ceremony ⚡")
        self.root.geometry("1200x800")
        
        # Configure window
        self.root.configure(bg="#0a0a0f")
        self.root.resizable(False, False)
        
        # Music state
        self.music_playing = False
        
        # Animation variables
        self.particles = []
        self.glow_alpha = 0
        self.glow_direction = 1
        self.title_y = -100
        self.content_alpha = 0
        self.background_animation_step = 0
        
        # Hat spinning animation variables
        self.hat_angle = 0
        self.hat_image = None
        self.hat_photo = None
        self.hat_spinning = True
        self.hat_id = None
        
        # Hat floating animation variables (up-down motion)
        self.hat_y_offset = 0
        self.hat_y_direction = 1  # 1 for down, -1 for up
        self.hat_y_speed = 2  # pixels per frame
        self.hat_y_range = 40  # total vertical range in pixels
        
        # Current screen theme
        self.current_theme = "welcome"  # welcome, sorting, result, maze
        self.current_house = None
        
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
        
        # Animated background assets
        self.bg_photo = None
        self.witch_images = []
        self.witches = []
        
        # Begin button image
        self.begin_button_image = None
        self.begin_button_photo = None
        
        # Load spinning hat image
        self.load_hat_image()
        self.load_begin_button_image()
        
        # House colors with gradients - Professional palette with richer tones
        self.house_colors = {
            "Gryffindor": {
                "primary": "#740001", "secondary": "#D3A625", "glow": "#FFCC00", 
                "dark": "#460000", "accent": "#AE0001", "light": "#FFC500",
                "bg_start": "#1a0505", "bg_end": "#4a0808"
            },
            "Hufflepuff": {
                "primary": "#FFDB00", "secondary": "#000000", "glow": "#FFE55C", 
                "dark": "#C19B3B", "accent": "#60605C", "light": "#FFF4A3",
                "bg_start": "#1a1508", "bg_end": "#4a3820"
            },
            "Ravenclaw": {
                "primary": "#0E1A40", "secondary": "#946B2D", "glow": "#5DADE2", 
                "dark": "#0B1229", "accent": "#222F5B", "light": "#87CEEB",
                "bg_start": "#050a1a", "bg_end": "#0f1f3a"
            },
            "Slytherin": {
                "primary": "#1A472A", "secondary": "#5D5D5D", "glow": "#5DBE71", 
                "dark": "#0F2A19", "accent": "#2A623D", "light": "#A8E6A3",
                "bg_start": "#0a150f", "bg_end": "#1a3025"
            }
        }
        
        # Create canvas for custom drawing with larger size
        self.canvas = tk.Canvas(
            self.root,
            width=1200,
            height=800,
            bg="#0a0a0f",
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Load animated background assets
        self.load_background_assets()
        
        # Create animated background FIRST (so it's behind everything)
        self.create_animated_background()
        self.create_witches()
        
        self.create_widgets()
        
        # Fix layering to ensure background is behind and witches float naturally
        self.fix_layering()
        
        self.start_animations()
        self.animate_background_pattern()
        
        # Start witch animation
        self.animate_witches()
    
    def create_widgets(self):
        """Create all GUI widgets with professional animation-ready structure"""
        
        # Only create gradient if no background image loaded
        if not self.bg_photo:
            self.create_gradient_background()
        
        # Animated particles
        self.create_particles()
        
        # === PERSISTENT MUSIC SPEAKER BUTTON (Top Right Corner) ===
        self.create_persistent_music_button()
        
        # Title with fade-in animation - Professional styling with shadow
        # Title shadow for depth (visible from start)
        self.title_shadow = self.canvas.create_text(
            603, 73,
            text="The Official Sorting Ceremony",
            font=("Harrington", 48, "bold"),
            fill="#000000",
            tags="title"
        )
        
        self.title_text = self.canvas.create_text(
            600, 70,
            text="The Official Sorting Ceremony",
            font=("Harrington", 48, "bold"),
            fill="#FFD700",
            tags="title"
        )
        
        # Subtitle shadow (visible from start)
        self.subtitle_shadow = self.canvas.create_text(
            602, 132,
            text="✨ The Magical Sorting Ceremony ✨",
            font=("Lucida Handwriting", 18, "italic"),
            fill="#000000",
            tags="subtitle"
        )
        
        self.subtitle_text = self.canvas.create_text(
            600, 130,
            text="✨ The Magical Sorting Ceremony ✨",
            font=("Lucida Handwriting", 18, "italic"),
            fill="#E8D7C3",
            tags="subtitle"
        )
        
        # Welcome frame with professional styling
        self.welcome_frame = tk.Frame(
            self.canvas,
            bg="#1a1a2e",
            relief=tk.FLAT,
            borderwidth=0
        )
        self.welcome_window = self.canvas.create_window(
            600, 320,
            window=self.welcome_frame,
            tags="welcome",
            state="hidden"
        )
        
        self.welcome_text = tk.Label(
            self.welcome_frame,
            text="⚡ ENTER THE MAGICAL REALM OF HOGWARTS ⚡\n\nPrepare to embark on an immersive journey through the ancient halls of wizardry.\nThe legendary Sorting Hat, imbued with the wisdom of the Four Founders,\nwill analyze your unique qualities and place you among your destined peers.\nYour magical legacy awaits...\n\n🦁 GRYFFINDOR  🦡 HUFFLEPUFF\n🦅 RAVENCLAW  🐍 SLYTHERIN",
            font=("Georgia", 14),
            fg="#E8D7C3",
            bg="#1a1a2e",
            justify=tk.CENTER,
            pady=25,
            padx=50
        )
        self.welcome_text.pack()
        
        # Name entry with professional styling
        self.entry_frame = tk.Frame(self.canvas, bg="#0a0a0f")
        self.entry_window = self.canvas.create_window(
            600, 520,
            window=self.entry_frame,
            tags="entry",
            state="hidden"
        )
        
        self.name_label = tk.Label(
            self.entry_frame,
            text="✨ Enter Your Name ✨",
            font=("Palatino Linotype", 16, "bold"),
            fg="#FFD700",
            bg="#0a0a0f"
        )
        self.name_label.pack(pady=8)
        
        # Custom styled entry with enhanced glow effect
        entry_container = tk.Frame(self.entry_frame, bg="#1a1a2e", relief=tk.FLAT, borderwidth=3)
        entry_container.pack(pady=10)
        
        self.name_entry = tk.Entry(
            entry_container,
            font=("Georgia", 20),
            width=24,
            justify=tk.CENTER,
            bg="#1a1a2e",
            fg="#FFD700",
            insertbackground="#FFD700",
            relief=tk.FLAT,
            borderwidth=2,
            highlightthickness=2,
            highlightbackground="#F4C430",
            highlightcolor="#FFD700"
        )
        self.name_entry.pack(pady=3, padx=3, ipady=12)
        self.name_entry.insert(0, "Student")
        
        # Bind focus events for character animation
        self.name_entry.bind("<FocusIn>", lambda e: self.show_mini_character())
        self.name_entry.bind("<FocusOut>", lambda e: self.hide_mini_character())
        self.name_entry.bind("<KeyRelease>", lambda e: self.character_react_to_typing())
        
        # Professional animated sort button with 3D effect
        self.sort_button = tk.Button(
            self.canvas,
            text="✨ BEGIN SORTING CEREMONY ✨",
            command=self.start_sorting,
            font=("Palatino Linotype", 18, "bold"),
            bg="#740001",
            fg="#FFD700",
            activebackground="#AE0001",
            activeforeground="#FFC500",
            relief=tk.RAISED,
            borderwidth=3,
            padx=60,
            pady=20,
            cursor="hand2"
        )
        self.sort_button_window = self.canvas.create_window(
            600, 650,
            window=self.sort_button,
            tags="sort_btn",
            state="hidden"
        )
        
        # START button - shown initially in the center (using image)
        if self.begin_button_photo:
            # Create button using the image
            self.start_button = tk.Button(
                self.canvas,
                image=self.begin_button_photo,
                command=self.on_start_clicked,
                borderwidth=0,
                highlightthickness=0,
                relief=tk.FLAT,
                bg="#0a0a0f",
                activebackground="#0a0a0f",
                cursor="hand2"
            )
        else:
            # Fallback to text button if image not found
            self.start_button = tk.Button(
                self.canvas,
                text="⚡ START CEREMONY ⚡",
                command=self.on_start_clicked,
                font=("Palatino Linotype", 24, "bold"),
                bg="#740001",
                fg="#FFD700",
                activebackground="#AE0001",
                activeforeground="#FFC500",
                relief=tk.RAISED,
                borderwidth=4,
                padx=70,
                pady=25,
                cursor="hand2"
            )
        
        self.start_button_window = self.canvas.create_window(
            600, 400,
            window=self.start_button,
            tags="start_btn"
        )
        
        # Bind hover effects for START button (only for text button)
        if not self.begin_button_photo:
            self.start_button.bind("<Enter>", lambda e: self.on_button_hover(self.start_button, "#AE0001"))
            self.start_button.bind("<Leave>", lambda e: self.on_button_leave(self.start_button, "#740001"))
        
        # Result frame with professional styling
        self.result_frame = tk.Frame(self.canvas, bg="#0a0a0f")
        self.result_window = self.canvas.create_window(
            600, 300,
            window=self.result_frame,
            tags="result",
            state="hidden"
        )
        
        self.result_label = tk.Label(
            self.result_frame,
            text="",
            font=("Palatino Linotype", 20, "bold"),
            fg="#FFE",
            bg="#0a0a0f",
            justify=tk.CENTER,
            pady=40,
            padx=60
        )
        self.result_label.pack()
        
        # Professional maze button with enhanced styling
        self.maze_button = tk.Button(
            self.canvas,
            text="🌟 ENTER THE TRIWIZARD MAZE 🌟",
            command=self.start_maze,
            font=("Palatino Linotype", 15, "bold"),
            bg="#0E1A40",
            fg="#FFD700",
            activebackground="#222F5B",
            activeforeground="#FFC500",
            relief=tk.RAISED,
            borderwidth=3,
            padx=40,
            pady=16,
            cursor="hand2"
        )
        self.maze_button_window = self.canvas.create_window(
            600, 650,
            window=self.maze_button,
            tags="maze_btn",
            state="hidden"
        )
        
        # Professional restart button with enhanced styling
        self.restart_button = tk.Button(
            self.canvas,
            text="🔄 Sort Another Student",
            command=self.restart,
            font=("Georgia", 14, "bold"),
            bg="#1a1a2e",
            fg="#F4C430",
            activebackground="#2a2a3e",
            activeforeground="#FFE55C",
            relief=tk.RAISED,
            borderwidth=2,
            padx=35,
            pady=16,
            cursor="hand2"
        )
        self.restart_button_window = self.canvas.create_window(
            600, 730,
            window=self.restart_button,
            tags="restart_btn",
            state="hidden"
        )
        
        # Bind hover effects
        self.sort_button.bind("<Enter>", lambda e: self.on_button_hover(self.sort_button, "#AE0001"))
        self.sort_button.bind("<Leave>", lambda e: self.on_button_leave(self.sort_button, "#740001"))
        self.restart_button.bind("<Enter>", lambda e: self.on_button_hover(self.restart_button, "#2a2a3e"))
        self.restart_button.bind("<Leave>", lambda e: self.on_button_leave(self.restart_button, "#1a1a2e"))
        self.maze_button.bind("<Enter>", lambda e: self.on_button_hover(self.maze_button, "#222F5B"))
        self.maze_button.bind("<Leave>", lambda e: self.on_button_leave(self.maze_button, "#0E1A40"))
    
    def create_persistent_music_button(self):
        """Create a persistent speaker icon button that shows on every window"""
        # Create a fixed position button frame in top-right corner
        button_frame = tk.Frame(
            self.canvas,
            bg="#1a1a2e",
            relief=tk.RAISED,
            borderwidth=2
        )
        
        # Position in top-right corner (adjusted for larger canvas)
        self.persistent_music_window = self.canvas.create_window(
            1150, 35,
            window=button_frame,
            tags="persistent_music",
            anchor="e"
        )
        
        # Speaker icon button - Professional styling
        self.persistent_music_button = tk.Button(
            button_frame,
            text="🔊",
            command=self.toggle_music,
            font=("Segoe UI Emoji", 30),
            bg="#1a1a2e",
            fg="#FFD700",
            activebackground="#2a2a3e",
            activeforeground="#FFC500",
            relief=tk.FLAT,
            borderwidth=0,
            padx=14,
            pady=10,
            cursor="hand2",
            width=2,
            height=1
        )
        self.persistent_music_button.pack()
        
        # Add hover glow effect
        self.persistent_music_button.bind("<Enter>", lambda e: self.persistent_music_button.config(bg="#2a2a3e", fg="#FFC500"))
        self.persistent_music_button.bind("<Leave>", lambda e: self.persistent_music_button.config(bg="#1a1a2e", fg="#FFD700"))
        
        # Keep this button always visible
        self.canvas.tag_raise("persistent_music")
    
    def create_gradient_background(self):
        """Create professional animated gradient background with Hogwarts atmosphere"""
        # Create gradient rectangles for dark mystical theme
        for i in range(80):
            y = i * 10
            # Calculate color gradient from very dark to slightly lighter (night sky)
            r = 10 + int(i * 0.2)
            g = 10 + int(i * 0.15)
            b = 15 + int(i * 0.4)
            color = f"#{min(r, 35):02x}{min(g, 30):02x}{min(b, 50):02x}"
            self.canvas.create_rectangle(
                0, y, 1200, y + 10,
                fill=color,
                outline="",
                tags="gradient"
            )
        
        # Add starry night effect
        for _ in range(120):
            x = random.randint(0, 1200)
            y = random.randint(0, 400)
            size = random.randint(1, 2)
            brightness = random.choice(["#FFFFFF", "#FFE4B5", "#F0E68C"])
            self.canvas.create_oval(
                x, y, x + size, y + size,
                fill=brightness,
                outline="",
                tags="stars"
            )
        
        # Add castle silhouette pattern
        self.draw_castle_silhouette()
    
    def create_particles(self):
        """Create floating magical particle effect with varied colors"""
        # Create golden magical particles
        for _ in range(25):
            x = random.randint(0, 1200)
            y = random.randint(0, 800)
            size = random.randint(2, 5)
            speed = random.uniform(0.4, 1.8)
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
                'direction': random.choice([-1, 1]),
                'color_type': 'gold'
            }
            self.particles.append(particle)
        
        # Create blue mystical particles
        for _ in range(20):
            x = random.randint(0, 1200)
            y = random.randint(0, 800)
            size = random.randint(1, 3)
            speed = random.uniform(0.3, 1.2)
            particle = {
                'id': self.canvas.create_oval(
                    x, y, x + size, y + size,
                    fill="#5DADE2",
                    outline="",
                    tags="particle"
                ),
                'x': x,
                'y': y,
                'size': size,
                'speed': speed,
                'direction': random.choice([-1, 1]),
                'color_type': 'blue'
            }
            self.particles.append(particle)
    
    def animate_particles(self):
        """Animate floating magical particles with enhanced color effects"""
        for particle in self.particles:
            # Move particle
            particle['y'] -= particle['speed']
            particle['x'] += particle['direction'] * 0.3
            
            # Reset if out of bounds
            if particle['y'] < 0:
                particle['y'] = 800
                particle['x'] = random.randint(0, 1200)
            
            if particle['x'] < 0 or particle['x'] > 1200:
                particle['direction'] *= -1
            
            # Update position
            self.canvas.coords(
                particle['id'],
                particle['x'],
                particle['y'],
                particle['x'] + particle['size'],
                particle['y'] + particle['size']
            )
            
            # Pulse glow effect based on particle type
            alpha_val = int(128 + 127 * math.sin(time.time() * 2 + particle['x']))
            try:
                if particle['color_type'] == 'gold':
                    r = 244
                    g = max(196 - (255 - alpha_val) // 3, 140)
                    b = 48
                    self.canvas.itemconfig(particle['id'], fill=f"#{r:02x}{g:02x}{b:02x}")
                else:  # blue
                    r = 93
                    g = 173 + (255 - alpha_val) // 4
                    b = 226
                    self.canvas.itemconfig(particle['id'], fill=f"#{r:02x}{g:02x}{b:02x}")
            except:
                pass
        
        self.root.after(50, self.animate_particles)
    
    def draw_castle_silhouette(self):
        """Draw Hogwarts castle silhouette in background for ambiance"""
        # Far left tower
        self.canvas.create_polygon(
            50, 350, 80, 250, 110, 350,
            fill="#0f0f1a",
            outline="",
            tags="castle_bg"
        )
        
        # Far right tower
        self.canvas.create_polygon(
            1090, 350, 1120, 250, 1150, 350,
            fill="#0f0f1a",
            outline="",
            tags="castle_bg"
        )
        
        # Central castle structure (subtle)
        castle_points = [
            200, 350,  # bottom left
            200, 300,
            250, 280,
            250, 320,
            300, 300,
            300, 340,
            350, 320,
            350, 280,
            400, 260,  # central peak
            450, 280,
            450, 320,
            500, 300,
            500, 340,
            550, 320,
            550, 280,
            600, 300,
            600, 350   # bottom right
        ]
        self.canvas.create_polygon(
            castle_points,
            fill="#0f0f1a",
            outline="#1a1a2a",
            tags="castle_bg"
        )
        
        # Add some tower windows with faint lights
        window_positions = [(100, 300), (250, 310), (400, 285), (1100, 300)]
        for wx, wy in window_positions:
            self.canvas.create_rectangle(
                wx - 3, wy - 5, wx + 3, wy + 5,
                fill="#4a3820",
                outline="",
                tags="castle_bg"
            )
    
    def animate_background_pattern(self):
        """Animate subtle background patterns for depth"""
        self.background_animation_step += 0.02
        
        # Animate floating candles effect (for Great Hall atmosphere)
        if hasattr(self, 'candle_lights'):
            for candle_id in self.candle_lights:
                try:
                    # Flicker effect
                    flicker = math.sin(self.background_animation_step * 3 + candle_id) * 0.3 + 0.7
                    # This creates a subtle flicker but we'll skip color change for performance
                except:
                    pass
        
        self.root.after(100, self.animate_background_pattern)
    
    def create_themed_background(self, theme):
        """Create themed background based on current screen"""
        # Remove old themed elements
        self.canvas.delete("theme_bg")
        
        if theme == "welcome":
            self.create_welcome_theme()
        elif theme == "great_hall":
            self.create_great_hall_theme()
        elif theme == "result":
            self.create_result_theme()
        elif theme == "maze":
            self.create_maze_theme()
    
    def create_welcome_theme(self):
        """Create Hogwarts entrance theme"""
        # Add floating candles
        self.candle_lights = []
        for i in range(8):
            x = 150 + i * 130
            y = 100 + random.randint(-20, 20)
            # Candle flame
            candle = self.canvas.create_oval(
                x - 4, y - 8, x + 4, y + 8,
                fill="#FFA500",
                outline="#FFD700",
                tags="theme_bg"
            )
            self.candle_lights.append(candle)
            # Glow around candle
            self.canvas.create_oval(
                x - 10, y - 14, x + 10, y + 14,
                fill="",
                outline="#FFD700",
                tags="theme_bg"
            )
    
    def create_great_hall_theme(self):
        """Create Great Hall sorting ceremony atmosphere"""
        # Add house banners silhouettes
        banner_colors = ["#740001", "#FFDB00", "#0E1A40", "#1A472A"]
        for i, color in enumerate(banner_colors):
            x = 200 + i * 220
            # Banner pole
            self.canvas.create_rectangle(
                x - 2, 150, x + 2, 350,
                fill="#3d2817",
                outline="",
                tags="theme_bg"
            )
            # Banner cloth
            self.canvas.create_polygon(
                x - 40, 150,
                x + 40, 150,
                x + 40, 280,
                x, 300,
                x - 40, 280,
                fill=color,
                outline="",
                stipple="gray50",
                tags="theme_bg"
            )
    
    def create_result_theme(self):
        """Create house-specific result background"""
        if self.current_house:
            colors = self.house_colors[self.current_house]
            # Create house-colored overlay
            for i in range(50):
                y = i * 16
                # Parse hex color
                start_color = colors["bg_start"].lstrip('#')
                end_color = colors["bg_end"].lstrip('#')
                
                r_start, g_start, b_start = int(start_color[0:2], 16), int(start_color[2:4], 16), int(start_color[4:6], 16)
                r_end, g_end, b_end = int(end_color[0:2], 16), int(end_color[2:4], 16), int(end_color[4:6], 16)
                
                progress = i / 50
                r = int(r_start + (r_end - r_start) * progress)
                g = int(g_start + (g_end - g_start) * progress)
                b = int(b_start + (b_end - b_start) * progress)
                
                self.canvas.create_rectangle(
                    0, y, 1200, y + 16,
                    fill=f"#{r:02x}{g:02x}{b:02x}",
                    outline="",
                    tags="theme_bg"
                )
            
            # Add house-specific pattern
            self.draw_house_pattern(self.current_house)
    
    def create_maze_theme(self):
        """Create Forbidden Forest/Triwizard maze atmosphere"""
        # Dark forest ambiance
        for i in range(60):
            y = i * 13.3
            r = 15 + int(i * 0.1)
            g = 20 + int(i * 0.15)
            b = 15 + int(i * 0.1)
            self.canvas.create_rectangle(
                0, y, 1200, y + 13.3,
                fill=f"#{r:02x}{g:02x}{b:02x}",
                outline="",
                tags="theme_bg"
            )
    
    def draw_house_pattern(self, house):
        """Draw house-specific decorative patterns"""
        colors = self.house_colors[house]
        emoji = house_info[house]["emoji"]
        
        # Scatter house emblems in background
        for i in range(12):
            x = random.randint(100, 1100)
            y = random.randint(100, 700)
            self.canvas.create_text(
                x, y,
                text=emoji,
                font=("Segoe UI Emoji", random.randint(30, 60)),
                fill=colors["dark"],
                tags="theme_bg"
            )
    
    def start_animations(self):
        """Start all entrance animations - show title and START button"""
        self.animate_particles()
        self.create_themed_background("welcome")
        
        # Title and START button are visible from the beginning
        # Hat animation will start when START button is clicked
        self.pulse_start_button_glow()
    
    def on_start_clicked(self):
        """Handle START button click - show spinning hat then name entry"""
        # Hide START button
        self.canvas.itemconfig("start_btn", state="hidden")
        
        # Show spinning hat
        self.create_spinning_hat()
        
        # After 3 seconds, stop hat and show name entry
        self.root.after(3000, self.stop_hat_and_show_entry)
    
    def stop_hat_and_show_entry(self):
        """Stop the hat spinning animation and show name entry form"""
        self.hat_spinning = False
        # Fade out the hat
        self.fade_out_hat_to_entry()
    
    def fade_out_hat_to_entry(self, alpha=1.0):
        """Fade out the spinning hat and show entry form"""
        if alpha > 0:
            alpha -= 0.05
            # Move hat up while fading
            self.canvas.move("spinning_hat", 0, -5)
            self.root.after(30, lambda: self.fade_out_hat_to_entry(alpha))
        else:
            # Remove the hat and show entry form
            self.canvas.delete("spinning_hat")
            # Show name entry and sort button
            self.canvas.itemconfig("entry", state="normal")
            self.canvas.itemconfig("sort_btn", state="normal")
            self.pulse_glow_effect()
    
    def pulse_start_button_glow(self):
        """Create pulsing glow effect for START button"""
        # Only apply glow to text button, not image button
        if self.begin_button_photo:
            return
            
        if not hasattr(self, 'start_glow_alpha'):
            self.start_glow_alpha = 0
            self.start_glow_direction = 1
        
        self.start_glow_alpha += 0.04 * self.start_glow_direction
        
        if self.start_glow_alpha >= 1:
            self.start_glow_direction = -1
        elif self.start_glow_alpha <= 0:
            self.start_glow_direction = 1
        
        # Update button glow
        glow_intensity_r = int(116 + 58 * self.start_glow_alpha)
        glow_intensity_g = int(0 + 1 * self.start_glow_alpha)
        try:
            if hasattr(self, 'start_button'):
                self.start_button.config(bg=f"#{glow_intensity_r:02x}{glow_intensity_g:02x}01")
        except:
            pass
        
        # Continue pulsing if START button is still visible
        try:
            if self.canvas.itemcget("start_btn", "state") != "hidden":
                self.root.after(60, self.pulse_start_button_glow)
        except:
            pass
    
    def animate_title_entrance(self):
        """Animate title sliding down with elegance (including shadow) - DEPRECATED"""
        # This method is no longer used as title is visible from start
        pass
    
    def fade_in_content(self):
        """Fade in the main content smoothly - DEPRECATED"""
        # This method is no longer used in new flow
        pass
    
    def pulse_glow_effect(self):
        """Create professional pulsing glow effect around buttons"""
        self.glow_alpha += 0.04 * self.glow_direction
        
        if self.glow_alpha >= 1:
            self.glow_direction = -1
        elif self.glow_alpha <= 0:
            self.glow_direction = 1
        
        # Update button glow with smooth transitions (enhanced colors)
        glow_intensity_r = int(116 + 58 * self.glow_alpha)  # 116 to 174
        glow_intensity_g = int(0 + 1 * self.glow_alpha)     # 0 to 1
        try:
            self.sort_button.config(bg=f"#{glow_intensity_r:02x}{glow_intensity_g:02x}01")
        except:
            pass
        
        self.root.after(60, self.pulse_glow_effect)
    
    def show_mini_character(self):
        """Show animated mini character when typing name"""
        if not self.character_visible:
            self.character_visible = True
            
            # Create owl character elements (adjusted for larger canvas)
            # Owl body
            self.character_elements.append(
                self.canvas.create_text(
                    850, 520,
                    text="🦉",
                    font=("Segoe UI Emoji", 56),
                    tags="mini_char"
                )
            )
            
            # Professional speech bubble
            bubble_frame = tk.Frame(self.canvas, bg="#1a1a2e", relief=tk.RAISED, borderwidth=2)
            bubble_window = self.canvas.create_window(
                980, 500,
                window=bubble_frame,
                tags="mini_char"
            )
            self.character_elements.append(bubble_window)
            
            bubble_text = tk.Label(
                bubble_frame,
                text="  A fine name!\n  Let's sort you!  ",
                font=("Georgia", 12, "italic", "bold"),
                fg="#FFD700",
                bg="#1a1a2e",
                justify=tk.LEFT
            )
            bubble_text.pack(padx=10, pady=6)
            
            # Add glow outline to bubble
            self.canvas.create_rectangle(
                925, 475, 1035, 525,
                outline="#F4C430",
                width=2,
                tags="mini_char"
            )
            
            # Star particles around character (more magical)
            for i in range(8):
                angle = (i * 45) * (math.pi / 180)
                x = 850 + 50 * math.cos(angle)
                y = 520 + 50 * math.sin(angle)
                star = self.canvas.create_text(
                    x, y,
                    text="✨",
                    font=("Segoe UI Emoji", 16),
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
            self.character_y_offset += 0.3 * self.character_bounce_direction
            
            if self.character_y_offset > 10:
                self.character_bounce_direction = -1
            elif self.character_y_offset < -10:
                self.character_bounce_direction = 1
            
            # Move all character elements
            for element in self.character_elements:
                try:
                    coords = self.canvas.coords(element)
                    if len(coords) >= 2:
                        current_y = coords[1]
                        # Only apply vertical movement
                        self.canvas.coords(element, coords[0], 520 + self.character_y_offset if element == self.character_elements[0] else current_y)
                except:
                    pass
            
            self.root.after(30, self.animate_character_bounce)
    
    def character_react_to_typing(self):
        """Character reacts when user types with magical sparkles"""
        if self.character_visible and len(self.character_elements) > 0:
            # Create magical sparkle effect when typing
            x = 850 + random.randint(-40, 40)
            y = 520 + random.randint(-40, 40)
            sparkle = self.canvas.create_text(
                x, y,
                text=random.choice(["✨", "⭐", "💫", "🌟"]),
                font=("Segoe UI Emoji", 18),
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
    
    def load_background_assets(self):
        """Load animated background assets (Hogwarts castle + floating witches)"""
        try:
            # Load Hogwarts background image (JPG format)
            bg_path = "assests/hogwarts_bg.jpg"
            if os.path.exists(bg_path):
                self.bg_image = Image.open(bg_path)
                self.bg_image = self.bg_image.resize((1200, 800), Image.Resampling.LANCZOS)
                self.bg_photo = ImageTk.PhotoImage(self.bg_image)
                print("✅ Hogwarts background loaded from hogwarts_bg.jpg!")
            else:
                print(f"⚠️ Background not found: {bg_path}")
                print("   Using gradient background instead.")
            
            # Load single witch image and use it for all 3 witches
            witch_path = "assests/witch1.png"
            if os.path.exists(witch_path):
                witch_img = Image.open(witch_path).resize((80, 80), Image.Resampling.LANCZOS)
                witch_photo = ImageTk.PhotoImage(witch_img)
                # Use the same image for all 3 witches (they'll have different positions/speeds)
                self.witch_images = [witch_photo, witch_photo, witch_photo]
                print(f"✅ Loaded witch1.png - creating 3 flying witches!")
            else:
                print(f"⚠️ Witch image not found: {witch_path}")
                print("   Add witch1.png with transparent background to assests folder")
                
        except Exception as e:
            print(f"⚠️ Could not load background assets: {e}")
    
    def load_hat_image(self):
        """Load the sorting hat image for spinning animation"""
        try:
            # Try to load hat.jpeg
            hat_path = "assests/hat.jpeg"
            if os.path.exists(hat_path):
                self.hat_image = Image.open(hat_path)
                
                # Remove background by making it transparent
                self.hat_image = self.hat_image.convert("RGBA")
                datas = self.hat_image.getdata()
                
                # Get the background color from corner (top-left pixel)
                bg_color = self.hat_image.getpixel((0, 0))[:3]
                
                # Create new image data with transparency
                newData = []
                for item in datas:
                    # Calculate color difference from background
                    r_diff = abs(item[0] - bg_color[0])
                    g_diff = abs(item[1] - bg_color[1])
                    b_diff = abs(item[2] - bg_color[2])
                    
                    # If pixel is similar to background color, make it transparent
                    # Threshold of 40 allows for slight variations in background
                    if r_diff < 40 and g_diff < 40 and b_diff < 40:
                        newData.append((255, 255, 255, 0))  # Transparent
                    else:
                        newData.append(item)
                
                self.hat_image.putdata(newData)
                
                # Resize to appropriate size (keeping aspect ratio)
                self.hat_image = self.hat_image.resize((300, 300), Image.Resampling.LANCZOS)
                self.hat_photo = ImageTk.PhotoImage(self.hat_image)
                print("✅ Sorting Hat image loaded from hat.jpeg with background removed!")
            else:
                print(f"⚠️ Hat image not found: {hat_path}")
                print("   Please add hat.jpeg to the assests folder for the spinning animation")
                # Create a fallback text-based hat
                self.hat_photo = None
        except Exception as e:
            print(f"⚠️ Could not load hat image: {e}")
            self.hat_photo = None
    
    def load_begin_button_image(self):
        """Load the begin button image"""
        try:
            button_path = "assests/images.jpeg"
            if os.path.exists(button_path):
                self.begin_button_image = Image.open(button_path)
                # Resize to appropriate button size (width, height)
                self.begin_button_image = self.begin_button_image.resize((300, 150), Image.Resampling.LANCZOS)
                self.begin_button_photo = ImageTk.PhotoImage(self.begin_button_image)
                print("✅ Begin button image loaded from images.jpeg!")
            else:
                print(f"⚠️ Begin button image not found: {button_path}")
                print("   Using default text button instead")
                self.begin_button_photo = None
        except Exception as e:
            print(f"⚠️ Could not load begin button image: {e}")
            self.begin_button_photo = None
    
    def create_spinning_hat(self):
        """Create the spinning hat at the center of the screen"""
        if self.hat_photo:
            # Use the actual image
            self.hat_id = self.canvas.create_image(
                600, 400,
                image=self.hat_photo,
                tags="spinning_hat"
            )
        else:
            # Fallback to emoji hat
            self.hat_id = self.canvas.create_text(
                600, 400,
                text="🎩",
                font=("Segoe UI Emoji", 150),
                tags="spinning_hat"
            )
        
        # Start the spinning animation
        self.animate_spinning_hat()
    
    def animate_spinning_hat(self):
        """Animate the hat with floating up-down motion (pop-up/bounce effect)"""
        if not self.hat_spinning:
            return
        
        # Calculate vertical movement
        dy = self.hat_y_speed * self.hat_y_direction
        
        # Move the hat vertically
        self.canvas.move(self.hat_id, 0, dy)
        self.hat_y_offset += dy
        
        # Reverse direction when reaching the limits
        if abs(self.hat_y_offset) >= self.hat_y_range:
            self.hat_y_direction *= -1
        
        # Continue animation
        if self.hat_spinning:
            self.root.after(30, self.animate_spinning_hat)  # ~33fps for smooth motion
    
    def stop_hat_spinning(self):
        """Stop the hat spinning animation and proceed to main content - DEPRECATED"""
        # This method is replaced by stop_hat_and_show_entry in new flow
        self.hat_spinning = False
        self.fade_out_hat()
    
    def fade_out_hat(self, alpha=1.0):
        """Fade out the spinning hat - DEPRECATED"""
        # This method is replaced by fade_out_hat_to_entry in new flow
        if alpha > 0:
            alpha -= 0.05
            self.canvas.move("spinning_hat", 0, -5)
            self.root.after(30, lambda: self.fade_out_hat(alpha))
        else:
            self.canvas.delete("spinning_hat")
    
    def create_animated_background(self):
        """Create the Hogwarts castle background (static image)"""
        if self.bg_photo:
            try:
                self.bg_id = self.canvas.create_image(
                    0, 0,
                    image=self.bg_photo,
                    anchor="nw",
                    tags="animated_bg"
                )
                # Ensure it's at the very back
                self.canvas.tag_lower("animated_bg")
                print("✅ Animated background created!")
            except Exception as e:
                print(f"⚠️ Could not create animated background: {e}")
    
    def create_witches(self):
        """Create floating witches that will animate across the screen"""
        if not self.witch_images:
            return
        
        try:
            num_witches = len(self.witch_images)
            
            for i in range(num_witches):
                x = random.randint(100, 1100)
                y = random.randint(100, 400)
                
                witch = self.canvas.create_image(
                    x, y,
                    image=self.witch_images[i],
                    tags="witch"
                )
                
                self.witches.append({
                    "id": witch,
                    "dx": random.choice([-1, 1]) * random.uniform(0.5, 1.2),
                    "dy": random.uniform(-0.3, 0.3)
                })
            
            print(f"✅ Created {num_witches} floating witches!")
        except Exception as e:
            print(f"⚠️ Could not create witches: {e}")
    
    def animate_witches(self):
        """Animate the floating witches (smooth movement across screen)"""
        if not self.witches:
            return
        
        try:
            for witch in self.witches:
                # Move witch
                self.canvas.move(witch["id"], witch["dx"], witch["dy"])
                coords = self.canvas.coords(witch["id"])
                
                if len(coords) >= 2:
                    x, y = coords[0], coords[1]
                    
                    # If witch goes off screen → reset to opposite side
                    if x < -100:
                        self.canvas.coords(witch["id"], 1300, random.randint(100, 400))
                    elif x > 1300:
                        self.canvas.coords(witch["id"], -100, random.randint(100, 400))
                    
                    # Keep vertical position in bounds
                    if y < 50:
                        witch["dy"] = abs(witch["dy"])
                    elif y > 450:
                        witch["dy"] = -abs(witch["dy"])
        except Exception as e:
            pass  # Silent fail to avoid spam
        
        # Continue animation
        self.root.after(40, self.animate_witches)
    
    def fix_layering(self):
        """Fix z-order layering to ensure proper visual hierarchy"""
        # Layer order (bottom to top):
        # 1. Animated background (Hogwarts castle)
        # 2. Gradient & stars
        # 3. Castle silhouette
        # 4. Witches (floating in sky)
        # 5. Decorations
        # 6. Particles
        # 7. UI elements (title, welcome, buttons)
        # 8. Music button (always on top)
        
        try:
            self.canvas.tag_lower("animated_bg")
            self.canvas.tag_raise("gradient")
            self.canvas.tag_raise("stars")
            self.canvas.tag_raise("castle_bg")
            self.canvas.tag_raise("witch")
            self.canvas.tag_raise("decoration")
            self.canvas.tag_raise("particle")
            self.canvas.tag_raise("title")
            self.canvas.tag_raise("subtitle")
            self.canvas.tag_raise("welcome")
            self.canvas.tag_raise("welcome_glow")
            self.canvas.tag_raise("entry")
            self.canvas.tag_raise("sort_btn")
            self.canvas.tag_raise("result")
            self.canvas.tag_raise("persistent_music")
        except Exception as e:
            print(f"⚠️ Layering adjustment failed: {e}")
    
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
        # Switch to Great Hall theme
        self.create_themed_background("great_hall")
        
        thinking_frame = tk.Frame(self.canvas, bg="#1a1a2e", padx=60, pady=40, relief=tk.RAISED, borderwidth=3)
        thinking_window = self.canvas.create_window(600, 420, window=thinking_frame, tags="thinking")
        
        # Add glow outline
        self.canvas.create_rectangle(
            300, 330, 900, 510,
            outline="#FFD700",
            width=3,
            tags="thinking"
        )
        
        thinking_label = tk.Label(
            thinking_frame,
            text=f"🤔 Hmm... {name}...\nDifficult. Very difficult...\n\n✨ Analyzing your magical traits... ✨",
            font=("Palatino Linotype", 19, "bold"),
            fg="#FFD700",
            bg="#1a1a2e",
            justify=tk.CENTER
        )
        thinking_label.pack()
        
        # Ensure music button stays on top
        self.canvas.tag_raise("persistent_music")
        
        # Animated dots
        self.animate_thinking_dots(thinking_label, 0, name)
    
    def animate_thinking_dots(self, label, count, name):
        """Animate thinking dots with professional timing"""
        if count < 20:
            dots = "." * ((count % 4) + 1)
            label.config(text=f"🤔 Hmm... {name}...\nDifficult. Very difficult{dots}\n\n✨ Analyzing your magical traits... ✨")
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
        center_x, center_y = 600, 420
        explosion_particles = []
        
        for _ in range(80):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(5, 15)
            size = random.randint(5, 14)
            
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
                'life': 28
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
        """Display final sorting result with professional animation and themed background"""
        # Switch to house-specific themed background
        self.current_house = house
        self.current_theme = "result"
        self.create_themed_background("result")
        
        # Clear any existing result
        self.result_label.config(text="")
        
        # Configure result display with professional styling
        result_text = f"🎉 CONGRATULATIONS, {name.upper()}! 🎉\n\n"
        result_text += f"You have been sorted into\n\n"
        result_text += f"{emoji} {house.upper()} {emoji}\n\n"
        result_text += f"{traits}\n"
        result_text += f"Founded by: {founder}"
        
        self.result_frame.config(bg=colors["primary"], relief=tk.RAISED, borderwidth=4)
        self.result_label.config(
            text=result_text,
            bg=colors["primary"],
            fg="#FFFACD"  # Lemon chiffon for better readability
        )
        
        # Show the four house castles and animate student walking to selected house
        self.show_houses_and_walking_student(house)
        
        # Ensure music button stays visible
        self.canvas.tag_raise("persistent_music")
        
        # Show result with slide-in animation after walking animation
        self.root.after(4500, lambda: self.show_final_result_panel())
        
        # Re-enable button
        self.sort_button.config(state=tk.NORMAL)
    
    def slide_in_result(self, current_y, target_y):
        """Slide in result animation with smooth easing"""
        if current_y < target_y:
            current_y += 10
            self.canvas.coords(self.result_window, 600, current_y)
            self.root.after(20, lambda: self.slide_in_result(current_y, target_y))
        else:
            # Ensure music button stays on top
            self.canvas.tag_raise("persistent_music")
    
    def show_houses_and_walking_student(self, selected_house):
        """Display 4 house castles and animate student walking to selected house"""
        # Castle positions (left to right: Gryffindor, Hufflepuff, Ravenclaw, Slytherin)
        # Adjusted for larger canvas
        castle_positions = {
            "Gryffindor": 200,
            "Hufflepuff": 450,
            "Ravenclaw": 700,
            "Slytherin": 950
        }
        
        # Draw all 4 castles
        for house_name, x_pos in castle_positions.items():
            self.draw_castle(x_pos, 500, house_name, house_name == selected_house)
        
        # Create and animate student walking to selected house
        target_x = castle_positions[selected_house]
        self.create_walking_student(120, 550, target_x, selected_house)
    
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
        
        # Fix layering to ensure proper display
        self.fix_layering()
        
        # Ensure music button stays on top
        self.canvas.tag_raise("persistent_music")
        
        # Animate result sliding in
        self.slide_in_result(120, 250)
    
    def restart(self):
        """Restart the sorting process with professional fade out animation"""
        # Hide result elements
        self.canvas.itemconfig("result", state="hidden")
        self.canvas.itemconfig("restart_btn", state="hidden")
        
        # Clear castle and student animations
        self.canvas.delete("castle")
        self.canvas.delete("castle_glow")
        self.canvas.delete("student")
        self.canvas.delete("theme_bg")
        self.canvas.delete("result_decoration")  # Clean up result decorations
        
        # Reset theme
        self.current_theme = "welcome"
        self.current_house = None
        self.create_themed_background("welcome")
        
        # Reset and show input elements
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, "Student")
        
        self.result_frame.config(bg="#0a0a0f", relief=tk.FLAT, borderwidth=0)
        self.result_label.config(text="", bg="#0a0a0f")
        
        # Hide maze button
        self.canvas.itemconfig("maze_btn", state="hidden")
        
        # Hide entry form and show START button again
        self.canvas.itemconfig("welcome", state="hidden")
        self.canvas.itemconfig("welcome_glow", state="hidden")
        self.canvas.itemconfig("entry", state="hidden")
        self.canvas.itemconfig("sort_btn", state="hidden")
        
        # Show START button
        self.canvas.itemconfig("start_btn", state="normal")
        self.pulse_start_button_glow()
        
        # Fix layering after restart
        self.fix_layering()
        
        # Ensure music button stays on top
        self.canvas.tag_raise("persistent_music")
    
    def start_maze(self):
        """Start the maze challenge with Forbidden Forest theme"""
        # Hide all previous elements
        self.canvas.itemconfig("result", state="hidden")
        self.canvas.itemconfig("restart_btn", state="hidden")
        self.canvas.itemconfig("maze_btn", state="hidden")
        self.canvas.delete("castle")
        self.canvas.delete("castle_glow")
        self.canvas.delete("theme_bg")
        self.canvas.delete("result_decoration")  # Clean up result decorations
        
        # Switch to maze theme
        self.current_theme = "maze"
        self.create_themed_background("maze")
        
        # Fix layering for maze screen
        self.fix_layering()
        
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
        # Seed random generator with current time for unique mazes each run
        random.seed(time.time())
        
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
        """Draw the maze on canvas with professional Forbidden Forest styling"""
        self.canvas.delete("maze")
        
        # Calculate offset to center maze
        maze_width = self.maze_size * self.cell_size
        offset_x = (1200 - maze_width) // 2
        offset_y = 120
        
        # Draw professional title with shadow
        self.canvas.create_text(
            602, 57,
            text="🌟 THE TRIWIZARD MAZE 🌟",
            font=("Copperplate Gothic Bold", 26, "bold"),
            fill="#000000",
            tags="maze"
        )
        self.canvas.create_text(
            600, 55,
            text="🌟 THE TRIWIZARD MAZE 🌟",
            font=("Copperplate Gothic Bold", 26, "bold"),
            fill="#FFD700",
            tags="maze"
        )
        
        # Draw maze cells with Forbidden Forest colors
        for y in range(self.maze_size):
            for x in range(self.maze_size):
                x1 = offset_x + x * self.cell_size
                y1 = offset_y + y * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                if self.maze[y][x] == 1:
                    # Wall - dark forest green/brown
                    self.canvas.create_rectangle(
                        x1, y1, x2, y2,
                        fill="#1a3025",
                        outline="#0f2019",
                        width=2,
                        tags="maze"
                    )
                else:
                    # Path - misty ground
                    self.canvas.create_rectangle(
                        x1, y1, x2, y2,
                        fill="#2a3a35",
                        outline="#1a2a25",
                        tags="maze"
                    )
        
        # Draw exit with magical glow effect
        exit_x1 = offset_x + self.exit_pos[0] * self.cell_size
        exit_y1 = offset_y + self.exit_pos[1] * self.cell_size
        exit_x2 = exit_x1 + self.cell_size
        exit_y2 = exit_y1 + self.cell_size
        
        # Multiple glow layers
        for i in range(3):
            self.canvas.create_rectangle(
                exit_x1 - i*3, exit_y1 - i*3, exit_x2 + i*3, exit_y2 + i*3,
                fill="",
                outline="#FFD700",
                width=2,
                tags="maze"
            )
        
        self.canvas.create_rectangle(
            exit_x1, exit_y1, exit_x2, exit_y2,
            fill="#5DBE71",
            outline="#FFD700",
            width=4,
            tags="maze"
        )
        self.canvas.create_text(
            exit_x1 + self.cell_size // 2,
            exit_y1 + self.cell_size // 2,
            text="🏆",
            font=("Segoe UI Emoji", 30),
            tags="maze"
        )
        
        # Ensure music button stays on top
        self.canvas.tag_raise("persistent_music")
        
        # Draw player
        self.draw_player()
    
    def draw_player(self):
        """Draw the player on the maze with enhanced visuals"""
        self.canvas.delete("player")
        
        maze_width = self.maze_size * self.cell_size
        offset_x = (1200 - maze_width) // 2
        offset_y = 120
        
        x = offset_x + self.player_pos[0] * self.cell_size + self.cell_size // 2
        y = offset_y + self.player_pos[1] * self.cell_size + self.cell_size // 2
        
        # Draw player glow effect
        self.canvas.create_oval(
            x - 22, y - 22, x + 22, y + 22,
            fill="",
            outline="#FFD700",
            width=2,
            tags="player"
        )
        
        # Draw player as a wizard with wand light
        self.canvas.create_text(
            x, y,
            text="🧙",
            font=("Segoe UI Emoji", 36),
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
        instructions = tk.Frame(self.canvas, bg="#1a1a2e", relief=tk.RAISED, borderwidth=2)
        instructions_window = self.canvas.create_window(
            600, 770,
            window=instructions,
            tags="maze"
        )
        
        instructions_label = tk.Label(
            instructions,
            text="Use Arrow Keys ⬆️⬇️⬅️➡️ to navigate through the maze | Find the Triwizard Cup 🏆",
            font=("Palatino Linotype", 13, "bold"),
            fg="#FFD700",
            bg="#1a1a2e",
            padx=30,
            pady=12
        )
        instructions_label.pack()
        
        # Add back button to return from maze
        back_button = tk.Button(
            self.canvas,
            text="⬅️ Back to Sorting Hat",
            command=self.return_from_maze,
            font=("Georgia", 12, "bold"),
            bg="#2a3a35",
            fg="#FFD700",
            activebackground="#3a4a45",
            activeforeground="#FFC500",
            relief=tk.RAISED,
            borderwidth=2,
            padx=25,
            pady=12,
            cursor="hand2"
        )
        back_window = self.canvas.create_window(120, 770, window=back_button, tags="maze")
        
        # Ensure music button stays on top
        self.canvas.tag_raise("persistent_music")
    
    def maze_completed(self):
        """Handle maze completion with professional UI"""
        self.maze_active = False
        
        # Show congratulations with professional styling
        congrats_frame = tk.Frame(self.canvas, bg="#1a1a2e", relief=tk.RAISED, borderwidth=4)
        congrats_window = self.canvas.create_window(600, 420, window=congrats_frame, tags="maze")
        
        # Add multiple glow outlines
        for i in range(3):
            self.canvas.create_rectangle(
                250 - i*10, 300 - i*10, 950 + i*10, 540 + i*10,
                outline="#FFD700",
                width=2,
                tags="maze"
            )
        
        congrats_label = tk.Label(
            congrats_frame,
            text="🎉 CONGRATULATIONS! 🎉\n\nYou've successfully navigated\nthe Triwizard Maze!\n\n⭐ The Triwizard Cup is yours! ⭐\n\nWell Done, Champion Wizard!",
            font=("Palatino Linotype", 20, "bold"),
            fg="#FFD700",
            bg="#1a1a2e",
            justify=tk.CENTER,
            padx=60,
            pady=40
        )
        congrats_label.pack()
        
        # Add professional return button
        return_button = tk.Button(
            self.canvas,
            text="🔄 Return to Sorting Hat",
            command=self.return_from_maze,
            font=("Palatino Linotype", 15, "bold"),
            bg="#740001",
            fg="#FFD700",
            activebackground="#AE0001",
            activeforeground="#FFC500",
            relief=tk.RAISED,
            borderwidth=3,
            padx=40,
            pady=18,
            cursor="hand2"
        )
        return_window = self.canvas.create_window(600, 600, window=return_button, tags="maze")
        
        # Ensure music button stays on top
        self.canvas.tag_raise("persistent_music")
    
    def return_from_maze(self):
        """Return to the main screen"""
        self.canvas.delete("maze")
        self.canvas.delete("player")
        self.canvas.delete("theme_bg")
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