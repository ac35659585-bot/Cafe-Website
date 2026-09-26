from flask import Flask, render_template, request

app = Flask(__name__)

# Sample Nearby Cafes Data
CAFES = [
    {
        "id": 1,
        "name": "Brew & Bite Cafe",
        "location": "Downtown, City Center",
        "rating": "4.5 ★",
        "image": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=500"
    },
    {
        "id": 2,
        "name": "The Coffee Bean & Bistro",
        "location": "Green Park, Main Market",
        "rating": "4.7 ★",
        "image": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=500"
    },
    {
        "id": 3,
        "name": "Urban Grind Roastery",
        "location": "Cyber Hub, Block B",
        "rating": "4.6 ★",
        "image": "https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=500"
    }
]

# Home Page - Subhi Cafes ki list dikhane ke liye
@app.route('/')
def home():
    return render_template('index.html', cafes=CAFES)

# Menu Page Route
@app.route('/menu')
def menu():
    return render_template('menu.html')

# Booking Page Route (With Cafe Selection)
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    selected_cafe = request.args.get('cafe', '')
    return render_template('booking.html', cafes=CAFES, selected_cafe=selected_cafe)

if __name__ == '__main__':
    app.run(debug=True)