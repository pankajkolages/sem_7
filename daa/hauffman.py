# ------------------------------------------------------------
# Program: Huffman Encoding using Greedy Method
# Description:
#   This program implements Huffman Coding for data compression.
#   It uses a greedy strategy to assign shorter codes to
#   more frequent characters.
# ------------------------------------------------------------

import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char      # Character (letter)
        self.freq = freq      # Frequency of the character
        self.left = None      # Left child
        self.right = None     # Right child

    # Less than operator for priority queue (heap)
    def __lt__(self, other):
        return self.freq < other.freq


# Function to generate Huffman Codes recursively
def generate_codes(node, code, huffman_dict):
    if node is None:
        return
    # Leaf node -> assign code
    if node.char is not None:
        huffman_dict[node.char] = code
        return
    # Traverse left (add 0)
    generate_codes(node.left, code + "0", huffman_dict)
    # Traverse right (add 1)
    generate_codes(node.right, code + "1", huffman_dict)


# Huffman Encoding main function
def huffman_encoding(char_freq):
    # Step 1: Create a priority queue (min-heap)
    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    # Step 2: Build Huffman Tree
    while len(heap) > 1:
        # Extract two smallest frequency nodes
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        # Create a new internal node with combined frequency
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        # Insert back into heap
        heapq.heappush(heap, merged)

    # Step 3: Generate Huffman Codes
    root = heap[0]
    huffman_dict = {}
    generate_codes(root, "", huffman_dict)
    return huffman_dict


# -------------------- MAIN PROGRAM ---------------------------

if __name__ == "__main__":
    print(" Huffman Encoding using Greedy Strategy ")

    # Step 1: Input characters and their frequencies
    num = int(input("Enter number of characters: "))
    char_freq = {}

    for i in range(num):
        char = input(f"Enter character {i+1}: ")
        freq = int(input(f"Enter frequency of '{char}': "))
        char_freq[char] = freq

    # Step 2: Perform Huffman Encoding
    huffman_codes = huffman_encoding(char_freq)

    # Step 3: Display the results
    print("\n Huffman Codes for the given characters:")
    print("----------------------------------------")
    for char, code in huffman_codes.items():
        print(f"Character: {char}   |   Code: {code}")


# | Type      | Complexity | Explanation                                                  |
# | --------- | ---------- | ------------------------------------------------------------ |
# | **Time**  | O(n log n) | Because each heap operation (insert/delete) takes log n time |
# | **Space** | O(n)       | For storing nodes and final codes                            |

# | Question                      | Answer                                                                                                |
# | ----------------------------- | ----------------------------------------------------------------------------------------------------- |
# | What is Huffman Encoding?     | A greedy algorithm for lossless data compression that assigns shorter codes to more frequent symbols. |
# | Why is it greedy?             | It always picks the two least frequent nodes to combine at every step.                                |
# | What data structure is used?  | A **min-heap (priority queue)**.                                                                      |
# | Is Huffman Encoding lossless? | Yes, it’s a **lossless compression algorithm**.                                                       |
# | What is the time complexity?  | O(n log n).                                                                                           |
# | What is the optimal property? | It produces the smallest possible average code length for the given frequencies.                      |
