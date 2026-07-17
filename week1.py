# Task 1: Hello

# Write a hello function that takes no arguments and returns Hello!.  Now, what matters here is what the function returns.  You can print() whatever you want for debugging purposes, but the tests ignore that, and only check the return value.

print("Hello")

# Task 2: Greet with a Formatted String
# Write a greet function.  It takes one argument, a name, and returns Hello, Name!.  Use a formatted string.  Note that you have to return exactly the right string or the test fails -- but PyTest tells you what didn't match.

#used fstring to format with interpolation. To specify a string as an f-string, simply put an f in front of the string literal
def greet(name):
    message = f"Hello {name}."
    print(message)

greet("Faith")

# Task 3: Calculator
# Write a calc function. It takes three arguments. The default value for the third argument is "multiply". The first two arguments are values that are to be combined using the operation requested by the third argument, a string that is one of the following add, subtract, multiply, divide, modulo, int_divide (for integer division) and power. The function returns the result.
# Error handling: When the function is called, it could ask you to divide by 0. That will throw an exception: Which one? You can find out by triggering the exception in your program or in the Python Interactive Shell. Wrap the code within the calc function in a try block, and put in an except statement for this exception. If the exception occurs, return the string "You can't divide by 0!".
# More error handling: When the function is called, the parameters that are passed might not work for the operation. For example, you can't multiply two strings. Find out which exception occurs, catch it, and return the string "You can't multiply those values!".


# Tip: You have to do different things for add, multiply, divide and so on. So you can do a conditional cascade, if/elif/elif/else. That's perfectly valid. But you might want to use the match-case Python statement instead.
# Again, as you complete each function, you run the test to see whether everything is correct.

#psuedo code
#we want a calculator function that has 3 paramters: two for values, and one that represents the operation we want done.
#this operation will be specified as an argument when we call the function (ex: calc("add)")), which will use our parameters to return a result
  # this string can be add, subtract, multiply, divide, modulo, int_divide (for integer division) and power.
#so within our function, we want to address each of these potential operation with an if else
    # if the operation parameter = "mutliply" then do this, if, = "add" then do this, and so on.

#Note: the try goes within the function before the operations being executed


def calc(value1, value2, operation="multiply"):
    try:
        if operation == "multiply":
            return value1 * value2

        elif operation == "add":
            return value1 + value2

        elif operation == "subtract":
            return value1 - value2

        elif operation == "divide":
            return value1 / value2

        elif operation == "modulo":
            return value1 % value2

        elif operation == "int_divide":
            return value1 // value2

        elif operation == "power":
            return value1 ** value2

        else:
            return "Error: Invalid operation."

    except ZeroDivisionError:
      return "Error: You can't divide by 0!"

    except TypeError:
      return "Error: unsupported operand type(s)"

print(calc("aper","lala","divide"))
# print(calc(5,6,"multiply"))
# print(calc(5,6,"add"))
# print(calc(5,6,"subtract"))
# print(calc(5,6,"divide"))
# print(calc(5,6,"modulo"))
# calc(5,6,"int_divide")
# calc(5,6,"power")




#First Attempt:
# def calc(value1,value2, multiply):
#     if multiply == "multiply":
#       return value1 * value2
#     elif multiply == "add":
#       return value1 + value2
#     elif multiply == "subtract":
#       return value1-value2
#     elif multiply == "divide":
#       return value1/value2
#     elif multiply == "modulo":
#       return value1 % value2
#     elif multiply == "int_divide":
#       int_divide = (value1/value2)
#       return int(int_divide)
#     elif multiply == "power":
#       return value1**value2

# try:
#  result = 10 / 0
# except ZeroDivisionError:
#    print("Error: You can't divide by 0!")


# Task 4: Data Type Conversion
# Create a function called data_type_conversion. It takes two parameters, the value and the name of the data type requested, one of float, str, or int. Return the converted value.
# Error handling: The function might be called with a bad parameter. For example, the caller might try to convert the string "nonsense" to a float. Catch the error that occurs in this case. If this error occurs, return the string You can't convert {value} into a {type}., except you use the value and data type that are passed as parameters -- so again you use a formatted string.

