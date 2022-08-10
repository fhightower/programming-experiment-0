# Programming Experiment

## Background

I was reading [Clean Architecture](https://www.goodreads.com/book/show/18043011-clean-architecture) in which Robert C. Martin, the author, shows a graph of an experiment done where someone
takes on the same programming challenge consecutively using different approaches (specifically test-driven development (TDD) and a 'just do it' (JDI) approach) to see which one works best.

In the book, the point is that test-driven development is consistently faster than a 'just-do-it' approach.

I wanted to perform the same experiment and see what happened...

## My Experiment

So, I conducted an experiment where I took on the same problem every two days and timed myself.

The problem I solved was this:

```python
# The goal is to create a mine-sweeper board with the given number of cols, rows, and mines
# The board should use "x" for mines and each square should contain the number of adjacent mines
# (consider squares in both cardinal and ordinal directions)

# For example, a 3x3 board with 3 mines should look something like:
# 1 2 2
# 1 x x
# 1 3 x
```

## Results

I did this four times with the following results:

| Iteration    | Approach     | Time (minutes) |
|--------------|-----------|------------|
| 1 | 'Just-Do-It' | 40.6 |
| 2 | Test-Driven Development | 36.0  |
| 3 | TDD | 26.7 |
| 4 | JDI | 18.4 |

## Analysis

Predictably, I got much faster over time as I got used to the problem and its nuances.

From my experiment, TDD was not faster than the JDI approach. The last iteration (using a JDI approach) was the fastest.

This indicates to me that the problem may have been too simple for TDD to have a positive impact or that I didn't do enough iterations to see a benefit
(perhaps another TDD iteration would be faster still?).

### Caveats

There are a few caveats to this experiment worth noting:

1. I am a new parent and have very variable sleep right now with a newborn at home
	- I suspect that quality of sleep may have more to do with the time it takes to complete this problem than the approach used :)
1. I chose a relatively simple problem so it was easy to 'carry-over' knowledge from one iteration to another
    - Perhaps a more complex problem or a greater spacing between iterations would have reduced the amount of 'carry-over' between iterations

## Future Experiments

A few ideas for future, similar experiments:

1. Space out the different iterations more so it is harder to 'carry-over' knowledge from one iteration to another
	- I spaced mine out every two days, but that wasn't enough... I think spacing of a week or two would be better
1. Use different problems
	- I may pick two problems and do an iteration on each problem with a diff. approach
1. Try TDD first on a different problem
	- I tried a JDI approach first, but would like to choose a different problem and try the TDD approach first
1. Track the quality of sleep and the time it takes to complete a programming problem

All in all, a future experiment would:

- Space out iterations more
- Have two different problems

This schedule would look something like:

- Week 1: Problem 1, Approach: TDD
- Week 2: Problem 2, Approach: JDI
- Week 3: Problem 1, Approach: JDI
- Week 4: Problem 2, Approach: TDD

## Usage

To start, run:

```
docker-compose run -rm dev
```

This will drop you into ipython in docker. Then, you can run:

```
# move into the directory for the game your testing...
!cd 1/
```

And then start the timer:

```
import time

start = time.time()
```

Now you can run the game using:

```
run game.py
```

To stop, run:

```
end = time.time()
total_minutes = (end - start) / 60
```

