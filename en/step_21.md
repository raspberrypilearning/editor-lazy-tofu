## Make sleeping Tofu breathe

Make Tofu grow and shrink gently for four breaths before waiting to wake up.

## Step 1

Add a `repeat (4)`{:class="block3control"} loop immediately before the opening script's `wait until`{:class="block3control"} block.

Inside it, add `start sound (Snoring)`{:class="block3sound"}.

![Tofu sprite](images/sprite-tofu.png)

```blocks3
when green flag clicked
go to x: (-197) y: (107)
set size to (23) %
point in direction (90)
set rotation style [left-right v]
show
switch costume to (tofu-sleeping v)
+repeat (4)
start sound (Snoring v)
end
wait until <key (space v) pressed?>
go to x: (0) y: (0)
broadcast (start v)
```

## Step 2

Inside `repeat (4)`{:class="block3control"}, after `start sound (Snoring)`{:class="block3sound"}, add two `repeat (10)`{:class="block3control"} loops to grow and shrink Tofu.

![Tofu sprite](images/sprite-tofu.png)

```blocks3
repeat (4)
start sound (Snoring v)
+repeat (10)
wait (0.04) seconds
change size by (1)
end
+repeat (10)
wait (0.04) seconds
change size by (-1)
end
end
```

## Now run your code

Click the green flag. Tofu snores and takes four breaths, then waits for space to start swimming.
