## Grow trees on the right bank

The other bank needs the same tree behaviour. Reuse the code you've made.

## Step 1

Click on `tree-left`{:class="block3looks"}. Drag each of its **two complete scripts**, by its top block, onto the existing `tree-right`{:class="block3looks"} sprite in the sprite list. This copies the scripts across.

Click on `tree-right`{:class="block3looks"} to see its copies. The right-hand sprite already has the overhanging-tree artwork facing into the river.

## Step 2

In its `go to x: () y: ()`{:class="block3motion"} block, change x from `-180` to `180`.

Negative x positions are on the left of the Stage; positive x positions are on the right. Keep y at `-200`, because trees on both banks enter at the same height.

The start of the right-hand script should now be:

```blocks3
when I receive [start v]
hide
go to x: (180) y: (-200)
```

Leave the clone script and the rest of the generator unchanged.

## Now run your code

Click the green flag. Trees should travel along both banks, leaving the river clear between them.
