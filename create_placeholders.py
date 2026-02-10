"""Create placeholder images for testing the animated background"""
from PIL import Image, ImageDraw
import os
import random

# Create assets folder if it doesn't exist
os.makedirs('assets', exist_ok=True)

# Create Hogwarts background (dark castle scene with stars)
print("Creating hogwarts_bg.jpg...")
bg = Image.new('RGB', (1200, 800), color=(10, 15, 30))
draw = ImageDraw.Draw(bg)

# Add stars
for _ in range(150):
    x = random.randint(0, 1200)
    y = random.randint(0, 400)
    size = random.randint(1, 3)
    brightness = random.randint(200, 255)
    draw.ellipse([x, y, x+size, y+size], fill=(brightness, brightness, brightness))

# Draw simple castle silhouette
# Main castle body
castle_points = [
    (400, 500), (400, 350), (450, 350), (450, 400),
    (500, 350), (500, 400), (550, 350), (550, 500),
    (600, 500), (600, 300), (650, 300), (650, 500),
    (700, 500), (700, 350), (750, 350), (750, 400),
    (800, 350), (800, 500)
]
draw.polygon(castle_points, fill=(30, 30, 50))

# Add moon
draw.ellipse([950, 100, 1050, 200], fill=(220, 220, 180))

bg.save('assets/hogwarts_bg.jpg')
print("✅ Created hogwarts_bg.jpg")

# Create flying witch silhouette
print("Creating witch1.png...")
witch = Image.new('RGBA', (100, 100), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(witch)

# Witch body (black silhouette)
# Broomstick
draw.line([(10, 60), (90, 60)], fill=(50, 30, 10), width=3)
# Bristles
for i in range(10, 30, 4):
    draw.line([(80, 55), (90, 50+i)], fill=(60, 40, 10), width=2)

# Witch figure
# Head
draw.ellipse([35, 30, 50, 45], fill=(0, 0, 0))
# Hat
draw.polygon([(30, 30), (55, 30), (45, 10)], fill=(0, 0, 0))
# Body
draw.polygon([(35, 45), (50, 45), (55, 65), (30, 65)], fill=(0, 0, 0))
# Cloak flowing behind
draw.polygon([(30, 50), (20, 45), (15, 60), (25, 65)], fill=(0, 0, 0))

witch.save('assets/witch1.png')
print("✅ Created witch1.png")

print("\n🎉 All placeholder assets created successfully!")
print("You can now run the game to see the animated background!")
