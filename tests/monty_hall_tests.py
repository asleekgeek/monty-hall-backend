import unittest

from werkzeug.exceptions import NotAcceptable

import service.decorator
import service.monty_hall_simulations_api


class TestMontyHallService(unittest.TestCase):
    def test_monty_hall_simulations_of_5(self):
        self.assertIsNotNone(service.monty_hall_simulations_api.simulation(5))

    def test_monty_hall_simulations_of_negative(self):
        self.addTypeEqualityFunc(service.monty_hall_simulations_api.simulation(-1), NotAcceptable)


if __name__ == '__main__':
    unittest.main()
