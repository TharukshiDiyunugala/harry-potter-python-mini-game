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
    """GUI Application for the Sorting Hat with Modern Animations"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Hogwarts Sorting Hat Ceremony")
        self.root.geometry("900x700")
        
        # Configure window
        self.root.configure(bg="#0a0a1a")
        self.root.resizable(False, False)
        
        # Music state
        self.music_playing = False
        
        # Animation variables
        self.particles = []
        self.glow_alpha = 0
        self.glow_direction = 1
        self.title_y = -100
        self.content_alpha = 0
        
        # Mini character animation variables
        self.character_visible = False
        self.character_y_offset = 0
        self.character_bounce_direction = 1
        self.character_elements = []
        
        # House colors with gradients
        self.house_colors = {
            "Gryffindor": {"primary": "#740001", "secondary": "#D3A625", "glow": "#FFD700"},
            "Hufflepuff": {"primary": "#FFD700", "secondary": "#000000", "glow": "#FFEB3B"},
            "Ravenclaw": {"primary": "#0E1A40", "secondary": "#946B2D", "glow": "#2196F3"},
            "Slytherin": {"primary": "#1A472A", "secondary": "#5D5D5D", "glow": "#4CAF50"}
        }
        
        # Create canvas for custom drawing
        self.canvas = tk.Canvas(
            self.root,
            width=900,
            height=700,
            bg="#0a0a1a",
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.create_widgets()
        self.start_animations()
    
    def create_widgets(self):
        """Create all GUI widgets with animation-ready structure"""
        
        # Background gradient effect
        self.create_gradient_background()
        
        # Animated particles
        self.create_particles()
        
        # Title with fade-in animation
        self.title_text = self.canvas.create_text(
            450, self.title_y,
            text="🎩 HOGWARTS SORTING HAT 🎩",
            font=("Helvetica", 32, "bold"),
            fill="#FFD700",
            tags="title"
        )
        
        self.subtitle_text = self.canvas.create_text(
            450, 120,
            text="✨ The Magical Sorting Ceremony ✨",
            font=("Helvetica", 14, "italic"),
            fill="#FFFFFF",
            tags="subtitle",
            state="hidden"
        )
        
        # Glowing frame for welcome message
        self.welcome_frame = tk.Frame(
            self.canvas,
            bg="#1a1a3e",
            relief=tk.FLAT,
            borderwidth=0
        )
        self.welcome_window = self.canvas.create_window(
            450, 250,
            window=self.welcome_frame,
            tags="welcome",
            state="hidden"
        )
        
        self.welcome_text = tk.Label(
            self.welcome_frame,
            text="Welcome to Hogwarts!\n\nThe Sorting Hat will determine\nwhich house you belong to...\n\n🦁 Gryffindor  🦡 Hufflepuff\n🦅 Ravenclaw  🐍 Slytherin",
            font=("Helvetica", 12),
            fg="#FFFFFF",
            bg="#1a1a3e",
            justify=tk.CENTER,
            pady=20,
            padx=30
        )
        self.welcome_text.pack()
        
        # Name entry with glow effect
        self.entry_frame = tk.Frame(self.canvas, bg="#0a0a1a")
        self.entry_window = self.canvas.create_window(
            450, 420,
            window=self.entry_frame,
            tags="entry",
            state="hidden"
        )
        
        self.name_label = tk.Label(
            self.entry_frame,
            text="Enter your name:",
            font=("Helvetica", 13),
            fg="#FFD700",
            bg="#0a0a1a"
        )
        self.name_label.pack(pady=5)
        
        # Custom styled entry
        self.name_entry = tk.Entry(
            self.entry_frame,
            font=("Helvetica", 16),
            width=25,
            justify=tk.CENTER,
            bg="#1a1a3e",
            fg="#FFFFFF",
            insertbackground="#FFD700",
            relief=tk.FLAT,
            borderwidth=2
        )
        self.name_entry.pack(pady=10, ipady=8)
        self.name_entry.insert(0, "Student")
        
        # Bind focus events for character animation
        self.name_entry.bind("<FocusIn>", lambda e: self.show_mini_character())
        self.name_entry.bind("<FocusOut>", lambda e: self.hide_mini_character())
        self.name_entry.bind("<KeyRelease>", lambda e: self.character_react_to_typing())
        
        # Animated sort button
        self.sort_button = tk.Button(
            self.canvas,
            text="🎩 BEGIN SORTING 🎩",
            command=self.start_sorting,
            font=("Helvetica", 16, "bold"),
            bg="#8B0000",
            fg="white",
            activebackground="#B22222",
            activeforeground="white",
            relief=tk.FLAT,
            borderwidth=0,
            padx=40,
            pady=15,
            cursor="hand2"
        )
        self.sort_button_window = self.canvas.create_window(
            450, 530,
            window=self.sort_button,
            tags="sort_btn",
            state="hidden"
        )
        
        # Music button
        self.music_button = tk.Button(
            self.canvas,
            text="🎵 Play Music",
            command=self.toggle_music,
            font=("Helvetica", 10),
            bg="#2a2a4e",
            fg="white",
            activebackground="#3a3a6e",
            activeforeground="white",
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2"
        )
        self.music_button_window = self.canvas.create_window(
            450, 600,
            window=self.music_button,
            tags="music_btn",
            state="hidden"
        )
        
        # Result frame
        self.result_frame = tk.Frame(self.canvas, bg="#0a0a1a")
        self.result_window = self.canvas.create_window(
            450, 350,
            window=self.result_frame,
            tags="result",
            state="hidden"
        )
        
        self.result_label = tk.Label(
            self.result_frame,
            text="",
            font=("Helvetica", 18, "bold"),
            fg="white",
            bg="#0a0a1a",
            justify=tk.CENTER,
            pady=30,
            padx=40
        )
        self.result_label.pack()
        
        # Restart button
        self.restart_button = tk.Button(
            self.canvas,
            text="🔄 Sort Another Student",
            command=self.restart,
            font=("Helvetica", 12),
            bg="#2a2a4e",
            fg="white",
            activebackground="#3a3a6e",
            activeforeground="white",
            relief=tk.FLAT,
            padx=25,
            pady=12,
            cursor="hand2"
        )
        self.restart_button_window = self.canvas.create_window(
            450, 620,
            window=self.restart_button,
            tags="restart_btn",
            state="hidden"
        )
        
        # Bind hover effects
        self.sort_button.bind("<Enter>", lambda e: self.on_button_hover(self.sort_button, "#B22222"))
        self.sort_button.bind("<Leave>", lambda e: self.on_button_leave(self.sort_button, "#8B0000"))
        self.music_button.bind("<Enter>", lambda e: self.on_button_hover(self.music_button, "#3a3a6e"))
        self.music_button.bind("<Leave>", lambda e: self.on_button_leave(self.music_button, "#2a2a4e"))
        self.restart_button.bind("<Enter>", lambda e: self.on_button_hover(self.restart_button, "#3a3a6e"))
        self.restart_button.bind("<Leave>", lambda e: self.on_button_leave(self.restart_button, "#2a2a4e"))
    
    def create_gradient_background(self):
        """Create animated gradient background"""
        # Create gradient rectangles
        for i in range(50):
            y = i * 14
            # Calculate color gradient from dark blue to dark purple
            color_val = int(10 + (i * 0.3))
            color = f"#{color_val:02x}{color_val:02x}{min(color_val + 10, 40):02x}"
            self.canvas.create_rectangle(
                0, y, 900, y + 14,
                fill=color,
                outline="",
                tags="gradient"
            )
    
    def create_particles(self):
        """Create floating particle effect"""
        for _ in range(30):
            x = random.randint(0, 900)
            y = random.randint(0, 700)
            size = random.randint(2, 5)
            speed = random.uniform(0.5, 2)
            particle = {
                'id': self.canvas.create_oval(
                    x, y, x + size, y + size,
                    fill="#FFD700",
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
        """Animate floating particles"""
        for particle in self.particles:
            # Move particle
            particle['y'] -= particle['speed']
            particle['x'] += particle['direction'] * 0.3
            
            # Reset if out of bounds
            if particle['y'] < 0:
                particle['y'] = 700
                particle['x'] = random.randint(0, 900)
            
            if particle['x'] < 0 or particle['x'] > 900:
                particle['direction'] *= -1
            
            # Update position
            self.canvas.coords(
                particle['id'],
                particle['x'],
                particle['y'],
                particle['x'] + particle['size'],
                particle['y'] + particle['size']
            )
            
            # Pulse effect
            alpha_val = int(128 + 127 * math.sin(time.time() * 2 + particle['x']))
            try:
                self.canvas.itemconfig(particle['id'], fill=f"#{alpha_val:02x}{alpha_val:02x}00")
            except:
                pass
        
        self.root.after(50, self.animate_particles)
    
    def start_animations(self):
        """Start all entrance animations"""
        self.animate_particles()
        self.animate_title_entrance()
    
    def animate_title_entrance(self):
        """Animate title sliding down"""
        if self.title_y < 60:
            self.title_y += 3
            self.canvas.coords(self.title_text, 450, self.title_y)
            self.root.after(20, self.animate_title_entrance)
        else:
            # Show subtitle after title
            self.canvas.itemconfig("subtitle", state="normal")
            self.fade_in_content()
    
    def fade_in_content(self):
        """Fade in the main content"""
        if self.content_alpha < 1:
            self.content_alpha += 0.05
            self.root.after(30, self.fade_in_content)
        else:
            # Show all elements
            self.canvas.itemconfig("welcome", state="normal")
            self.canvas.itemconfig("entry", state="normal")
            self.canvas.itemconfig("sort_btn", state="normal")
            self.canvas.itemconfig("music_btn", state="normal")
            self.pulse_glow_effect()
    
    def pulse_glow_effect(self):
        """Create pulsing glow effect around buttons"""
        self.glow_alpha += 0.05 * self.glow_direction
        
        if self.glow_alpha >= 1:
            self.glow_direction = -1
        elif self.glow_alpha <= 0:
            self.glow_direction = 1
        
        # Update button highlighting
        glow_intensity = int(139 + 50 * self.glow_alpha)
        try:
            self.sort_button.config(bg=f"#{glow_intensity:02x}0000")
        except:
            pass
        
        self.root.after(50, self.pulse_glow_effect)
    
    def show_mini_character(self):
        """Show animated mini character when typing name"""
        if not self.character_visible:
            self.character_visible = True
            
            # Create owl character elements
            # Owl body
            self.character_elements.append(
                self.canvas.create_text(
                    650, 420,
                    text="🦉",
                    font=("Helvetica", 48),
                    tags="mini_char"
                )
            )
            
            # Speech bubble
            bubble_frame = tk.Frame(self.canvas, bg="#FFD700", relief=tk.RIDGE, borderwidth=2)
            bubble_window = self.canvas.create_window(
                750, 400,
                window=bubble_frame,
                tags="mini_char"
            )
            self.character_elements.append(bubble_window)
            
            bubble_text = tk.Label(
                bubble_frame,
                text="  Nice to\n  meet you!  ",
                font=("Helvetica", 10, "italic"),
                fg="#000000",
                bg="#FFD700",
                justify=tk.LEFT
            )
            bubble_text.pack(padx=5, pady=3)
            
            # Star particles around character
            for i in range(5):
                angle = (i * 72) * (math.pi / 180)
                x = 650 + 40 * math.cos(angle)
                y = 420 + 40 * math.sin(angle)
                star = self.canvas.create_text(
                    x, y,
                    text="✨",
                    font=("Helvetica", 12),
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
                        self.canvas.coords(element, coords[0], 420 + self.character_y_offset if element == self.character_elements[0] else current_y)
                except:
                    pass
            
            self.root.after(30, self.animate_character_bounce)
    
    def character_react_to_typing(self):
        """Character reacts when user types"""
        if self.character_visible and len(self.character_elements) > 0:
            # Create sparkle effect when typing
            x = 650 + random.randint(-30, 30)
            y = 420 + random.randint(-30, 30)
            sparkle = self.canvas.create_text(
                x, y,
                text=random.choice(["✨", "⭐", "💫", "🌟"]),
                font=("Helvetica", 14),
                tags="sparkle"
            )
            
            # Fade out and remove sparkle
            self.fade_out_sparkle(sparkle, 0)
    
    def fade_out_sparkle(self, sparkle_id, step):
        """Fade out sparkle effect"""
        if step < 10:
            try:
                coords = self.canvas.coords(sparkle_id)
                if len(coords) >= 2:
                    # Move sparkle up
                    self.canvas.coords(sparkle_id, coords[0], coords[1] - 2)
                self.root.after(50, lambda: self.fade_out_sparkle(sparkle_id, step + 1))
            except:
                pass
        else:
            try:
                self.canvas.delete(sparkle_id)
            except:
                pass
    
    def on_button_hover(self, button, color):
        """Button hover effect with scale animation"""
        button.config(bg=color)
        # Add subtle scale effect
        current_font = button.cget("font")
    
    def on_button_leave(self, button, color):
        """Button leave effect"""
        button.config(bg=color)
    
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
        """Start the sorting process with animations"""
        name = self.name_entry.get().strip()
        if not name:
            name = "Student"
        
        # Disable button during sorting
        self.sort_button.config(state=tk.DISABLED)
        
        # Hide input elements with fade out
        self.canvas.itemconfig("welcome", state="hidden")
        self.canvas.itemconfig("entry", state="hidden")
        self.canvas.itemconfig("sort_btn", state="hidden")
        
        # Show thinking animation
        self.show_thinking_animation(name)
    
    def show_thinking_animation(self, name):
        """Display animated thinking process"""
        thinking_frame = tk.Frame(self.canvas, bg="#1a1a3e", padx=40, pady=30)
        thinking_window = self.canvas.create_window(450, 350, window=thinking_frame, tags="thinking")
        
        thinking_label = tk.Label(
            thinking_frame,
            text=f"🤔 Hmm... {name}...\nDifficult. Very difficult...\n\n✨ Analyzing your traits... ✨",
            font=("Helvetica", 16),
            fg="#FFD700",
            bg="#1a1a3e",
            justify=tk.CENTER
        )
        thinking_label.pack()
        
        # Animated dots
        self.animate_thinking_dots(thinking_label, 0, name)
    
    def animate_thinking_dots(self, label, count, name):
        """Animate thinking dots"""
        if count < 15:
            dots = "." * ((count % 3) + 1)
            label.config(text=f"🤔 Hmm... {name}...\nDifficult. Very difficult{dots}\n\n✨ Analyzing your traits... ✨")
            self.root.after(200, lambda: self.animate_thinking_dots(label, count + 1, name))
        else:
            # Remove thinking animation
            self.canvas.delete("thinking")
            # Show result with explosion animation
            self.show_result_with_animation(name)
    
    def show_result_with_animation(self, name):
        """Show sorting result with explosion animation"""
        # Randomly select house
        house = random.choice(houses)
        colors = self.house_colors[house]
        emoji = house_info[house]["emoji"]
        traits = house_info[house]["traits"]
        founder = house_info[house]["founder"]
        
        # Create explosion effect
        self.create_explosion_effect(colors["glow"])
        
        # Show result after explosion
        self.root.after(1000, lambda: self.display_final_result(name, house, colors, emoji, traits, founder))
    
    def create_explosion_effect(self, color):
        """Create particle explosion effect"""
        center_x, center_y = 450, 350
        explosion_particles = []
        
        for _ in range(50):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(5, 15)
            size = random.randint(5, 15)
            
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
                'life': 20
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
        """Display final sorting result with animation"""
        # Clear any existing result
        self.result_label.config(text="")
        
        # Configure result display
        result_text = f"🎉 CONGRATULATIONS, {name.upper()}! 🎉\n\n"
        result_text += f"You have been sorted into\n\n"
        result_text += f"{emoji} {house.upper()} {emoji}\n\n"
        result_text += f"{traits}\n"
        result_text += f"Founded by: {founder}"
        
        self.result_frame.config(bg=colors["primary"], relief=tk.RIDGE, borderwidth=5)
        self.result_label.config(
            text=result_text,
            bg=colors["primary"],
            fg="#FFFFFF"
        )
        
        # Show result with slide-in animation
        self.canvas.itemconfig("result", state="normal")
        self.canvas.itemconfig("restart_btn", state="normal")
        self.canvas.itemconfig("music_btn", state="normal")
        
        # Animate result sliding in
        self.slide_in_result(300, 350)
        
        # Re-enable button
        self.sort_button.config(state=tk.NORMAL)
    
    def slide_in_result(self, current_y, target_y):
        """Slide in result animation"""
        if current_y < target_y:
            current_y += 10
            self.canvas.coords(self.result_window, 450, current_y)
            self.root.after(20, lambda: self.slide_in_result(current_y, target_y))
    
    def restart(self):
        """Restart the sorting process with fade out animation"""
        # Hide result elements
        self.canvas.itemconfig("result", state="hidden")
        self.canvas.itemconfig("restart_btn", state="hidden")
        
        # Reset and show input elements
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, "Student")
        
        self.result_frame.config(bg="#0a0a1a", relief=tk.FLAT, borderwidth=0)
        self.result_label.config(text="", bg="#0a0a1a")
        
        # Fade in input elements
        self.canvas.itemconfig("welcome", state="normal")
        self.canvas.itemconfig("entry", state="normal")
        self.canvas.itemconfig("sort_btn", state="normal")
        self.canvas.itemconfig("music_btn", state="normal")

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