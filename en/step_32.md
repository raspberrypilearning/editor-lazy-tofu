## Choose your river speed

Give the player a slider to change how fast the river passes.

Click on the `Stage` and tick the checkbox beside `speed`{:class="block3variables"} to show it.

Right-click its display on the Stage and choose **slider**. Right-click it again and choose **change slider range**. Set the minimum to `1` and the maximum to `20`.

Keep the minimum above zero: your clone generators divide their waits by speed, so zero would not give them a usable interval.

Drag the display to a clear space at the top of the Stage.

## Now run your code

Click the green flag and wake Tofu. Start at speed `1`, then move the slider up a little.

The plants, ripples and objects all move faster. Their generators make clones more often too, because their waits are divided by the same speed.

Try to collect food without losing all your health. Clicking the green flag returns the speed to `1` for a new game.
