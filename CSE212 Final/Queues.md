# Queues

## What are queues?
Queues are a way to store items. They can be implemented using lists, or through the `collections.dequeue` class. Using the class is recommended as it can handle more than using lists and allows more efficient processing.

Queues are basically the opposite of a stack. Stacks operate under a last in, first out (LIFO) principle, while queues are first in, first out (FIFO).

A good example is a pipe that transports basketballs. The new basketballs are put in at the end (enqueueing) and are only taken out at the front (dequeueing). You can't open the pipe and take out a basketball.
 

The following picture might help clarify this: 

![queueing picture](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/02/Queue.png)

## Queue use cases
Queues are great for any FIFO operation, such as people on a waitlist, or keeping track of orders.
 


## Performance

Different queue operations have different BigO notations. To borrow from the reading:

| Common Queue Operation | Description                                                                                | Python Code                                                                 | Performance                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| enqueue(value)         | Adds "value" to the back of the queue                                                      | `my_queue.append(value)`                                                    | O(1) - Performance of adding to the end of the dynamic array                         |
| dequeue()              | Two approaches: Remove and return the item from the front of the queue; or pop off index 0 | `value = my_queue[0]<br>del my_queue[0]`<br>or<br>`value = my_queue.pop(0)` | O(n) - Performance of obtaining and removing from the beginning of the dynamic array |
| size()                 | Return the size of the queue                                                               | `length = len(my_queue)`                                                    | O(1) - Performance of returning the size of the dynamic array                        |
| empty()                | Returns true if the length of the queue is zero.                                           | `if len(my_queue) == 0:`                                                    | O(1) - Performance of checking the size of the dynamic array                         |


## Examples
* enqueue
* dequeue
* popleft
* pop

``` Python
from collections import deque

# Create queue
# Print myQueue. Notice how it is empty
myQueue = deque([])
print( myQueue)

# Enqueueing
# Append 1 to the queue
# Print myQueue again. Notice how it has 1 appended (or enqueued) to it.
myQueue.append(1)
print(myQueue)

# You can append to the left side of the queue using .appendleft
myQueue.appendleft("left")
print(myQueue)

# Dequeueing
# We can use .popleft to remove that last item from the left side of the queue
myQueue.popleft()
print(myQueue)

# Add "right" to the queue
myQueue.append("right")
print(myQueue)

# Use pop to remove "right"
myQueue.pop()
print(myQueue)

```

See `queueExample.py` for examples. Feel free to play around with them!

 

## Problem
Doctor Who needs help keeping track of who's next in line. He keeps losing his printout and would like to have it digitally.
Create a queue that will store the names of any patient names supplied.

See [queueProblem.py](./queueProblem.py) if you get stuck.


## Jump to Section:

#### [Welcome](./Welcome.md)

#### Queues
* [Queues](./Queues.md)
* [Queue Examples](./queueExample.py)
* [Queue  Problems](./queueProblem.py)

#### Sets
* [Sets](./Sets.md)
* [Set Examples](./setExample.py)
* [Set  Problems](./setProblem.py)

#### Trees
* [Trees](./Trees.md)
* [Tree Examples](./treeExample.py)
* [Tree Problems](./treeProblem.py)