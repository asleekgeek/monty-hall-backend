from flask import jsonify, Response

from game import monty_hall_game
from service import app
from service.decorator import validate_parameter


# home route just returns a description of our API
@app.route("/")
def home():
    return 'Monty Hall problem simulations with random switch and without after the initial reveal of the first door'


# API call for running simulations, where n is the number of simulated games
@validate_parameter
@app.route('/monty_hall_simulations/<int:n>', methods=['GET'])
def simulation(n):
    def generate():
        for i in range(1, n):
            game_result = monty_hall_game.game(i)
            # there is a possibility to group the simulated games in chunks here
            # now the API method is only yielding back the simulated games one by one
            yield game_result

    return Response(jsonify(generate(),
                            message="",
                            category="success",
                            status=200
                            ))


if __name__ == "__main__":
    app.run()
