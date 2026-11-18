## Jump into the water

Replace the instant move into the river with a short jump.

## Step 1

Find the `go to x: (0) y: (0)`{:class="block3motion"} block at the end of the opening script. Replace that block with this sequence.

Add `switch costume to (tofu-jumping)`{:class="block3looks"} and the three `glide`{:class="block3motion"} blocks shown below.

![Tofu sprite](images/sprite-tofu.png)

```blocks3
repeat (3)
change y by (-10)
turn ccw (15) degrees
wait (0.2) seconds
change y by (-10)
turn cw (15) degrees
wait (0.2) seconds
end
set rotation style [left-right v]
+switch costume to (tofu-jumping v)
+glide (0.2) secs to x: (-149) y: (82)
+glide (0.2) secs to x: (-62) y: (69)
+glide (0.2) secs to x: (0) y: (0)
broadcast (start v)
```

## Step 2

After the last `glide`{:class="block3motion"} and before `broadcast (start)`{:class="block3events"}, add `start sound (Splash)`{:class="block3sound"}, `switch costume to (splash)`{:class="block3looks"} and `wait (1) seconds`{:class="block3control"}.

![Tofu sprite](images/sprite-tofu.png)

```blocks3
glide (0.2) secs to x: (0) y: (0)
+start sound (Splash v)
+switch costume to (splash v)
+wait (1) seconds
broadcast (start v)
```

## Now run your code

Click the green flag, wait for the four breaths, then press space. **Tofu** wakes, waves, waddles, jumps and splashes. Try the arrow keys once the splash finishes.

Restart during the animation too. **Tofu** should return to the sleeping position and size.
