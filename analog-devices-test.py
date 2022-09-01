#!/usr/bin/env python

import random
import sys
import struct

intermediate_output = "intermediate_output.txt"
final_output = "final_output.txt"

try:
    input = sys.argv[1]
except IndexError:
    print("Usage: %s <random_number>" %sys.argv[0])
    sys.exit(1)

def generateRandomNumber():
    """
    Generate Random number
    """

    intermediate = open(intermediate_output, 'w')
    for i in range(int(input)):
        x = round(i*random.random(),2)  #only for 2 round off 
        intermediate.writelines(str(x) + '\n')
    intermediate.close()
    print("====================================================")
    print("intermediate output file:", intermediate_output )
    print("====================================================")
    intermediate = open(intermediate_output, 'r')
    content=intermediate.read()
    print(content)
    intermediate.close()


def convertToBinary():
    """
    Convert numbers to binary
    """
    final = open(final_output, 'w')
    with open(intermediate_output) as input_file:
      for line in input_file:
        final.writelines(''.join('{:0>8b}'.format(c) for c in struct.pack('!f', float(line.rstrip()))) + '\n')
    input_file.close()
    final.close()
    print("====================================================")
    print("Final output file:", final_output )
    print("====================================================")
    final = open(final_output, 'r')
    content=final.read()
    final.close()
    print(content)


# Main
generateRandomNumber()
convertToBinary()
