#!/usr/bin/python3
from Atheer.ATHEER_Arabic_Stemmer import AtheerStemmer
import sys

stems_list = None

if(sys.argv[2] == "stem"):
    stems_list = AtheerStemmer.text2stem(sys.argv[1], full=False)
elif(sys.argv[2] == "root"):
    stems_list = AtheerStemmer.text2root(sys.argv[1])
elif(sys.argv[2] == "stem+"):
    stems_list = AtheerStemmer.text2stem(sys.argv[1], full=True)

print(" ".join(stems_list))
sys.stdout.flush()