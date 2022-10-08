try:
    import os, sys
    if len(sys.argv) == 1: sys.exit(f"use: python3 {sys.argv[0]} directory_name")
    else: parameters = sys.argv[1:]
    for dirname in parameters: os.mkdir(dirname)

except Exception as err:
    exit(err)
