from game import monty_hall_game
from service import app
from service.decorator import validate_parameter
from flask import jsonify
from flask import stream_with_context, Response


# home route just returns a description of our API
@app.route("/")
def home():
    return "Monty Hall problem simulations with random switch and without after the initial reveal of the first door"


# API call for running simulations, where n is the number of simulated games
@validate_parameter
@app.route("/monty_hall_simulations/<int:n>", methods=['GET'])
@return_json
def simulation(n):
    @stream_with_context
    def generate():
        for i in range(1, n):
            game_result = monty_hall_game.game(i)
            yield jsonify(game_result)

    return Response(generate())


if __name__ == "__main__":
    app.run()
