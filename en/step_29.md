## Make a splash

Finish the opening with a splash as Tofu lands in the water.

On `Tofu`{:class="block3looks"}, add `start sound (Splash)`{:class="block3sound"}, switch to the `splash` costume, then wait `1` second.

Place these blocks after the last glide and before the `start` broadcast.

```blocks3
glide (0.2) secs to x: (0) y: (0)
start sound (Splash v)
switch costume to (splash v)
wait (1) seconds
broadcast (start v)
```

The movement script chooses Tofu's next costume once it receives `start`.

## Now run your code

Click the green flag and watch the full opening. After Tofu's four breaths, press space to wake up. Wait for the splash to finish before swimming for food.

Try restarting during the animation too. Tofu should return to the sleeping position and size.
