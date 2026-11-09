## Set the river speed

Tofu will stay near the middle of the screen while trees and other objects move past. A shared variable will keep their movement at the same speed.

## Step 1

Click on the `Stage` and create a variable called `speed`{:class="block3variables"}, **For all sprites**. Untick its checkbox for now.

Set it to `1` when the green flag is clicked.

Then make a new message called `start` in a `broadcast ()`{:class="block3events"} block and send it after setting the speed.

```blocks3
when green flag clicked
set [speed v] to (1)
broadcast (start v)
```

## Step 2

Click on `Tofu`{:class="block3looks"}. At the top of the movement loop, replace `when green flag clicked`{:class="block3events"} with `when I receive (start)`{:class="block3events"}.

Keep Tofu's separate starting-position script on the green flag.

```blocks3
when I receive [start v]
```

The Stage sets up the speed first, then tells the game to start. Later, Tofu will send this same message after jumping into the water.

## Now run your code

Click the green flag. Tofu should still move with the arrow keys. The river scenery will use the same `start` message next.
