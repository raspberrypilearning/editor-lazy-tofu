## Waddle towards the river

Make Tofu waddle down the bank before jumping in.

On `Tofu`{:class="block3looks"}, add these blocks after the wave sequence, before the final position change.

Switch to `tofu-running` and set the rotation style to `all around` so Tofu can lean from side to side.

Repeat a pair of steps three times: move down, lean left, wait, then move down, lean right and wait again.

```blocks3
switch costume to (tofu-running v)
set rotation style [all around v]
repeat (3)
change y by (-10)
turn ccw (15) degrees
wait (0.2) seconds
change y by (-10)
turn cw (15) degrees
wait (0.2) seconds
end
```

The two turns balance each other, just as the two size changes did in the breathing animation.

## Now run your code

Click the green flag and press space. Tofu waves, waddles down the bank, then appears in the river to begin swimming.
