# Queues

## What are queues?
Queues are a way to store items. They can be implemented using lists, or through the `collections.dequeue` class. Using the class is recommended as it can handle more than using lists.

Queues are basically the opposite of a stack. Stacks operate under a last in, first out (LIFO) principle, while queues are first in, first out (FIFO).

A good example is a pipe that transports basketballs. The new basketballs are put in at the end (enqueueing) and are only taken out at the front (dequeueing). You can't open the pipe and take out a basketball.
<br />

The following picture maight help clarify this:

![queueing picture](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/02/Queue.png)

## Queue use cases
Queues are great for any FIFO operation, such as people on a waitlist, or keeping track of orders.
<br />


## Performance

Different queue operations have different BigO notations. To borrow from the reading:

| Common Queue Operation | Description                                                                                | Python Code                                                                 | Performance                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
|  |
| enqueue(value)         | Adds "value" to the back of the queue                                                      | `my_queue.append(value)`                                                    | O(1) - Performance of adding to the end of the dynamic array                         |
| dequeue()              | Two approaches: Remove and return the item from the front of the queue; or pop off index 0 | `value = my_queue[0]<br>del my_queue[0]`<br>or<br>`value = my_queue.pop(0)` | O(n) - Performance of obtaining and removing from the beginning of the dynamic array |
| size()                 | Return the size of the queue                                                               | `length = len(my_queue)`                                                    | O(1) - Performance of returning the size of the dynamic array                        |
| empty()                | Returns true if the length of the queue is zero.                                           | `if len(my_queue) == 0:`                                                    | O(1) - Performance of checking the size of the dynamic array                         |



## Examples
* enqueue
* dequeue
* get
* put
* pop
* popleft

See `queueExample.py` for examples. Feel free to play around with them!

<br />

## Problem
Doctor Who needs help keeping track of who's next in line. He keeps losing his printout and would like to have it digitally.
Create a queue that will store the names of any patient names supplied.

See `queueProblem.py` if you get stuck.
