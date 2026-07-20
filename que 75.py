def bag_of_words(sentences):
    vocabulary =[]
    
    for sentence in sentences:
        words =sentence.split()

        for word in words:
            if word  not in vocabulary:
                vocabulary.append(word)
    
    vectors =[]

    for sentence in sentences:
        words =sentence.split()
        vector=[]

        for word in vocabulary:
            vector.append(words.count(word))
        
        vectors.append(vector)


    return vocabulary,vectors

sentences=[
     "I love python",
    "I love coding",
    "python is easy"

]

vocab,vectors = bag_of_words(sentences)
print("Vocabulary: ",vocab)
print("Vectors:")

for v in vectors:
    print(v)