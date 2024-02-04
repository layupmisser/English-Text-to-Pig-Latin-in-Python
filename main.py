import re
import os.path

# 2. The code must include a succinct description of the converter at the top of the file using triple quotes. Put appropriate code comments to promote readability.

class PigLatin:

  defaultOutputFilePath = "out.txt"
  
  # driver
  def fileLatinify(self, inputFile, outputFile="out.txt"):
    f = open(inputFile, "r")

    # if output file is none
    # then default to out.txt

    # If no output file exists at the given path, output to the specified default instead
    if (os.path.isfile(outputFile)):
      outputFile = self.defaultOutputFilePath

    lineList = f.readlines()
    newLineList = [] # List of strings
    
    for line in lineList:
      wordList = self.splitString(line)
      newWordList = []

      for word in wordList:
        # check to see if the "word" is alphabetical or not
        # skip if they are a symbol or a space

        if (re.match(r"[A-Za-z]+",word[0:1]) != None):
          if (re.match(r"[aeiouAEIOU]",word[0:1]) != None):
            word = self.vowelConvert(word)
          elif (re.match(r"[^aeiouAEIOU][^aeiouAEIOU]", word[0:2]) != None):
            word = self.twoConsonantConvert(word)
          else:
            word = self.oneConsonantConvert(word)

        newWordList.append(word)
        print("word: {}".format(word))
        
      newLineList.append("".join(newWordList)) # Join the split list from splitString() together
      print("final wordList after loop: {}".format(newWordList))

    
    # output into a text file
    print(newLineList)
  

  def splitString(self, s):
    pattern = r"\b" # not sure what the preceding r does but it changes the meaning big time
    wordList = re.split(pattern, s)
    # Gives us a list of strings that are separated by "empty string"
    # Example:
      # ['', 'When', ' ', 'Mr', '. ', 'Bilbo', ' ', 'Baggins', ' ', 'of', ' ', 'Bag', ' ', 'End', ' ', 'announced', ' ', 'that', ' ', 'he', ' ', 'would', ' ', 'shortly', ' ', 'be', ' ', 'celebrating', ' ', 'his', ' ', 'eleventy', '-', 'first', ' ', 'birthday', ' ', 'with', ' ', 'a', ' ', 'party', ' ', 'of', ' ', 'special', ' ', 'magnificence', ', ', 'there', ' ', 'was', ' ', 'much', ' ', 'talk', ' ', 'and', ' ', 'excitement', ' ', 'in', ' ', 'Hobbiton', '.\n']

    print("Wordlist from split string: {}".format(wordList))
    return wordList
    

    
  # need to find a way to see if a letter is contained within a list of acceptable letters
    # could potentially use regex

  # have a convert() function that calls the other helper functions

  # 5. The output file must retain the capitalization of words used in the input file.  For example, "Happy" should be "Appyhay", not "appyHay".

  # 1. If a word starts with a consonant and a vowel, put the first letter of the word at the end of the word and add "ay."
    # Example: Happy = appyh + ay = Appyhay
  def oneConsonantConvert(self, word):
    # check to see if first letter is capitalized
    # if so, make so to capitalize the new first letter 
    firstLetter = word[0:1]

    newWord = word[1:]
    newWord = newWord + firstLetter.lower() + "ay."

    # Captialize the new first letter if the original first letter was upper
    if (firstLetter.isupper()):
      letterList = list(newWord)
      letterList[0] = letterList[0].upper()
      newWord = "".join(letterList)
    
    return newWord

  
  # 2. If a word starts with two consonants move the two consonants to the end of the word and add "ay."
    # Example: Child = Ildch + ay = Ildchay
  def twoConsonantConvert(self, word):
    firstTwoLetters = word[0:2]

    newWord = word[2:]
    newWord = newWord + firstTwoLetters.lower() + "ay."

    # Captialize first letter if needed
    letterList = list(newWord)
    if (firstTwoLetters[0].isupper()):
      letterList[0] = letterList[0].upper()
    # Captialize second letter if needed
    if (firstTwoLetters[1].isupper()):
      letterList[1] = letterList[1].upper()

    newWord = "".join(letterList)
    
    return newWord
    
  def vowelConvert(self, word):
    # 3. If a word starts with a vowel add the word "way" at the end of the word.
    # Example: Awesome = Awesome +way = Awesomeway

    newWord = word + "way"
    
    return newWord

  
  
  
  
# main function should use argparse
  # should have a default output file if none was specified
    # use out.txt as the default
  
    # 1. The code must use the Python argparseLinks to an external site. library to parse command-line arguments and select the input text file. Include an optional argument for the user to specify the name of output file, and if not specified, use out.txt as a default. An example execution would be:
  
    # python3 piglatin.py --input data.txt --output data_out.txt
  
  # 4. The output file must retain all of the punctuation used in the input text file, including whitespace, quotation marks, periods, newlines, and numbers. 
    # find out if readlines preserves whitespace

def main():
  PigLatin().fileLatinify("data.txt")

main()