from flask import Response, json

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
        games = range(n).__iter__()

        yield '['

        try:
            game = next(games)
            result = monty_hall_game.game(game)
            yield json.dumps(result)
        except StopIteration:
            # no results – close array and stop iteration
            yield ']'
            raise StopIteration

        # loop over remaining results
        for gg in games:
            result = monty_hall_game.game(gg)
            yield ", " + json.dumps(result)

        # close array
        yield "]"

    return Response(generate(), content_type="application/json")


if __name__ == "__main__":
    app.run()
