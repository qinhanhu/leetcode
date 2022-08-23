# 二叉树遍历框架
def traverse(root):
    if not root:
        return
    traverse(root.left)
    traverse(root.right)

#  多叉树遍历框架 
def traverse(root):
    if root == null:
        return
    for child in root.children:
        traverse(child)


# /* 图遍历框架 DFS */
visited = [false] * cntNodes
def traverse(graph, node):
    # 防止走回头路进入死循环
    if visited[node]:
        return
    # 前序遍历位置，标记节点 v 已访问
    visited[node] = true
    for neighbor in graph[v]:
        traverse(graph, neighbor)
# or 
def traverse(graph, node):
    visited[node] = true
    for neighbor in graph[v]:
        if not visited[neighbor]:
            traverse(graph, neighbor)