def data_type_conversion(value,type):
  try:
    match type:
        case "float":
            print(float(value))
        case "str":
            print(str(value))
        case "int":
            print(int(value))
  except ValueError:
    print(f"Invalid literal for int(): You can't convert {value} into a {type}")

data_type_conversion("lala","int")

# Task 5: Grading System, Using *args

# Create a grade function. It should collect an arbitrary number of parameters, compute the average, and return the grade. based on the following scale, popular in American schools:

# A: 90 and above
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60

# When you use *args you get access to a variable named args in your function, which is a tuple, an ordered collection of values like a list. You'll learn more about tuples and lists in the next lesson. There are some helpful functions you can use at this point: sum(args), len(args), and so on. One of the curiosities of Python is that these are not methods of any class. They are standalone functions.

# Handle the error that occurs if the parameters are nonsense.
# Return the string "Invalid data was provided." in this case. Typically, you don't handle every possible exception in your error handling, except if the values in the parameters come from the end user.)

#compute the avergage by adding up all of the numbers, and dividing by the total number of values
#using a for loop helps address the issue from first attempt

def grade(*args):
    try:
        for score in args:    # for every value in args, the tuple, if the score is <0 or >100...
            if score < 0 or score > 100:
                return "Grade entered is not between 0 and 100"

        return sum(args) / len(args)  #otherwise complete the calculation

    except TypeError:
        return "Type Error: Invalid data was provided."


#call the function
print(grade(1,2,3,4))  #output is 2.5
print(grade(81,90,98,100)) #output is 92.25
# grade(101,0,52) #Not in range response
# grade("hey", "this", "is", "invalid", "syntax") #invalid syntax: type error



#First Attempt: the code worked but I wanted to add an conditional that would check if any numerical data was within the typical grade scale (0-100), assuming extra credit is entered as a seperate score.
#after adding the conditional, the if statement would only return the error handling message.
# def grade(*args):
#   try:
#     if args>= 0 and args <=100:
#       return sum(args)/len(args)
#     else:
#       print("Grade entered is not between 0 and 100")

#   except TypeError:
#     print("Type Error: Invalid data was provided.")




# Task 6: Use a For Loop with a Range

# Create a function called repeat. It takes two parameters, a string and a count, and returns a new string that is the old one repeated count times.
# You could return string * count to pass the test — but for this task, use a for loop and a range.

# Using range to loop a specific number of times
# range(stop) where stop is greater than the last number generated
# range(start, stop) starts with a number other 0
# range(start, stop, step) uses the specified step size instead of 1

def repeat(string, count):     #word acts as a loop counter, so it means "for every loop"
  for word in range(count):   #count is being used as a paramter for the number of times we want to repeat, so its the range because we want to repeat *count* times and it will stop when we reach that count
    print(string)

repeat("hello world", 5)

# Task 7: Student Scores, Using **kwargs

# Create a function called student_scores. It takes one positional parameter and an arbitrary number of keyword parameters. The positional parameter is either "best" or "mean".

# - If it is "best", the name of the student with the highest score is returned.
# - If it is "mean", the average score is returned.

# As you are using **kwargs, your function can access a variable named kwargs, which is a dict. The next lesson explains about dicts. What you need to know now is the following:

# - A dict is a collection of key value pairs.

# - You can iterate through the dict as follows:
#   - for key, value in kwargs.items:
#   - You can also get kwargs.keys() and kwargs.values().
#   - The arbitrary list of keyword arguments uses the names of students as the keywords and their test score as the value for each.

def student_scores(positional, **kwargs):
  highest_score = 0
  best_student = ""

  for name, score in kwargs.items(): # for every key,value in the dict,
    if score > highest_score:       #if the score, the value, is higher than the highest score (starting at 0), assign that value to highest score and so on
        highest_score = score
        best_student = name         #the key for each value will also be updated to the variabl name

  if positional == "best":
    return best_student, highest_score
  elif positional == "mean":                #an if conditional is used insetad of elif or else because this condition is not based on the other
    return sum(kwargs.values())/len(kwargs.values())


print(student_scores("mean", student1 = 25, student2 = 50, student3= 75, student4 = 100))

