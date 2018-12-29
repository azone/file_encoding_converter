#!/usr/bin/env python

import sys
import argparse
import codecs

def print_error(error_string):
    sys.stderr.write(error_string + '\n')
    sys.stderr.flush()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Convert a file\'s encoding to what you want.')
  parser.add_argument('input_file', metavar='input_file', help='Input file', nargs=1)
  parser.add_argument('-o', '--output_file', help='Output file(this will replace the input file if not specified)', default=None)
  parser.add_argument('-d', '--input_encoding', help='Input encoding', default='GBK')
  parser.add_argument('-e', '--output_encoding', help='Output encoding', default='UTF-8')
  args = parser.parse_args()

  try:
    input_file_count = len(args.input_file)
    for input_file in args.input_file:
      with codecs.open(input_file, 'rb', encoding=args.input_encoding) as fp:
        content = fp.read()
        encoded_content = codecs.encode(content, args.output_encoding)
        output_file = None if input_file_count > 1 else args.output_file
        if output_file is None:
          output_file = input_file
        with open(output_file, 'wb') as new_fp:
          new_fp.write(encoded_content)
  except IOError as error:
    print_error(error)
    sys.exit(2)
  except ValueError as error:
    print(error)
    sys.exit(2)
  else:
    pass