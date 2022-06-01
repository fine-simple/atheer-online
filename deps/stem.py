from ArabicStemmer.TAO_Arabic_Stemmer import TAOstemmer
import sys

stems_list = None

if(sys.argv[2] == "stem"):
    stems_list = TAOstemmer.text2stem(sys.argv[1], full=False)
elif(sys.argv[2] == "root"):
    stems_list = TAOstemmer.text2root(sys.argv[1])
elif(sys.argv[2] == "stem+"):
    stems_list = TAOstemmer.text2stem(sys.argv[1], full=True)

print(" ".join(stems_list))
sys.stdout.flush()