## Collect food

Make each food clone check whether Tofu has reached it.

Click on `objects`{:class="block3looks"} and find its movement script.

Inside `repeat until`{:class="block3control"}, after the y change, add an `if then`{:class="block3control"} block that checks `touching (Tofu)`{:class="block3sensing"}.

Inside that, add another `if then`{:class="block3control"} block. Check whether `costume number`{:class="block3looks"} is less than `4`.

The first three costumes are food. When one touches Tofu, add `5` to the score, start the `Chomp` sound and delete the clone.

```blocks3
when I start as a clone
switch costume to (pick random (1) to (6))
show
repeat until <(y position) > (180)>
change y by (speed)
if <touching (Tofu v)?> then
if <(costume [number v]) < (4)> then
change [score v] by (5)
start sound (Chomp v)
delete this clone
end
end
end
delete this clone
```

Keep the last `delete this clone`{:class="block3control"} block outside the loop: it still removes objects that reach the top without being collected.

## Now run your code

Click the green flag and swim into a shrimp, snail or worm. The food disappears and your score goes up by `5`.

Rubbish still floats past for now; you'll make it cost health next.
