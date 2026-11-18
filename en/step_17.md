## Crash into a tree

Make the trees into obstacles. A collision will send **Tofu** back to the middle and cost one health.

## Step 1

Add a new script for the `start`{:class="block3events"} message.

Inside a `forever`{:class="block3control"} loop, check `touching (tree-left)`{:class="block3sensing"}. If so, `start sound (Scream1)`{:class="block3sound"}, `go to x: (0) y: (0)`{:class="block3motion"} and `change health by (-1)`{:class="block3variables"}.

![Tofu sprite](images/sprite-tofu.png)

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

Click the green flag and steer into a tree on the left. **Tofu** returns to the middle and loses one health.

## Step 2

The right-bank trees need the same collision response.

Use an `or`{:class="block3operators"} block to join two touching checks: one for `touching (tree-left)`{:class="block3sensing"} and one for `touching (tree-right)`{:class="block3sensing"}.

![Tofu sprite](images/sprite-tofu.png)

```blocks3
when I receive [start v]
forever
if <<touching (tree-left v)?> or <touching (tree-right v)?> :: +> then
start sound (Scream1 v)
go to x: (0) y: (0)
change [health v] by (-1)
end
end
```

An `or`{:class="block3operators"} condition is true when either check is true, so you can share the response code.

## Now run your code

Click the green flag and try a tree on each bank. Both should send **Tofu** to the middle and take away one health.
