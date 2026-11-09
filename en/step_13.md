## Choose the ripple costume

The ripple sprite has two costumes facing opposite ways. Choose one to match the side of the river where each clone appears.

Click on `water-ripples`{:class="block3looks"}.

In the clone script, replace the single costume block with an `if then else`{:class="block3control"} block.

If x is less than `0`, the clone is on the left: choose `water-ripples2`. Otherwise, choose `water-ripples`.

```blocks3
when I start as a clone
if <(x position) < (0)> then
switch costume to (water-ripples2 v)
else
switch costume to (water-ripples v)
end
show
repeat until <(y position) > (180)>
change y by (speed)
end
delete this clone
```

## Now run your code

Click the green flag. Watch ripples on both sides of the river: their costumes face opposite ways.
