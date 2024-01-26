# temporary file to run program
import sys, os
from parser import *
from handler import *

def main():
  argc = len(sys.argv)
  if argc != 1 and argc != 2:
    exit()
  
  fs = []
  if argc == 1:
    path = "./data/"
    fs = os.listdir(path)
    fs = [path+file for file in fs]

  if argc == 2:
    fs.append(sys.argv[1])
  
  parser = Parser()
  handler = OutcomeHandler()
  for file in fs:
    if parser.parse(file):
      if handler.determine_call(parser.details):
        print(f"{file} = {handler.outcome}")
  exit()

if __name__=='__main__':
  main()
