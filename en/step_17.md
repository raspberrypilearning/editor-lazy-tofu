## Set up score and health

Tofu will earn points for food and lose health after collisions.

Click on the `Stage`. Make two variables, `score`{:class="block3variables"} and `health`{:class="block3variables"}, both **For all sprites**.

Tick both checkboxes so the player can see them. You can drag their displays to clear spaces at the top of the Stage.

In the Stage's green-flag script, set score to `0` and health to `3`, before sending `start`.

```blocks3
when green flag clicked
set [speed v] to (1)
set [score v] to (0)
set [health v] to (3)
broadcast (start v)
```

Setting the variables before the broadcast means all the game scripts begin with the new values.

## Now run your code

Click the green flag. Score starts at `0` and health starts at `3`. Next, you'll make food change the score.
