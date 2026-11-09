## Crash into a tree

Make the trees into obstacles. A collision will send Tofu back to the middle and cost one health.

Click on `Tofu`{:class="block3looks"} and add a new script for the `start` message.

Inside a forever loop, check whether Tofu is touching `tree-left`. If so, start the `Scream1` sound, go to the middle of the river and change health by `-1`.

```blocks3
when I receive [start v]
forever
if <touching (tree-left v)?> then
start sound (Scream1 v)
go to x: (0) y: (0)
change [health v] by (-1)
end
end
```

Checking whether Tofu touches the sprite also checks its clones, so one condition covers every left-bank tree.

## Now run your code

Click the green flag and steer into a tree on the left. Tofu returns to the middle and loses one health.
