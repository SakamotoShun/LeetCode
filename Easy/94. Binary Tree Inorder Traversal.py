nodes_val, tracking = [],[]

while root != None:
    if root.left != None:
        tracking.append(root)
        root = root.left
    elif root.right != None:
        nodes_val.append(root.val)
        root = root.right
    else:
        nodes_val.append(root.val)
        if len(tracking) > 0:
            root = tracking.pop()
            if root != None:
                root.left = None
        else:
            root = None
            
return nodes_val
