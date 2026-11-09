## Make sleeping Tofu breathe

Make Tofu grow and shrink gently for four breaths before waiting to wake up.

On `Tofu`{:class="block3looks"}, add a `repeat (4)`{:class="block3control"} loop immediately before the opening script's `wait until`{:class="block3control"} block.

Inside it, add two repeat loops. The first grows Tofu a little ten times; the second shrinks Tofu by the same amount.

```blocks3
repeat (4)
repeat (10)
wait (0.04) seconds
change size by (1)
end
repeat (10)
wait (0.04) seconds
change size by (-1)
end
end
wait until <key (space v) pressed?>
```

Keep `wait until <key (space) pressed?>`{:class="block3control"} **outside and after** the outer loop. The `go to x: (0) y: (0)`{:class="block3motion"} and `broadcast (start)`{:class="block3events"} blocks stay after the wait.

The size goes up by ten and down by ten during each breath. Tofu finishes all four breaths, then waits for the player to press space.

## Now run your code

Click the green flag. Watch Tofu take four breaths, then press space to start swimming.
