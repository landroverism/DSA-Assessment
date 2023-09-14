def is_balanced(expression):
  stack = []
  mapping = {')': '(','}','{', ']': '['}
  for char in expression:
    if char in mapping.values():
      stack.append(char)
    elif char in mapping.keys():
      if stack and stack[-1] == mapping[char]:
        stack.pop()
      else:
        return 0
  return  not stack 

  expression1 = "([{}])"
  expression2 = "([)]"
  print(is_balanced(expression1))
  print(is_balanced(expression2))


    

