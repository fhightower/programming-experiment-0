## Initialization

To start, run:

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

