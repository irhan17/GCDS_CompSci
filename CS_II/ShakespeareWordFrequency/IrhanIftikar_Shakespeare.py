#Name: Irhan Iftikar
#Date: March 2024
#Description: Program that counts frequency of notable words in 2 Shakespeare plays using dictionaries
#Criteria: Meets all spec criteria
#Bonuses: All bonuses listed in spec are fulfilled (Uses Plotly to graph, sorts the dictionary)
#Bugs: No notable bugs found
#Sources: Various Internet Sources for Dictionary Syntax (w3schools, Stack Overflow, GeeksForGeeks, etc.) & Shakespeare Works Source: https://www.folger.edu/explore/shakespeares-works/download/

#Imports modules used in program
import plotly.express as px
from pathlib import Path

def find_path(file_path): 
    #Description: Function that finds file path & opens and sorts the data from the txt tile
    #parameters - file path name of .txt file
    #returns - a list of all the words in the .txt file
    current_dir = Path(__file__).parent
    path = current_dir / file_path
    file = open(path)
    data = file.read()
    words = data.split()
    index = 0
    for word in words:
        words[index] = word.lower() #Lowercases all the words in the .txt for easier processing
        index += 1
    return words

def frequency(words):
    #Description: Function that orders all words in .txt file by frequency and also gets rid of superfluous words in file
    #parameters - a list of all the words in the .txt file
    #returns - the clean dictionary file with 10 most frequent non-trivial words 
    frequency_dict = {}
    for word in words:  #Cycles through all the words and finds the frequency of each word
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    sorted_frequency_dict = dict(sorted(frequency_dict.items(), reverse=True, key=lambda x:x[-1]))  #Sorts values of dictionary in decreasing order
    #unwanted_characters is a list of all the superfluous terms that aren't important to the program
    unwanted_characters = ['the', 'and', 'to', 'of', 'i', 'a', 'that', 'in', 'my', 'is', 'you', 'with', 'his', 'not', 'be', 'it', 'your', 'our', 'have', 'but', 'he', 'for', 'this', 'all', 'what', 'as', 'we', 'which', 'me', 'so', 'do', 'will', 'they', 'th\'', 'are', 'upon', 'their', 'no', 'on', 'from', '[enter', 'him', 'at', 'by', 'yet', 'first', 'was', 'would', 'good', 'if', 'her', 'am', 'or', 'she', 'did', '[to', 'me,', 'thou', 'shall', 'hath', 'thy', 'should', 'when', 'like', 'were', 'make', 'how', 'had', 'come', 'them', 'great', 'know', 'say', 'may', 'thee', 'us', 'must', 'more', 'i\'ll', '\'tis', 'let', 'who', 'where', 'now', 'how', 'had', 'come', 'them', 'than', 'an', 'scene', '=======', 'second', '[they', 'exit.]', 'macbeth,', 'see', 'time', 'there', 'nor', 'me.', 'man', 'you,', 'see', 'some', 'then', 'here', 'go', 'one', 'home', 'us', 'till', 'where', 'these', 'syracuse,', 'come', 'may', 'more', 'now', 'make', 'them', 'tell']
    for word in unwanted_characters:
        if word in sorted_frequency_dict:
            del sorted_frequency_dict[word] #If the unwanted character exists in the dictionary, it deletes them
    converted_frequency_dict = dict(list(sorted_frequency_dict.items())[0: 10])  #Takes top ten key:value pairs from the sorted dictionary
    return converted_frequency_dict

def graphs(dictionary, choice):
    #Description: Function that creates a bar graph of the top 10 most important words and frequencies
    #parameters - the sorted dictionary and the choice of Shakespeare's play chosen by the user
    #returns - void
    keys = dictionary.keys()
    values = dictionary.values()
    graph_dictionary = {"Words": keys, "Quantity": values}
    fig = px.bar(graph_dictionary, x='Words', y='Quantity', title="Irhan Iftikar: Word Distribution of Shakespeare's {}: ".format(choice))
    fig.show()

def get_choice():
    #Description: Function that prompts the user for their choice of a Shakespeare play
    #parameters - void
    #returns - choice chosen by the user
    while True:
        choice = input("Select (1) for Macbeth and (2) for Comedy of Errors: ")
        if choice == "1":
            choice = 'Macbeth'
            return choice
        elif choice == "2":
            choice = 'Comedy of Errors'
            return choice
        else:
            print("Input not valid, try again.")

def main():
    #Description: Main function that executes the program by calling other functions
    #parameters - void
    #returns - void
    choice = get_choice()
    if choice == "Macbeth":
        words = find_path("macbeth.txt")
    elif choice == "Comedy of Errors":
        words = find_path("comedy_of_errors.txt")
    dictionary = frequency(words)
    graphs(dictionary, choice)

main() #Calls main function that executes the program