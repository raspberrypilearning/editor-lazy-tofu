## Set up score and health

Set up score and health, then make objects disappear when **Tofu** touches them.

## Step 1

Click on the **Stage**.

Make two variables, `score`{:class="block3variables"} and `health`{:class="block3variables"}, both **For all sprites**.

## Step 2

In the green-flag script, add `set score to 0`{:class="block3variables"} and `set health to 3`{:class="block3variables"} before `broadcast (start)`{:class="block3events"}.

![Stage thumbnail](images/sprite-stage.png)

```blocks3
when green flag clicked
set [speed v] to (1)
+set [score v] to (0)
+set [health v] to (3)
broadcast (start v)
```

## Step 3

Click on the **objects** sprite and find the movement script.

Inside `repeat until`{:class="block3control"}, add an `if then`{:class="block3control"} block: if `touching (Tofu)`{:class="block3sensing"}, `delete this clone`{:class="block3control"}.

![objects sprite](images/sprite-objects.png)

```blocks3
when I start as a clone
switch costume to (pick random (1) to (6))
show
repeat until <(y position) > (180)>
change y by (speed)
+if <touching (Tofu v)?> then
delete this clone
end
end
delete this clone
```

## Now run your code

Click the green flag and swim into food and rubbish. Each clone disappears when it touches **Tofu**.
