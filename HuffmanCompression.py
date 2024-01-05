#To access the file and extract the text from that file
#Create a frequency Dictionary of each alphabet
#Create a min-heap in order to get the two minimum frequences to construct a node
#Construct Binary Tree from the Heap
#Construct the code and store it in a map (dictionary)
#Construct encoded text
 #Return the encoded binary file
import heapq, os

class BinaryTree:
    #Every node has a value, frequency, 
    def __init__(self, value, frequency):
        self.value= value
        self.frequency= frequency

        #Setting left and right child None initially
        self.left= None
        self.right= None

    #inbuilt push method cannot make comparisions based on Binary Trees 
    def __lt__(self, other):
        #Comparing based on frequency
        return self.frequency< other.frequency
    
    def __eq__(self, other):
        return self.frequency== other.frequency
    
    def print_tree(self, level=0, prefix="Root: "):
        print(" " * (level * 4) + prefix + f"{self.value} ({self.frequency})")
        if self.left:
            self.left.print_tree(level + 1, "L--- ")
        if self.right:
            self.right.print_tree(level + 1, "R--- ") 


class HuffmanCompression:
    
    def __init__(self,path):
        self.path= path
        
        #Iterable for heap
        self.__heap= []

        #Dictionary for saving the huffmaan matching from the tree
        self.__code= {}

        self.__reversecode= {}

    
    #__ (double underscore for private function)
    def __frequency_from_text(self, text):
        frequency_dictionary= {}
        for char in text:
            if char not in frequency_dictionary:
                frequency_dictionary[char]= 0
            # else:
            frequency_dictionary[char]+= 1
        
        return frequency_dictionary
    
    def __build_heap(self, frequency_dictionary):
        for key in frequency_dictionary:
            frequency= frequency_dictionary[key]

            #Add to binary tree
            node= BinaryTree(key, frequency)    #Create Node
            heapq.heappush(self.__heap, node)       #Push the value to the heap (only contains key and frequency)


    def __build_huffman_tree(self):

        while len(self.__heap)> 1:
            
            node_1 = heapq.heappop(self.__heap)
            node_2 = heapq.heappop(self.__heap)
            
            merged_node = BinaryTree(None, node_1.frequency + node_2.frequency)
            merged_node.left = node_1
            merged_node.right = node_2

            heapq.heappush(self.__heap, merged_node)

        #Return the root of the huffman tree
        return self.__heap[0]


    def __build_tree_code_helper(self,root,curreent_code):
        if root is None:
            return
        
        #Since for leaf node we have a value, we have reached the leaf and required code
        if root.value is not None:
            self.__code[root.value]= curreent_code
            self.__reversecode[curreent_code]= root.value
            return

        #Call left or right
        self.__build_tree_code_helper(root.left, curreent_code+'0')
        self.__build_tree_code_helper(root.right, curreent_code+'1')

    def __build_tree_code(self):
        root= heapq.heappop(self.__heap)
        self.__build_tree_code_helper(root, '')

    def __build_encoded_text(self, text):
        encoded_text= ''

        for char in text:
            #Get encoded text/ encryption from the underlying code array
            encoded_text+= self.__code[char]
        
        return encoded_text
    
    def __build_padded_encoded_text(self, encoded_text):
        # Formula 8- l%8
        padding_value= 8 - len(encoded_text) % 8
        #Append zero the number of times

        for i in range(0, padding_value):
            encoded_text+='0'

        #8-bit string with leading zeros
        padded_info= format(padding_value, "08b")          #*****************************************************
        # padded_info= "{:08b}".format(padding_value) 

        padded_text= padded_info+encoded_text

        return padded_text
    
    def __build_byte_array(self, padded_text):
        #In binary
        byte_array= []
        #Increment with 8 in order to slice it to one byte
        for i in range(0, len(padded_text), 8):
            byte= padded_text[i:i+8]

            byte_array.append(int(byte,2))
        
        return byte_array

        
    def compression(self):

        # text= "abcdadfnjjkncjbjcvnbcbvxnbxvncxbvnbxvcwhoqefhuihyropr"
        #Getting the filename and extension
        # filename, file_extension= os.path.splittext(self.path)
        print("Starting Compression\n")
        # We are returning a compressed output file
        output_path = 'output' + '.bin'

        # Reading the file
        with open(self.path, 'r') as file:
            text = file.read().rstrip()  # Remove extra spaces using rstrip()

            frequency_dictionary = self.__frequency_from_text(text)

            print(f'Frequency Dictionary: \n{frequency_dictionary}\n')
            #Now we have the frequency table
            #Create a heap now:
            heap_frequency= self.__build_heap(frequency_dictionary)

            #Can print to see the current Tree values
            huffman_tree= self.__build_huffman_tree()

            # Uncomment to see the underlying created Huffman Tree
            # print(f'Huffman tree:')
            # huffman_tree.print_tree()

            #Build the dictionary for all codes for respective nodes
            self.__build_tree_code()
            print(f'Code Dictionary: \n{self.__code}\n')

            #Encode the Given Text
            encoded_text= self.__build_encoded_text(text)
            #Uncomment to see the encoded text
            # print(f'Encoded Text: \n{encoded_text}\n')

            #Padding in order to make it 8-bit representation
            padded_encoded_text= self.__build_padded_encoded_text(encoded_text)


            #Uncomment to see the padded encoded text
            # print(padded_encoded_text)

            #Inorder to read convert it into bytes
            bytes_array= self.__build_byte_array(padded_encoded_text)

            #Convert bytes array to final bytes
            final_bytes= bytes(bytes_array)

        with open(output_path, 'wb') as output:
            output.write(final_bytes)

        #Return Output File
        print("Compressed successfully....")
        return output_path

    def __remove_padding(self, text):
        padded_info= text[:8]
        padded_value= int(padded_info, 2)

        text= text[8:]
        text= text[:-1*padded_value]
        return text

    def __decoded_text(self, text):
        current_bits= ''
        decoded_text= ''

        for char in text:
            current_bits+= char
            if current_bits in self.__reversecode:
                decoded_text+= self.__reversecode[current_bits]
                current_bits= ''
        
        return decoded_text

    def decompress(self, input_path):
        output_path= 'output_decompressed' + '.txt'
        
        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string= ''
            byte= file.read(1)

            while byte:
                byte= ord(byte)
                bits= bin(byte)[2:].rjust(8,'0')
                bit_string+= bits
                byte= file.read(1)

            text_after_remove_padding= self.__remove_padding(bit_string)

            original_text= self.__decoded_text(text_after_remove_padding)

            output.write(original_text)

        return output_path


one = HuffmanCompression('alice_in_wonderland.txt')

frequency_dictionary= one.compression()

decompressedFile= one.decompress('output.bin')


 

