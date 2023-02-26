import csv
def Write():

    f=open('Hangman.csv','a',newline='')
    cw=csv.writer(f)
    name=input('Enter your Name ⊂(◉‿◉)つ')
    phno=input('Enter your Phone Number ⊂(◉‿◉)つ')
    lid=input('Enter Login Id ⊂(◉‿◉)つ')
    passwd=input('Enter Password ⊂(◉‿◉)つ')
    cw.writerow([name,phno,lid,passwd])
    f.close()

def Read(logid,paswd):

    f=open('Hangman.csv')
    cr=csv.reader(f)
    for i in cr:
        if i[2]==logid:
            global z
            z=1
            if i[3]==paswd:
                global x
                x=1
                print('******************************************************************')
                print('\t\t\t\t\t            --WELCOME--')
                print('********** ********************************************************')
                import random
                from words import word_list


                def get_word():
                    word = random.choice(word_list)
                    return word.upper()


                def play(word):
                    word_completion = "*" * len(word)
                    guessed = False
                    guessed_letters = []
                    guessed_words = []
                    tries = 6
                    print("Let's play Hangman!☜☆☞ ")
                    print(display_hangman(tries))
                    print(word_completion)
                    print("\n")
                    while not guessed and tries > 0:
                        guess = input("Please guess a letter or word☜☆☞  ").upper()
                        if len(guess) == 1 and guess.isalpha():
                            if guess in guessed_letters:
                                print("You already guessed the letter(¬_¬)", guess)
                            elif guess not in word:
                                print(guess, "is not in the word ︶︿︶")
                                tries -= 1
                                guessed_letters.append(guess)
                            else:
                                print("Good job,", guess, "is in the word! ⊂(◉‿◉)つ")
                                guessed_letters.append(guess)
                                word_as_list = list(word_completion)
                                indices = [i for i, letter in enumerate(word) if letter == guess]
                                for index in indices:
                                    word_as_list[index] = guess
                                word_completion = "".join(word_as_list)
                                if "*" not in word_completion:
                                    guessed = True
                        elif len(guess) == len(word) and guess.isalpha():
                            if guess in guessed_words:
                                print("You already guessed the word (¬_¬)", guess)
                            elif guess != word:
                                print(guess, "is not the word.")
                                tries -= 1
                                guessed_words.append(guess)
                            else:
                                guessed = True
                                word_completion = word
                        else:
                            print("Not a valid guess.")
                        print(display_hangman(tries))
                        print(word_completion)
                        print("\n")
                    if guessed:
                        print("Congrats, you guessed the word! You win! ▄︻̷̿┻̿═━一")
                    else:
                        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
                def display_hangman(tries):
                    stages = [  # final state: head, torso, both arms, and both legs
                                """
                                   --------
                                   |      |
                                   |      O
                                   |   \|/
                                   |      |
                                   |    / \
                                   -
                                """,
                                # head, torso, both arms, and one leg
                                """
                                   --------
                                   |      |
                                   |      O
                                   |   \|/
                                   |      |
                                   |     / 
                                   -
                                """,
                                # head, torso, and both arms
                                """
                                   --------
                                   |      |
                                   |      O
                                   |   \|/
                                   |      |
                                   |      
                                   -
                                """,
                                # head, torso, and one arm
                                """
                                   --------
                                   |      |
                                   |      O
                                   |   \|
                                   |      |
                                   |     
                                   -
                                """,
                                # head and torso
                                """
                                   --------
                                   |      |
                                   |      O
                                   |      |
                                   |      |
                                   |     
                                   -
                                """,
                                # head
                                """
                                   --------
                                   |      |
                                   |      O
                                   |    
                                   |      
                                   |     
                                   -
                                """,
                                # initial empty state
                                """
                                   --------
                                   |      |
                                   |      
                                   |    
                                   |      
                                   |     
                                   -
                                """
                    ]
                    return stages[tries]


                def main():
                    word = get_word()
                    play(word)
                    while input("Play Again? (Y/N) ").upper() == "Y":
                        word = get_word()
                        play(word)
                        
                
                if __name__ == "__main__":
                    main()

                break
            else:
                print('\t\t\t\t\t ●_● INCORRECT PASSWORD ●_●')

def Display():
    
    f=open('Hangman.csv')
    cr=csv.reader(f)
    for i in cr:
        print(i)
    print()

restart='y'                
while restart.lower()!='a':
    print('1.☞Already have an account☜.\n2.☞Create new account☜\n3.☞Details of Users *For Admin Access Only*☜\n4.☞Exit☜')
    print('\t\t\t     ------------------------------------------------------')
    print()
    choice=int(input('Enter your choice:\t'))
    print()

    while choice not in [1,2,3,4]:
        print('-------------------------------------------------------------●_● INVALID CHOICE ●_●-------------------------------------------')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print()
        choice=int(input('Enter your choice:\t'))

    if choice==1:
        logid=input('Enter Login Id :-) \t')
        paswd=input('Enter Password :-) \t')
        x=3
        z=3
        Read(logid,paswd)
        while z!=1:
            print('----------------------------------X \t X \t X \t ●_● INVALID LOGIN ID  ●_● \t X \t X \t X \t-------------------------------')
            logid=input('Enter Login Id:\t')
            paswd=input('Enter Password:\t')
            Read(logid,paswd)
        while  x!=1:
            paswd=input('Enter Password:\t')
            Read(logid,paswd) 
    if choice==2:
        Write()
        print('--------------------------------------------------^_^ Account Created Successfully ^_^----------------------------------------------')
        print()

    if choice==3:
        p='sourabhkaraj'
        while True:
            q=input('Enter Password:\t')
            if q==p:
                print()
                Display()
                break
            else:
                print('---------------------------------------------------●_●INCORRECT PASSWORD ●_●---------------------------------------------')
    if choice==4:
        print('#######################################')
        print('***************************************')
        print('*                          THANK YOU FOR PLAYING                              *')
        print('*                                                                                                               *')
        print('*                           PROJECT BY:-                                                       *')
        print('*                           SOURABH KHERA                                              *')
        print('*                           12 A                                                                           *')
        print('*                           ROLL NO:- 37                                                        *')
        print('#######################################')
        print('***************************************')
        break

               
