# Algorithms - ANTEQUINA (Non-linear Data Structures)

## 1. Binary Tree

### Build Tree
1. Start.
2. Create nodes: A, N, T, E, Q, U, I, N, A.
3. Set root = A.
4. Link A.left = N, A.right = T.
5. Link N.left = E, N.right = Q.
6. Link T.left = U, T.right = I.
7. Link E.left = N, E.right = A.
8. End.

### BFS (Level-order)
1. Start. Create an empty queue and an empty result list.
2. Enqueue the root (A).
3. While the queue is not empty:
   a. Dequeue a node and add its value to the result.
   b. If it has a left child, enqueue it.
   c. If it has a right child, enqueue it.
4. Print the result: A, N, T, E, Q, U, I, N, A.
5. End.

### DFS (Preorder)
1. Start with the root (A).
2. If the node is empty, return.
3. Visit the node (add to result).
4. Recursively traverse the left subtree.
5. Recursively traverse the right subtree.
6. Print the result: A, N, E, N, A, Q, T, U, I.
7. End.

## 2. Graph

### Build Graph
1. Start. Create vertices: A, N, T, E, Q, U, I, N2, A2.
2. Create an empty adjacency list for every vertex.
3. For each edge (u, v): add v to u's list and u to v's list.
   Edges: (A,N) (A,T) (N,E) (N,Q) (T,U) (T,I) (E,Q) (E,N2) (Q,U) (U,I)
4. Count edges: total = 10.
5. End. (A2 stays isolated.)

### BFS (start at A)
1. Create a queue, a visited set, and a result list.
2. Mark A visited and enqueue it.
3. While the queue is not empty:
   a. Dequeue vertex v, add to result.
   b. For each neighbor of v not visited: mark visited, enqueue.
4. Print: A, N, T, E, Q, U, I, N2.
5. End.

### DFS (start at A)
1. Create a visited set and a result list.
2. visit(v): mark v visited, add to result.
3. For each neighbor of v not visited, call visit(neighbor).
4. Call visit(A).
5. Print: A, N, E, Q, U, T, I, N2.
6. End.
