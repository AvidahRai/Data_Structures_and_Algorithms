# Data Structures and Algorithms Cheat Sheet

| S.No | Data Structure / Operation                   | Time Complexity | Space Complexity | Notes |
|------|-----------------------------------------------|------------------|-------------------|-------|
| 1    | **Python List**                                   |            | O(n)              |       |
| 1.1  | Append                                        | O(1)             | O(1)              | O(1) Amortized |
| 1.2  | Pop (end)                                     | O(1)             | O(1)              |       |
| 1.3  | Prepend                                       | O(n)             | O(n)              | Shifting elements requires auxiliary space |
| 1.4  | Pop First                                     | O(n)             | O(n)              | Shifting elements requires auxiliary space |
| 1.5  | Insert (middle)                               | O(n)             | O(n)              | Shifting elements |
| 1.6  | Remove (by value)                             | O(n)             | O(n)              | Shifting elements |
| 1.7  | Lookup (by index)                             | O(1)             | O(1)              |       |
| 1.8  | Lookup (by value)                             | O(n)             | O(1)              |       |
| 2    | **Singly Linked List**                            |             | O(n)              | Using Nodes |
| 2.1  | Append                                        | O(1)             | O(1)              |       |
| 2.2  | Pop (end)                                     | O(n)             | O(1)              |       |
| 2.3  | Prepend                                       | O(1)             | O(1)              |       |
| 2.4  | Pop First                                     | O(1)             | O(1)              |       |
| 2.5  | Get                                           | O(n)             | O(1)              |       |
| 2.6  | Set                                           | O(n)             | O(1)              |       |
| 2.7  | Insert                                        | O(n)             | O(1)              |       |
| 2.8  | Remove                                        | O(n)             | O(1)              |       |
| 2.9  | Lookup (by index)                             | O(n)             | O(1)              |       |
| 2.10 | Lookup (by value)                             | O(n)             | O(1)              |       |
| 3    | **Doubly Linked List**                            |              | O(n)              | Using Nodes |
| 3.1  | Print List                                    | O(n)             | O(1)              |       |
| 3.2  | Append                                        | O(1)             | O(1)              |       |
| 3.3  | Pop                                           | O(1)             | O(1)              |       |
| 3.4  | Prepend                                       | O(1)             | O(1)              |       |
| 3.5  | Pop First                                     | O(1)             | O(1)              |       |
| 3.6  | Get                                           | O(n)             | O(1)              |       |
| 3.7  | Set                                           | O(n)             | O(1)              |       |
| 3.8  | Insert                                        | O(n)             | O(1)              |       |
| 3.9  | Remove                                        | O(n)             | O(1)              |       |
| 4    | **Stack (Nodes)**                                 |              | O(n)              |       |
| 4.1  | Print Stack                                   | O(n)             | O(1)              |       |
| 4.2  | Push                                          | O(1)             | O(1)              |       |
| 4.3  | Pop                                           | O(1)             | O(1)              |       |
| 5    | **Queue (Nodes)**                                 |              | O(1)              |       |
| 5.1  | Print Queue                                   | O(n)             | O(1)              |       |
| 5.2  | Enqueue                                       | O(1)             | O(1)              |       |
| 5.3  | Dequeue                                       | O(1)             | O(1)              |       |
| 6    | **Hash Table (w/ Collision Handling)**            |             | O(n)              | Amortized |
| 6.1  | Hashing (private)                             | O(1)             | O(1)              | `hash = (hash + ord(c) * 23) % len(map)` |
| 6.2  | Set                                           | O(1)*            | O(1)              | *Amortized; worst case O(n) |
| 6.3  | Get                                           | O(1)*            | O(1)              | *Amortized; worst case O(n) |
| 6.4  | Keys                                          | O(n)             | O(n)              |       |
| 7    | **Binary Search Tree**                            |        | O(n)              | *Balanced; O(n) unbalanced |
| 7.1  | Insert                                        | O(log n)*        | O(1)              | *Worst case O(n) |
| 7.2  | Contains                                      | O(log n)*        | O(1)              | *Worst case O(n) |
| 8    | **Heap (Python List)**                           |              | O(n)              |       |
| 8.1  | Swap (private)                                | O(1)             | O(1)              |       |
| 8.2  | Sink Down                                     | O(log n)         | O(1)              |       |
| 8.3  | Insert (bubble up)                            | O(log n)         | O(1)              |       |
| 8.4  | Remove (sink down)                            | O(log n)         | O(1)              |       |
| 9    | **Trie**                                          |             | O(n)              | n = length of word |
| 9.1  | Lookup                                        | O(n)             |                   |       |
| 9.2  | Insert                                        | O(n)             |                   |       |
| 10   | **Graph (Adjacency Matrix)**                      |                  | O(n²)             |       |
| 10.1 | Add Vertex                                    | O(n²)            | O(n²)             |       |
| 10.2 | Add Edge                                     | O(1)             | O(n²)             |       |
| 10.3 | Remove Edge                                  | O(1)             | O(n²)             |       |
| 10.4 | Remove Vertex                                | O(n²)            | O(n²)             |       |
| 11   | **Graph (Adjacency List)**                        |          | O(n)              | v = vertices, e = edges |
| 11.1 | Print Graph                                   | O(v + e)         | O(n)              |       |
| 11.2 | Add Vertex                                    | O(1)             | O(n)*             | *Amortized |
| 11.3 | Add Edge                                      | O(1)             | O(1)              |       |
| 11.4 | Remove Edge                                   | O(n)             | O(n)              |       |
| 11.5 | Remove Vertex                                 | O(n)             | O(n)              |       |
| 12   | **Recursive Binary Search Tree**                  |         | O(n)              | *Worst case O(n) unbalanced |
| 12.1 | Contains                                      | O(log n)*        | O(1)              |       |
| 12.2 | Insert                                        | O(log n)*        | O(1)              |       |
| 12.3 | Delete                                        | O(log n)*        | O(1)              |       |
| 13   | **Tree / Graph Traversal**                        |              |                   |       |
| 13.1 | Breadth-First Search                          | O(n)             | O(n)              |       |
| 13.2 | DFS Preorder                                  | O(n)             | O(log n)          | Worst case O(n) unbalanced |
| 13.3 | DFS Postorder                                 | O(n)             | O(log n)          |       |
| 13.4 | DFS Inorder                                   | O(n)             | O(log n)          |       |
| 14   | **Basic Sorting Algorithms**                      |                  |                   |       |
| 14.1 | Bubble Sort                                   | O(n²)            | O(1)              |       |
| 14.2 | Selection Sort                                | O(n²)            | O(1)              |       |
| 14.3 | Insertion Sort                                | O(n²) / O(n)*    | O(1)              | *Best-case O(n) |
| 15   | **Merge Sort**                                    | O(n log n)       | O(n)              |       |
| 16   | **Quick Sort**                                    | O(n log n)*      | O(1)   
