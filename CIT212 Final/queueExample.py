# Create examples of enqueueing, dequeueing, popping, etc

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