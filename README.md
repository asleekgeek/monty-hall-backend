# Monty Hall n simulation Python Flask API

Backend API runs n simulations of the Monty Hall paradox, with random switching of choices.

The API endpoint is implemented in a way that simulates a very long running operation, using yield to return a iterable
subset of the processed simulation so that the frontend can react and show the progress of the operation.

## How to run

There is a Dockerfile included so you can run in from a container.

## Monty Hall problem

The Monty Hall is a brain-teaser, in the form of a probability puzzle, loosely based on the American television game
show Let's Make a Deal and named after its original host, Monty Hall.

The concept of the game is that the player sees three closed doors - behind one is a car, and behind the other two are
goats. The game starts with the player getting to choose a door, without opening it. Then the presenter opens one of the
two remaining doors (but never the one with the car) and shows that this door does not contain profit. The player is
then given another choice to change the door. The question is whether the chances of winning increase if the player
changes the door.

Source: https://en.wikipedia.org/wiki/Monty_Hall_problem

