#!/usr/bin/env python3
import argparse

# Initialize parser with a short description
parser = argparse.ArgumentParser(description='Compress a file using various algorithms')

# Add positional and optional arguments
parser.add_argument('input_file', help='file to be compressed')
parser.add_argument('output_file', help='compressed output file')
parser.add_argument('--alg', help='algorithm will be used')

# Parse argument
args = parser.parse_args()

print('Input file: {}'.format(args.input_file))
print('Output file: {}'.format(args.output_file))
print('Algorithm: {}'.format(args.alg))