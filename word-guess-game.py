import sys
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from random import seed
from random import randint
seed(1234)

def main():
    # check the argument
    if len(sys.argv) < 2 :
        print("Please enter the text filename as a argument")
        exit()
    elif len(sys.argv) > 2 :
        print("Please only provide one text filename as a argument")
        exit()

    # get the filemname
    file = sys.argv[1]
    print("The file is: " + file)

    # read the file and get the text
    with open(file, "r") as f:
        text = f.read()
    # print(text)
    
    # use nltk to get the tokens
    tokens = word_tokenize(text)

    # Process the text
    print(f"Lexical Diversity is: {cal_lexical_diversity(tokens):.2%}\n")

    preprocessed_tokens, nouns_lemmas= preprocess_text(text)

    most_common_50 = get_most_common_50(preprocessed_tokens, nouns_lemmas)
    # print(most_common_50)

    word_guess_game(most_common_50)


def word_guess_game(most_common_50):
    print("Let's play a word guessing game! (you can guess '!' as a letter to end the game)")
    # a. give the user 5 points to start with; the game ends when their total score is negative, or they guess ‘!’ as a letter
    score = 5

    while score > 0 :
        # b. randomly choose one of the 50 words in the top 50 list
        word_to_guess = most_common_50[randint(0, 49)]
        # print(word_to_guess)

        # c. output to console an “underscore space” for each letter in the word
        current_status = ["_"] * len(word_to_guess)
        print(" ".join(current_status))

        while "_" in current_status :
            # d. ask the user for a letter
            letter = input("Guess a letter: ")
            if(letter == "!") :
                print("You enter '!', exit the game")
                exit()
            elif not letter or letter.isspace() :
                if not letter : 
                    print("You didn't guess a letter, try again\n")
                else :
                    print("Space is invalid, please guess a letter\n")
                print(" ".join(current_status))
                continue
            elif len(letter) != 1 :
                print("Please guess only one letter at a time\n")
                print(" ".join(current_status))
                continue

            # e. if the letter is in the word, print ‘Right!’, fill in all matching letter _ with the letter and add 1 point to their score
            if letter in word_to_guess :
                if letter in current_status :
                    print("You have already guessed this letter, try another one\n")
                    print(" ".join(current_status))
                    continue
                score += 1
                print(f"Right! Score is {score}\n")
                for i in range(len(word_to_guess)) :
                    if letter == word_to_guess[i] :
                        current_status[i] = letter
            # f. if the letter is not in the word, subtract 1 from their score, print ‘Sorry, guess again’
            else :
                score -= 1
                # g. guessing for a word ends if the user guesses the word or has a negative score
                if score < 0 :
                    print("Sorry, you get a negative score, please restart the game")
                    exit()
                print(f"Sorry, guess again. Score is {score}")

            print(" ".join(current_status))
 
        print("You solved it!\n")
        print(f"Current score: {score}\n")
        print("Guess another word\n")
    
    return 0

def cal_lexical_diversity(tokens):
    return len(set(tokens)) / len(tokens)

def preprocess_text(text): 
    # tokenize the lower-case raw text
    tokens = word_tokenize(text.lower())    

    # reduce the tokens to:
    # 1. only those that are alpha
    # 2. not in the NLTK stopword list
    # 3. length > 5
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words and len(t) > 5]

    # lemmatize the tokens 
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens]

    # use set() to make a list of unique lemmas
    unique_lemmas = set(lemmas)
    unique_lemmas = list(unique_lemmas)     # convert from set back to a list 

    # do pos tagging on the unique lemmas and print the first 20 words and their tag
    tags = nltk.pos_tag(unique_lemmas)

    # create a list of only those lemmas that are nouns
    nouns_lemmas = [w for w, t in tags if t.startswith("NN")]  # NN, NNS, NNP, NNPS 
    
    # return (1) tokens (not unique tokens) from step a, and (2) nouns from the function
    return tokens, nouns_lemmas

def get_most_common_50(preprocessed_tokens, nouns_lemmas):
    # Make a dictionary of {noun:count of noun in tokens} items from the nouns and tokens lists
    noun_counts_dict = {noun: preprocessed_tokens.count(noun) for noun in nouns_lemmas}

    # Sort the dict by count and print the 50 most common words and their counts
    sorted_noun_counts_dict = sorted(noun_counts_dict.items(), key = lambda x: x[1], reverse = True)
    
    # Save these words to a list because they will be used in the guessing game.
    most_common_50 = [w for w, c in sorted_noun_counts_dict[:50]]

    return most_common_50


if __name__ == "__main__":
    main()