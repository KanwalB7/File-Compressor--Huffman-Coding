Compression using Huffman Coding:
Compression Steps:
#Access the file and extract the text from that file
#Create a frequency Dictionary of each alphabet
#Create a min-heap in order to get the two minimum frequences to construct a node
#Construct Binary Tree from the Heap
#Construct the code and store it in a map (dictionary)
#Construct encoded text
#Return the encoded binary file

**Intended File to Compress:** alice_in_wonderland.txt (156 KB)

**Compressed File:** output.bin (86 KB)    (44.8% Compression)

**Decompressed File:** output_decompressed.txt(152 KB)

In order to compress your own file change the path in the code.
