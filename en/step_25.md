## Add snoring

Give sleeping Tofu a sound to go with the breathing.

On `Tofu`{:class="block3looks"}, add `start sound (Snoring)`{:class="block3sound"} at the beginning of the outer `repeat (4)`{:class="block3control"} loop, before the two breathing loops.

```blocks3
repeat (4)
start sound (Snoring v)
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

Use `start sound`{:class="block3sound"} so the breathing animation can continue while the sound plays.

## Now run your code

Click the green flag. Tofu snores and breathes four times, then waits on the bank. Press space after the four breaths to wake up and play.
