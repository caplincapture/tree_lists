# Constructor
def is_tree(tree):
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

# Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def square_tree(t):
  sq_branches = [square_tree(branch) for branch in branches(t)]
  return tree(label(t)**2, sq_branches)

def tree_max(t):
  return max([label(t)] + [tree_max(branch) for branch in branches(t)])

def find_path(tree, x):
    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree):
      p
        path = find_path(b, x)
        if path:
          print(path)
            return [label(tree)] + path

        
def is_min_heap(t):
    for b in branches(t):
        if label(t) > label(b) or not is_min_heap(b):
            return False
    return True

def largest_product_path(tree):
    if not tree:
        return 0
    elif is_leaf(tree):
        return label(tree)
    else:
        paths = [label(tree) * largest_product_path(b) for b in branches(tree)]
        return max(path)        

# Iterative implementation
def level_order(tree):
    if not tree:
        return []
    current_level, next_level = [label(tree)], [tree]
    while next_level:
        find_next= []
        for b in next_level:
            find_next.extend(branches(b))
        next_level = find_next
        current_level.extend([label(t) for t in next_level])
    return current_level
# Recursive implementation

def level_order(tree):
    def find_next(current_level):
        if current_level == []:
            return []
        else:
            next_level = []
            for b in current_level:
                next_level.extend(branches(b))
            return [label(t) for t in next_level] + find_next(next_level)
    return [label(tree)] + find_next([tree])

t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
print(find_path(t, 5))
#print(find_path(t, 10)) # returns None
#tree(label(t)**2, sq_branches)
### LIBRARY FOR TESTING ###
t = tree(1,[tree(3,[tree(4),tree(5)]),tree(2)])
numbers = tree(1,[tree(2,[tree(3),tree(4)]),tree(5,[tree(6,[tree(7)]),tree(8)])])
#print(square_tree(numbers))
#print(tree_max(t))
#print(is_leaf(t))

def acorn_finder(t):
  def find_acorn(t, arg='acorn'):
    if label(t) == arg:
      return True
    for b in branches(t):
      path = find_acorn(b, arg)
      if path:
        return True
    return False
  return find_acorn(t,arg='acorn')

scrat = tree('acorn')
print(acorn_finder(scrat))

sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('acorn')]), tree('branch2')])
print(acorn_finder(sproul))
numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
print(acorn_finder(numbers))
t = tree(1, [tree('acorn',[tree('not acorn')])])
print(acorn_finder(t))
