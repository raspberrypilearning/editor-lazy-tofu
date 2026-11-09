## Wake up and wave

Let Tofu pause and wave before getting into the water.

On `Tofu`{:class="block3looks"}, add these blocks **after** `wait until <key (space) pressed?>`{:class="block3control"} and **before** `go to x: (0) y: (0)`{:class="block3motion"}.

Switch to `tofu`, wait a second, then start `Magic Spell` and switch to the waving costume. After half a second, return to `tofu` and wait another half a second.

```blocks3
switch costume to (tofu v)
wait (1) seconds
start sound (Magic Spell v)
switch costume to (tofu-waving v)
wait (0.5) seconds
switch costume to (tofu v)
wait (0.5) seconds
```

Keep the position change and `broadcast (start)`{:class="block3events"} at the end. You'll replace the position change with a jump shortly.

## Now run your code

Click the green flag, wait for the four breaths, then press space. Tofu wakes up, waves, then starts the game.
