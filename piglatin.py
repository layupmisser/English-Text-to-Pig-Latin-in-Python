# """Converter uses regex to isolate English words from symbols and whitespace. Then, the functions below easily find and convert each word individually into pig latin then writes them into the output file."""
# Run using the following command
# python3 piglatin.py [--input inputFilePath] [--output outputFilePath] 
# Example:
  # python3 piglatin.py --input data.txt --output out.txt

import re #regex 
import argparse

class PigLatin:

  defaultOutputFilePath = "out.txt" 
  consonantSuffix = "ay" # the suffix that is added when the first letter/first two letters are consonants

  # Driver function. Use this for conversion of a file into piglatin.
  def fileLatinify(self, inputFile="data.txt", outputFile="out.txt"):
    f = open(inputFile, "r")

    # if output file is none then default to out.txt
    if (outputFile == None):
      outputFile = self.defaultOutputFilePath

    lineList = f.readlines()
    newLineList = [] # List of strings
    
    # Take every line of the file, isolate the words, symbols, and whitespace 
    # Then, loop through and modify only the words into pig latin 
    for line in lineList:
      wordList = self.splitString(line) # returns a list of symbols, whitespace, and words
      newWordList = []

      for word in wordList:
        # check to see if the "word" is alphabetical or not
        # skip if they are a symbol or a space

        # make sure that the current "word" has only alphabetical characters and is actually a word
        if (re.match(r"[A-Za-z]+",word[0:1]) != None):
          if (re.match(r"[aeiouAEIOU]",word[0:1]) != None): # if first letter is a vowel, perform vowel convert on the word
            word = self.vowelConvert(word)
          elif (re.match(r"[^aeiouAEIOU][^aeiouAEIOU]", word[0:2]) != None): # if first two letters are consonants, do the twoConsonantCOnvert
            word = self.twoConsonantConvert(word)
          else: # if the first letter is a consonant, do the consonant convert
            word = self.oneConsonantConvert(word) 

        newWordList.append(word)
        print("word: {}".format(word))

      # Join together the list of words using .join() into one string, then add to the list of new lines        
      newLineList.append("".join(newWordList)) # Join the split list from splitString() together
      print("final wordList after loop: {}".format(newWordList))

    f.close()
    # output into a text file
    print(newLineList)
    
    n = open(outputFile, "w") # "w" will override existing content
    
    # Write all the new piglatinified lines into the given output file
    for line in newLineList:
      n.write(line)
    n.close()


  # Isolate words, symbols, and white space from a given line from the file
  # Example:
    # ['', 'When', ' ', 'Mr', '. ', 'Bilbo', ' ', 'Baggins', ' ', 'of', ' ', 'Bag', ' ', 'End', ' ', 'announced', ' ', 'that', ' ', 'he', ' ', 'would', ' ', 'shortly', ' ', 'be', ' ', 'celebrating', ' ', 'his', ' ', 'eleventy', '-', 'first', ' ', 'birthday', ' ', 'with', ' ', 'a', ' ', 'party', ' ', 'of', ' ', 'special', ' ', 'magnificence', ', ', 'there', ' ', 'was', ' ', 'much', ' ', 'talk', ' ', 'and', ' ', 'excitement', ' ', 'in', ' ', 'Hobbiton', '.\n']
  def splitString(self, s):

    # \b patterns means to select the empty character, which is a string with no length that is before and after every string
    # the "r" prefix to the pattern tells Python not to parse the string, thus, "\b" is taken literally as a backslash and b
    pattern = r"\b" 
    wordList = re.split(pattern, s) # Gives us a list of strings that are separated by "empty string"

    print("Wordlist from split string: {}".format(wordList))
    return wordList
    

  # 1. If a word starts with a consonant and a vowel, put the first letter of the word at the end of the word and add "ay"
    # Example: Happy = appyh + ay = Appyhay
  def oneConsonantConvert(self, word):
    # check to see if first letter is capitalized
    # if so, make so to capitalize the new first letter 
    firstLetter = word[0:1]

    newWord = word[1:] # take all parts of the word except for the 0th character
    newWord = newWord + firstLetter.lower() + self.consonantSuffix # create the new word and add the piglatin suffix

    # Captialize the new first letter if the original first letter was upper
    if (firstLetter.isupper()):
      letterList = list(newWord)  # we must convert it into a list because strings are not mutable -> converting to list first is a loop hole to do the same thing
      letterList[0] = letterList[0].upper()
      newWord = "".join(letterList) # convert back to a string using .join
    
    return newWord

  
  # 2. If a word starts with two consonants move the two consonants to the end of the word and add "ay"
    # Example: Child = Ildch + ay = Ildchay
  def twoConsonantConvert(self, word):
    firstTwoLetters = word[0:2]

    newWord = word[2:]
    newWord = newWord + firstTwoLetters.lower() + self.consonantSuffix

    # Captialize first letter if the original first letter was capitalized
    letterList = list(newWord) # must convert into list since strings are not mutable
    if (firstTwoLetters[0].isupper()):
      letterList[0] = letterList[0].upper()
    # Captialize second letter if the original second letter was capitalized
    if (firstTwoLetters[1].isupper()):
      letterList[1] = letterList[1].upper()

    newWord = "".join(letterList) # convert back to string
    
    return newWord
    
  # 3. If a word starts with a vowel add the word "way" at the end of the word.
  # Example: Awesome = Awesome +way = Awesomeway
  def vowelConvert(self, word):
    return word + "way"

  
  
  
  
# main function should use argparse
  # should have a default output file if none was specified
    # use out.txt as the default
  
    # 1. The code must use the Python argparseLinks to an external site. library to parse command-line arguments and select the input text file. Include an optional argument for the user to specify the name of output file, and if not specified, use out.txt as a default. An example execution would be:
  
    # python3 piglatin.py --input data.txt --output data_out.txt
  
  # 4. The output file must retain all of the punctuation used in the input text file, including whitespace, quotation marks, periods, newlines, and numbers. 
    # find out if readlines preserves whitespace

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--input")
  parser.add_argument("--output")
  args = parser.parse_args()

  PigLatin().fileLatinify(args.input, args.output)

main()