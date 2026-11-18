## Wake up and wave

Let **Tofu** pause and wave before getting into the water.

Add these blocks **after** `wait until <key (space) pressed?>`{:class="block3control"} and **before** `go to x: (0) y: (0)`{:class="block3motion"}.

![Tofu sprite](images/sprite-tofu.png)

```blocks3
wait until <key (space v) pressed?>
+switch costume to (tofu v)
+wait (1) seconds
+start sound (Magic Spell v)
+switch costume to (tofu-waving v)
+wait (0.5) seconds
+switch costume to (tofu v)
+wait (0.5) seconds
go to x: (0) y: (0)
```

## Now run your code

Click the green flag, wait for the four breaths, then press space. **Tofu** wakes up, waves, then starts the game.
