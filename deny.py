import os, platform
print(" Loading ")
bit = platform.architecture()[0]
if "64bit" in bit:
  import deny64
else:
  print(" Not Supported ")
