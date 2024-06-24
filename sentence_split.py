list_sentences =[
"I want to buy a car",
"She needs to play piano ",
"They don't have to read books",
"Do we need to go ?",
"We want to go to the park but my friend needs to visit her grandma ",
"I need to dance more because I want to be fit",
"John has to play piano every day because he needs to practice ",
"I have to tell you something ",
"He doesn't want to go shopping ",
"I want to get up at 6 and my brother wants to sleep ",
"They have to come to the party so we need to buy more cake",
"Do we want to go to the swimming pool ?",
"My mom and I want to go to the theatre so we need to go to bed early ",
"Does she have to cook breakfast because her mom wants to sleep more ?",
"I don't like to sing",
"Tom likes to play football with friends ",
"Does Sara want to eat a cake ?",
"My friends like to read books and I like to ride a bike ",
"She likes to cook on Fridays ",
"Does Lily need to pay for a taxi ?",
]
list_words = []

for sentence in list_sentences:
    words = sentence.split()
    for word in words:
        # print(word)
        # print(words)
        word = word.lower()
        if word == "," or word == "." or word == "?":
            continue
        if not word in list_words:
            list_words.append(word)
result = '\n'.join(list_words)        
print(result)

# my_input = input('insert sentences')
# print(my_input)
# def separator(my_input: list):
#     list_sentences =list_sentences
#     list_words = []

#     for sentence in list_sentences:
#         words = sentence.split()
#         for word in words:
#             print(word)
#             print(words)
#             if not word in list_words:
#                 list_words.append(word)
#     result = '\n'.join(list_words) 
#     return result   
# ready_words = separator()  
# print(ready_words)
