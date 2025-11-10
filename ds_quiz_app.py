import streamlit as st

st.title("📘 Data Structures Quiz")

questions = [
    {
        "question": "1. Which data structure works on FIFO principle?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "Queue"
    },
    {
        "question": "2. Which data structure uses LIFO principle?",
        "options": ["Queue", "Stack", "Array", "Linked List"],
        "answer": "Stack"
    },
    {
        "question": "3. What is the time complexity of binary search in a sorted array?",
        "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"],
        "answer": "O(log n)"
    },
    {
        "question": "4. Which data structure is best for implementing recursion?",
        "options": ["Queue", "Tree", "Stack", "Graph"],
        "answer": "Stack"
    },
    {
        "question": "5. Which of the following is a linear data structure?",
        "options": ["Graph", "Tree", "Array", "Hash Table"],
        "answer": "Array"
    },
    {
        "question": "6. Which tree is used in database indexing?",
        "options": ["Binary Tree", "AVL Tree", "B-Tree", "Heap"],
        "answer": "B-Tree"
    },
    {
        "question": "7. What is the maximum number of children a binary tree node can have?",
        "options": ["1", "2", "3", "4"],
        "answer": "2"
    },
    {
        "question": "8. Which data structure provides the fastest lookup on average?",
        "options": ["Array", "Linked List", "Hash Table", "Queue"],
        "answer": "Hash Table"
    },
    {
        "question": "9. Which heap is used in Dijkstra’s algorithm?",
        "options": ["Max Heap", "Min Heap", "Fibonacci Heap", "Binary Search Tree"],
        "answer": "Min Heap"
    },
    {
        "question": "10. Traversing a graph level-by-level is done using:",
        "options": ["DFS", "BFS", "Inorder Traversal", "Postorder Traversal"],
        "answer": "BFS"
    }
]

score = 0

for q in questions:
    st.write(f"### {q['question']}")
    user_answer = st.radio("", q['options'], key=q['question'])
    if user_answer == q['answer']:
        score += 1

st.write("---")
st.write(f"## ✅ Your Score: **{score} / {len(questions)}**")
