"""
People do not like reading text in which a word is used multiple times in a short paragraph. 
You are to write a program which helps identify such a problem.

Write a program which takes as input an array and finds the distance between a closest pair of equal entries. 
For example, if s = ["All", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun","and", "no" "results"], 
then the second and third occurrences of "no" is the closest
Pair.
Hint:Each entry in the array is a candidate.

"""
# Had trouble understanding this question when I read it the first time.

# What is essentialy asking is to find the two nearest duplicated neighbors; In theis case similar words that are occuring close together.

array = ["All", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun","and", "no" "results"]

# Always assume valid inputs
def find_the_nearest_word_in_array(arr):
    word_counter , nearest_distance_btwn_similar_words = {}, float('inf')

    for i, word in enumerate(arr):
        if word in word_counter:
            latest_idx = word_counter[word]
            nearest_distance_btwn_similar_words = min(nearest_distance_btwn_similar_words, i - latest_idx)

        word_counter[word] = i

    return nearest_distance_btwn_similar_words if nearest_distance_btwn_similar_words != float('inf') else -1

print('Find the nearest word in the array:', find_the_nearest_word_in_array(array))
another_array = ["hello", "hello", "world", "world", "world", "hello"]
print(find_the_nearest_word_in_array(another_array))
another_one = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "the"]
print(find_the_nearest_word_in_array(another_one))
another_two =  ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
print(find_the_nearest_word_in_array(another_two))
