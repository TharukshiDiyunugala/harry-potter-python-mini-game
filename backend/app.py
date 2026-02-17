"""
Flask Backend for Harry Potter Sorting Hat Game
Provides REST API for Vue.js frontend
"""
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import random

app = Flask(__name__, static_folder='../frontend/dist')
CORS(app)  # Enable CORS for Vue.js frontend

# Game data
HOUSES = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

HOUSE_INFO = {
    "Gryffindor": {
        "traits": "Brave, daring, and chivalrous!",
        "color": "#740001",
        "secondaryColor": "#D3A625",
        "glowColor": "#FFCC00",
        "emoji": "🦁",
        "founder": "Godric Gryffindor",
        "description": "Their daring, nerve, and chivalry set Gryffindors apart"
    },
    "Hufflepuff": {
        "traits": "Loyal, patient, and hardworking!",
        "color": "#FFDB00",
        "secondaryColor": "#000000",
        "glowColor": "#FFE55C",
        "emoji": "🦡",
        "founder": "Helga Hufflepuff",
        "description": "Those patient Hufflepuffs are true and unafraid of toil"
    },
    "Ravenclaw": {
        "traits": "Wise, witty, and clever!",
        "color": "#0E1A40",
        "secondaryColor": "#946B2D",
        "glowColor": "#5DADE2",
        "emoji": "🦅",
        "founder": "Rowena Ravenclaw",
        "description": "Where those of wit and learning will always find their kind"
    },
    "Slytherin": {
        "traits": "Ambitious, cunning, and resourceful!",
        "color": "#1A472A",
        "secondaryColor": "#5D5D5D",
        "glowColor": "#5DBE71",
        "emoji": "🐍",
        "founder": "Salazar Slytherin",
        "description": "Those cunning folk use any means to achieve their ends"
    }
}


@app.route('/api/houses', methods=['GET'])
def get_houses():
    """Get all house information"""
    return jsonify({
        'success': True,
        'houses': HOUSE_INFO
    })


@app.route('/api/sort', methods=['POST'])
def sort_student():
    """Sort a student into a house"""
    data = request.get_json()
    name = data.get('name', 'Student')
    
    # Randomly select a house
    selected_house = random.choice(HOUSES)
    house_data = HOUSE_INFO[selected_house]
    
    return jsonify({
        'success': True,
        'name': name,
        'house': selected_house,
        'houseInfo': house_data
    })


@app.route('/api/maze/generate', methods=['GET'])
def generate_maze():
    """Generate a random maze"""
    size = int(request.args.get('size', 15))
    maze = _generate_maze_data(size)
    
    return jsonify({
        'success': True,
        'maze': maze,
        'size': size,
        'start': [1, 1],
        'end': [size - 2, size - 2]
    })


def _generate_maze_data(size):
    """Generate maze using recursive backtracking"""
    import random
    import time
    
    random.seed(time.time())
    maze = [[1 for _ in range(size)] for _ in range(size)]
    
    start_x, start_y = 1, 1
    maze[start_y][start_x] = 0
    stack = [(start_x, start_y)]
    
    while stack:
        x, y = stack[-1]
        neighbors = []
        
        for dx, dy in [(0, -2), (0, 2), (-2, 0), (2, 0)]:
            nx, ny = x + dx, y + dy
            if 1 <= nx < size - 1 and 1 <= ny < size - 1 and maze[ny][nx] == 1:
                neighbors.append((nx, ny, dx, dy))
        
        if neighbors:
            nx, ny, dx, dy = random.choice(neighbors)
            maze[y + dy // 2][x + dx // 2] = 0
            maze[ny][nx] = 0
            stack.append((nx, ny))
        else:
            stack.pop()
    
    maze[1][1] = 0
    maze[size - 2][size - 2] = 0
    
    return maze


# Serve Vue.js frontend
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    """Serve Vue.js app"""
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    print("🎩 Starting Hogwarts Sorting Hat Backend...")
    print("🌐 Backend running at: http://localhost:5000")
    print("🎨 Make sure to build Vue.js frontend first!")
    app.run(debug=True, port=5000)
