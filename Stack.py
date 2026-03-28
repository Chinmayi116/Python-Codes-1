# Stack implementation using list

stack = []

# Push operation
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

# Pop operation
removed = stack.pop()
print("Popped element:", removed)

# Peek (top element)
top = stack[-1]
print("Top element:", top)

# Display stack
print("Final Stack:", stack)
