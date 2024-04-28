from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/sharkwords")
def show_game_page():
    """Show the game's page."""

    return render_template("sharkwords.html")







if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")