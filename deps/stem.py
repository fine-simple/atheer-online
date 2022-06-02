#!/usr/bin/python3
from Atheer.ATHEER_Arabic_Stemmer import AtheerStemmer
import sys

stems_list = None

if(sys.argv[2] == "stem"):
    stems_list = AtheerStemmer.text2stem(sys.argv[1], full=False)
elif(sys.argv[2] == "plus"):
    stems_list = AtheerStemmer.text2stem(sys.argv[1], full=True)
elif(sys.argv[2] == "root"):
    stems_list = AtheerStemmer.text2root(sys.argv[1])

print(" ".join(stems_list))
sys.stdout.flush()