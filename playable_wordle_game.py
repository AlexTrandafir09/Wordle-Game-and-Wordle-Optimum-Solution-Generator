import random
L=[]
for word in (open("all_wordle_words.txt","r")).read().strip().split():
    L.append(word)
correct_word=random.choice(open('all_wordle_words.txt').read().split())
ok=0
word_count=0
colour_list=["X","X","X","X","X"]
while ok==0:
    ok_cases=1
    ok=1
    word_count+=1
    read_word=input(f"Try number {word_count} is: ")
    if read_word.isupper()==False:
        print("The word you enter can only be written in uppercase. Try again.")
        ok_cases=0
    if read_word.isalpha()==False:
        print("The word you enter can only contain letters.Try again.")
    if len(read_word)!=5:
        print("The word you enter can only be of length 5. Try again.")
        ok_cases=0
    if read_word not in L:
        print("The word you entered is not on the list.")
        ok_cases=0
    if ok_cases==1:
        for i in range (5):
            if read_word[i]==correct_word[i]:
                colour_list[i]="Green"
            elif read_word[i] in correct_word and read_word[i] !=correct_word[i]:
                        colour_list[i]="Yellow"
            else:
                colour_list[i]="Grey"

        for i in range(5):
            if colour_list[i]!="Green":
                ok=0
        if ok==1:
            print("You guessed correctly!")
            break
        else:
            print(*colour_list)

    else:

        ok=0
        word_count -= 1