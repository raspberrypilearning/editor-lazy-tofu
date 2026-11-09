## End the game

Stop the game when Tofu runs out of health.

Click on the `Stage` and add a new `when I receive (start)`{:class="block3events"} script.

Use `wait until`{:class="block3control"} to wait for health to be less than `1`, then `stop all`{:class="block3control"}.

```blocks3
when I receive [start v]
wait until <(health) < (1)>
stop [all v]
```

This script starts after the Stage has reset health, so it checks the current game.

## Now run your code

Click the green flag and play until Tofu loses all three health points. Tofu, the plants, ripples and objects stop moving.

Click the green flag again. Score and health reset for a new game.
