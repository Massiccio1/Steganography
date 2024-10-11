from PIL import Image
import numpy as np
from bitarray import bitarray

def encode(key, input_file="img/3.png",output_file="img/5.png"):

    print("loading...")
    im = Image.open(input_file)
    pixels = list(im.getdata())
    pixels  = list(map(list, pixels))

    # print(pixels)
    width, height = im.size
    
    text = key
    ending= "ç"
    full_text=text+ending
    offset = 0

    bin_stream = string_to_binary_stream(full_text)
    l = len(bin_stream)
    print("byte string: ", bin_stream)
    print("length: ", l)
    

    print("preparing...")
    pix_offset = 0
    rgb_offset = 0
    #image prep

    while offset < l:

        # (r,g,b)=(0,0,0)
        # print(r,g,b)
        if pixels[pix_offset][rgb_offset]%2==1:
            pixels[pix_offset][rgb_offset]-=1
        rgb_offset+=1
        offset+=1
        if rgb_offset==3:
            pix_offset+=1
            rgb_offset=0

    offset=0
    pix_offset = 0
    rgb_offset = 0  

    print("encoding...")

    #encode
    while offset < l:

        # (r,g,b)=(0,0,0)
        # print(r,g,b)
        pixels[pix_offset][rgb_offset]+=int(bin_stream[offset])
        offset+=1
        rgb_offset+=1
        if rgb_offset==3:
            pix_offset+=1
            rgb_offset=0

    pixels = [tuple(l) for l in pixels]
    image_out = Image.new(im.mode,im.size)
    image_out.putdata(pixels)
    image_out.save(output_file)# can give any format you like .png
    im.close()
    image_out.close()

    im.close()
    print("done")
    return output_file


def decode(input_file="img/5.png"):

    print("loading...")
    im = Image.open(input_file)
    pixels = list(im.getdata())
    pixels  = list(map(list, pixels))
    im.close()
    offset = 0
    pix_offset = 0
    rgb_offset = 0
    decoded_byte_string = ""

    print("decoding...")
    
    #decode
    while offset < len(pixels)*3:
        
        decoded_byte_string+=str(pixels[pix_offset][rgb_offset]%2)
        offset+=1
        rgb_offset+=1
        if rgb_offset==3:
            pix_offset+=1
            rgb_offset=0
    
        if len(decoded_byte_string)>=8 and offset%8==0 :
            tail = decoded_byte_string[-8:]
            # print(tail)
            # print(binary_stream_to_string(tail))

            if tail == "11100111":
                #terminal
                # print("string found: ", binary_stream_to_string(decoded_byte_string[:-8]))
                print("done")
                return binary_stream_to_string(decoded_byte_string[:-8])
    print("done, no string found")
    return  ""

def string_to_binary_stream(s):
    #chatgpt
    binary_stream = ""
    for char in s:
        # Convert each character to its ASCII value
        ascii_value = ord(char)
        # Convert the ASCII value to binary representation
        binary_representation = bin(ascii_value)[2:]  # [2:] to remove the '0b' prefix
        # Pad the binary representation to make sure it's 8 bits long
        binary_representation = binary_representation.zfill(8)
        # Concatenate the binary representation to the binary stream
        binary_stream += binary_representation
    return binary_stream

def binary_stream_to_string(binary_stream):
    char_string = ""
    # Iterate through the binary stream in chunks of 8 characters
    for i in range(0, len(binary_stream), 8):
        # Get the next 8 characters representing a byte
        byte = binary_stream[i:i+8]
        # Convert the binary representation back to an integer
        ascii_value = int(byte, 2)
        # Convert the ASCII value to a character and append it to the string
        char_string += chr(ascii_value)
    return char_string


def test():
    pass
                      
    
    

def main():
    
    # test()
    
    # return 0
    
    a = int(input(":: Welcome to Steganography ::\n"
                        "1. Encode\n2. Decode\n"))
    if (a == 1):
        key = input("string to encode: ")
        encode(key)
 
    elif (a == 2):
        print("Decoded Word :  " + decode())
    else:
        raise Exception("Enter correct input")
 

if __name__ == "__main__":
    main()