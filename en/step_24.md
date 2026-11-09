## Make sleeping Tofu breathe

Make Tofu grow and shrink gently while waiting to wake up.

On `Tofu`{:class="block3looks"}, replace the opening script's `wait until`{:class="block3control"} with a `repeat until`{:class="block3control"} loop, keeping the condition `awake = 1`.

Inside it, add two repeat loops. The first grows Tofu a little ten times; the second shrinks Tofu by the same amount.

```blocks3
repeat until <(awake) = (1)>
repeat (10)
wait (0.04) seconds
change size by (1)
end
repeat (10)
wait (0.04) seconds
change size by (-1)
end
end
```

Keep the `go to x: (0) y: (0)`{:class="block3motion"} and `broadcast (start)`{:class="block3events"} blocks after the outer loop.

The size goes up by ten and down by ten during each breath. The separate key-press script remembers a quick press, so Tofu can finish the current breath before waking. You don't need to hold the key down.

## Now run your code

Click the green flag. Tofu breathes while sleeping. Press space to finish the current breath and start swimming.