#First Attempt: value() --> values() and theres no need for a for loop, plus putting return within the for loop keys it from strarting the next iteration
# def student_scores(positional, **kwargs):  #**kwargs is the arbitrary number of keyword parameters
#   for value in kwargs.items():  #iterate through the dictionary
#     if positional == "best":
#       return max(kwargs.values())
#     if positional == "mean":
#       return sum(kwargs.values())/len(kwargs.values())

# student_scores("mean", student1 = 25, student2 = 50, student3= 75, student4 = 100)



# Task 8: Titleize, with String and List Operations

# Create a function called titleize. It accepts one parameter, a string. The function returns a new string, where the parameter string is capitalized as if it were a book title.

# The rules for title capitalization are:
# (1) The first word is always capitalized.
# (2) The last word is always capitalized.
# (3) All the other words are capitalized, except little words. For the purposes of this task, the little words are "a", "on", "an", "the", "of", "and", "is", and "in".

# The following string methods may be helpful: split(), join(), and capitalize().

# The split() method returns a list. You might store this in the words variable. words[-1] gives the last element in the list.

# The in comparison operator: You have seen in used in loops. But it can also be used for comparisons, for example to check to see if a substring occurs in a string, or a value occurs in a list.

# Useful pattern: As you loop through the words in the words list, it is helpful to have the index of the word for each iteration. You can access that index using the enumerate() function:


#psuedocode: return a new string where the argument has been capitalized like a book title.
#turn the string into a concatenated array, suing the split() method
#capitalize the first and last word
#then join them back together

def titleize(str):
    split = str.split()   #turns it into a list
    for i in range(len(split)):     #for every iteration over the range of the length of our split list, len(split) tells us the num of objects in the list
      if len(split[i]) >= 3:        #len(split[i]), the i represents the index of each word, of the word at that index is >= 3, then
        split[i] = split[i].capitalize()  #reassign the value at that index to the capitalized version

    return  " ".join(split)     #outside the loop, we join the list back into a string and return it




print(titleize("hello hey"))




# Task 9: Hangman, with more String Operations

# Create a function hangman. It takes two parameters, both strings, the secret and the guess.

# The secret is some word that the caller doesn't know. So the caller guesses various letters, which are the ones in the guess string.

# A string is returned. Each letter in the returned string corresponds to a letter in the secret, except any letters that are not in the guess string are replaced with an underscore. The others are returned in place. Not everyone has played this kid's game, but it's common in the US.

# Example: Suppose the secret is "alphabet" and the guess is "ab". The returned string would be "a___ab__".

# Note that Python strings are immutable. That means that the following code would give an error:

# secret = "alphabet"
# secret[1] = "_"

# On the other hand, you can concatenate strings with the + operator.

# psuedo code:

#create an empty string to store the answer

# for every letter in secret:
#     if letter is in guess:
#         add the letter to the answer
#     else:
#         add "_" to the answer

# return the answer

def hangman(secret, guess):
  answer = ""

  for letter in secret:
    if letter in guess:
      answer += letter

    else:
      answer += "_"

  return answer


print(hangman("python","pt"))

# Task 10: Pig Latin, Another String Manipulation Exercise

# Pig Latin is a kid's trick language. Each word is modified according to the following rules.
#  (1) If the string starts with a vowel (aeiou), "ay" is tacked onto the end.

#  (2) If the string starts with one or several consonants, they are moved to the end and "ay" is tacked on after them.
#  (3) "qu" is a special case, as both of them get moved to the end of the word, as if they were one consonant letter.

# Create a function called pig_latin. It takes an English string or sentence and converts it to Pig Latin, returning the result. We will assume that there is no punctuation and that everything is lower case.

def pig_latin(sentence):
    result = []

    for word in sentence.split():
        if word[0] in "aeiouAEIOU":
            result.append(word + "ay")
        else:
            result.append(word[1:] + word[0] + "ay")

    return " ".join(result)

print(pig_latin("apple pie"))



# def pig_latin(sentence):
#   translate = sentence.split()  #this is a list (array) of the string
#   for i in range(len(translate)):
#     if translate[i][0] in "aeiouAEIOU":   #if the i string index's, first letter index has one of these letters
#       translate[i].append("ay")
#     return "".join(translate)

#   else:
#     translate.append(translate[0], "ay")
#     translate.pop(0)
#   return "".join(translate)



# pig_latin("apple pie")
