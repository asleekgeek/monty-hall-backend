import unittest
import service.monty_hall_simulations_api


class TestMontyHallService(unittest.TestCase):
    def test_monty_hall_simulations_of_5(self):
        self.assertIsNotNone(service.monty_hall_simulations_api.simulation(1))

    def test_monty_hall_simulations_of_negative(self):
        self.failureException(service.monty_hall_simulations_api.simulation(-1))


if __name__ == '__main__':
    unittest.main()
