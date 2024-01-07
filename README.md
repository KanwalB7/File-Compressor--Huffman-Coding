Compression using Huffman Coding: <br>
Compression Steps:<br>
#Access the file and extract the text from that file <br>
#Create a frequency Dictionary of each alphabet<br>
#Create a min-heap in order to get the two minimum frequences to construct a node<br>
#Construct Binary Tree from the Heap<br>
#Construct the code and store it in a map (dictionary)<br>
#Construct encoded text<br>
#Return the encoded binary file<br>

**Intended File to Compress:** alice_in_wonderland.txt (156 KB)

**Compressed File:** output.bin (86 KB)    (44.8% Compression)

**Decompressed File:** output_decompressed.txt(152 KB)

In order to compress your own file change the path in the code.
