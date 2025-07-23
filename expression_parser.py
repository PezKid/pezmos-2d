# expression interface
class Expr:
  def evaluate(self, env):
    pass

  def __repr__(self):
    pass

# classes inheriting Expr
class Num(Expr):
  def __init__(self, value):
    self.value = value

  def evaluate(self, env):
    return self.value

  def __repr__(self):
    return f'Num({self.value})'

class Var(Expr):
  def __init__(self, name):
    self.name = name

  def evaluate(self, env):
    return env[self.name]

  def __repr__(self):
    return f'Var({self.name})'

class Add(Expr):
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def evaluate(self, env):
    return self.left.evaluate(env) + self.right.evaluate(env)

  def __repr__(self):
    return f'Add({self.left}, {self.right})'

class Mul(Expr):
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def evaluate(self, env):
    return self.left.evaluate(env) * self.right.evaluate(env)

  def __repr__(self):
    return f'Mul({self.left}, {self.right})'
  
  

def tokenize(string):
  tokens = []
  i = 0
  
  while (i < len(string)):
    char = string[i]
    
    if char.isspace():
      i += 1
      continue
    
    elif char.isdigit():
      num = char
      i += 1
      while (i < len(string) and (string[i] == '.' or string[i].isdigit())):
        num += string[i]
        i += 1
      tokens.append(("NUMBER", num))
    
    elif char.isalpha():
      ident = char
      i += 1
      while (i < len(string) and string[i].isalpha()):
        ident += string[i]
        i += 1
      tokens.append(("IDENT", ident))

    elif char == '+':
      tokens.append(("PLUS", char))
      i += 1
    elif char == '-':
      tokens.append(("MINUS", char))
      i += 1
    elif char == '*':
      tokens.append(("TIMES", char))
      i += 1
    elif char == '/':
      tokens.append(("DIVIDE", char))
      i += 1
    elif char == '(':
      tokens.append(("LPAREN", char))
      i += 1
    elif char == ')':
      tokens.append(("RPAREN", char))
      i += 1
    else:
      raise ValueError(f"Unexpected character: {char}")
  
  return tokens