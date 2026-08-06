#replace() method replaces a specified phrase with another specified phrase.
string= "she is beautiful and she is good dancer"
# print(string.replace("is","was",1))
#find() method finds a specified phrase and returns the position of where it was found
# print(string.find("is"))
is_pos1= string.find("is") #first occurrence
is_pos2= string.find("is", is_pos1+1) #second occurrence
print(is_pos2)