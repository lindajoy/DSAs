"""
This question I came up with after recieving a take away assignment.
Given a list 
INPUT:
["Alex",Beatrice,101.32,
Beatrice,Alex,1.20,
Beatrice,Alex,4.54,
Beatrice,Carl,71.42,
eatrice,Carl,28.76,
] 

Generate the output such that it is:
Alex,Beatrice,120.54
Beatrice,Alex,5.74
Beatrice,Carl,168.08
Carl,Alex,60.88
Carl,Beatrice,25.30
"""
input = ["Alex","Beatrice",101.32,
"Beatrice","Alex",1.20,
"Beatrice","Alex",4.54,
"Beatrice","Carl",71.42,
"Beatrice","Carl",28.76,
] 

def generateOutput(lst):
    startIndex = 0
    concat_sliced_array = []

    while startIndex in range(len(lst)):
        sliced_array = lst[startIndex : startIndex+3]
        startIndex = startIndex + 3
        concat_sliced_array.append(sliced_array)

    for i in concat_sliced_array:
        combined_dict_array = []
        combined_dict_array.append(dict([("from" ,i[0]), ("to", i[1]), ("amount", i[2])]))

        total_sum = {}

        # if sorted_word not in my_anagram_dictionary.keys():
        #     my_anagram_dictionary.setdefault(sorted_word, []).append(i)
        # else:
        #     my_anagram_dictionary[sorted_word].append(i)
        for i in combined_dict_array:
            print(i)
            key = (i['from'] + i['to'])
            print(key)

            if key not in total_sum.keys():
                print(total_sum[key])
                total_sum[key] = float(i['amount'])
            else:
               print(total_sum[key])
               total_sum[key] += float(i['amount'])
        return total_sum


       
    # return combined_dict_array

    

print(generateOutput(input))

