## Jump into the water

Replace the instant move into the river with a short jump.

On `Tofu`{:class="block3looks"}, find the `go to x: (0) y: (0)`{:class="block3motion"} block at the end of the opening script. Replace that block with this sequence.

Switch to `tofu-jumping`, return to `left-right` rotation, then glide through three positions to reach the middle of the river.

```blocks3
switch costume to (tofu-jumping v)
set rotation style [left-right v]
glide (0.2) secs to x: (-149) y: (82)
glide (0.2) secs to x: (-62) y: (69)
glide (0.2) secs to x: (0) y: (0)
```

Keep `broadcast (start)`{:class="block3events"} after the final glide. Tofu must reach the water before the game starts.

## Now run your code

Click the green flag and press space. Tofu wakes, waves, waddles and jumps into the river. The arrow keys work once the jump finishes.
