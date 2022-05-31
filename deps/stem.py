from ArabicStemmer.TAO_Arabic_Stemmer import TAOstemmer
import sys

stems_list = TAOstemmer.text2root(sys.argv[1])

print(" ".join(stems_list))
sys.stdout.flush()