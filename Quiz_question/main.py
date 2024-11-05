def import_questions(file):
    questions=[]
    with open(file, 'r') as file1:
        for line in file1:
            sentence=line.strip().split(',')
            question=sentence[0]
            options=sentence[1:5]
            answer= sentence[5]
            questions.append((question,options,answer))
    return questions

def show_question(question, options):
    print("\n"+question)
    for option in options:
        print(f" {option} ")
        
file='question.txt'
direct_questions=import_questions(file)
score=0
print("*** Please answer the questions by choosing only the options.***\n")
for question, options, answer in direct_questions:
    show_question(question, options)
    user_answer=input("Enter the option:").strip().upper()
    
    if answer==user_answer:
        score+=1
        print("Correct!")
    else:
        print("Wrong!")
print(f"\nYour final score is: {score}/10")
