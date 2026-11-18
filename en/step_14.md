## Float food and rubbish

Give Tofu some things to find in the river.

## Step 1

Copy all three scripts from `water-ripples`{:class="block3looks"} to `objects`{:class="block3looks"}.

## Step 2

In the clone movement script, remove the whole `if then else`{:class="block3control"} block that chooses ripple costumes.

Replace it with a `switch costume to ()`{:class="block3looks"} block containing `pick random (1) to (6)`{:class="block3operators"}.

![objects sprite](images/sprite-objects.png)

```blocks3
when I start as a clone
+switch costume to (pick random (1) to (6))
show
repeat until <(y position) > (180)>
change y by (speed)
end
delete this clone
```

## Step 3

In the size-changing script, change the size amounts to `2`{:class="block3looks"} and `-2`{:class="block3looks"}.

![objects sprite](images/sprite-objects.png)

```blocks3
when I start as a clone
forever
+change size by (2)
wait (0.1) seconds
+change size by (-2)
wait (0.1) seconds
end
```

## Now run your code

Click the green flag. Food and rubbish bob as they float through the river. They don't affect Tofu yet.
