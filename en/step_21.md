## Check both banks

The right-bank trees need the same collision response.

On `Tofu`{:class="block3looks"}, use an `or`{:class="block3operators"} block to join two touching checks: one for `tree-left` and one for `tree-right`.

```blocks3
when I receive [start v]
forever
if <<touching (tree-left v)?> or <touching (tree-right v)?>> then
start sound (Scream1 v)
go to x: (0) y: (0)
change [health v] by (-1)
end
end
```

An `or` condition is true when either check is true, so you can share the response code.

## Now run your code

Click the green flag and try a tree on each bank. Both should send Tofu to the middle and take away one health.
