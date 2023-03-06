
""" Inside str1, find str2. """
str1 = "Is it going well?" 
str2 = "it"
print(str1.find(str2))
#the program find the it in the position 3

str1 = "ociaociaociaociao"
print(str1.find("ciao"))
#the program returns 1 since is the first position where he can find OX

str1 = "parts"
str2 = "ps"
print(str1.find(str2))
#since we cannot find ps the program returns -1

test_string = "tested, testing, tests, test"
print(test_string.find("sted")) 

word = "embossed"
print(word[2:6])
# the program prints the substring boss

sentence = "I like rocks but they seem indifferent."
conjunction_index = sentence.find("but")
#conjunction_index = sentence.find(" but ")
left_side = sentence[0:conjunction_index] 
#left_side = sentence[0:conjunction_index-1] 
right_side = sentence[conjunction_index + 3:]
#right_side = sentence[conjunction_index + 4:]
classy_sentence = left_side + "yet" + right_side
print(classy_sentence)
