import re

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def flatten_lol(lol):
  flat_list = []
  for l in lol:
    for word in l:
      flat_list.append(word)
  return flat_list

def print_word_freq(file):
   #empty lists 
    first = []
    frequency = {}
    

    with open(file) as f:
       #grab the item/words out of the text file
      for items in f:
          first.append(items)
        #remove the punctuation from the text  
      cleaned_text = []
      for w in first:
        clean = re.sub(r"[!?.,]","", w.lower())
        cleaner = clean.split()
        cleaned_text.append(cleaner)
        
    #run the clean text through the flatten function
      working_list = flatten_lol(cleaned_text)
      

      for word in list(working_list):  
          if word in STOP_WORDS:
           working_list.remove(word)
           for word in working_list:
             count = frequency.get(word,0)
             frequency[word] = count + 1
     
             frequency_list = frequency.keys()
            #counting the words in the text
             for words in frequency_list:
               
              print(words, '|' ,frequency[words]) 
# This is an "incantation." You will not see it very often, and it needs to be here to be able to pass file names as arguments.
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
