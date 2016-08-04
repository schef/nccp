#!/usr/bin/python3
__author__ = "Stjepan Horvat"

import sys
import time
import subprocess
from subprocess import Popen, PIPE
from neovim import attach

nvim = attach('socket', path='/tmp/nvim')
buffer = nvim.current.buffer

startDelay = 3
msgDelay = 0.8
command = "char-write-req 0044"

def pasteFromClipboard():
  subprocess.call(["xdotool", "click", "2"])
  #subprocess.call(["xdotool", "key", "Return"])

def copyToClipboard(string):
  p = Popen(['xsel','-pi'], stdin=PIPE)
  p.communicate(input=string.encode('utf-8'))

def sendMsg(string):
  copyToClipboard(string + "\n")
  pasteFromClipboard()
  print(string)

def linesToClipboard(startLine, endLine):
  for i in range(startLine-1, endLine):
    string = buffer[i]
    status = "(" + str(i-startLine+2) + "/" + str(endLine-startLine+1) + ")"
    print(status)
    sendMsg(string)
    time.sleep(msgDelay)

def main():
  print("You have " + str(startDelay) + " seconds delay to set the mouse.")
  startLine = int(input("startLine> "))
  endLine = int(input("endLine> "))
  input("Press any key and position your mouse!>")
  time.sleep(startDelay)
  linesToClipboard(startLine, endLine)
  print("Finished successfully")

if __name__ == "__main__":
    main()
