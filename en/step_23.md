## Let Tofu sleep

The game works. Now give Tofu a nap on the bank before the swimming begins.

The `start` message already starts the movement, scenery and collision checks. You'll have Tofu send it after waking, instead of the Stage sending it straight away.

## Step 1

Click on the `Stage`. Remove `broadcast (start)`{:class="block3events"} from its green-flag script. Keep the three variable resets.

```blocks3
when green flag clicked
set [speed v] to (1)
set [score v] to (0)
set [health v] to (3)
```

## Step 2

Click on `Tofu`{:class="block3looks"}. Make a variable called `awake`{:class="block3variables"}, **For this sprite only**, and untick its checkbox.

Use `0` for asleep and `1` for awake. Add a separate key-press script to remember when the player presses space:

```blocks3
when [space v] key pressed
set [awake v] to (1)
```

Find Tofu's green-flag starting-position script.

Change the position to `x: -197, y: 107` and the costume to `tofu-sleeping`.

Set `awake`{:class="block3variables"} to `0` at the start. At the end, wait until `awake`{:class="block3variables"} is `1`, go to `0, 0`, then broadcast `start`.

```blocks3
when green flag clicked
go to x: (-197) y: (107)
set size to (23) %
point in direction (90)
set rotation style [left-right v]
show
set [awake v] to (0)
switch costume to (tofu-sleeping v)
wait until <(awake) = (1)>
go to x: (0) y: (0)
broadcast (start v)
```

Keep both of Tofu's existing `when I receive (start)`{:class="block3events"} scripts. The game will use them once Tofu is in the river.

## Now run your code

Click the green flag. Tofu sleeps on the left bank and the river stays still.

Press the space bar. Tofu appears in the middle and the game begins.
