Maximal Palindromic Factorisation 
=======

by Winston Lao
-----------

This program finds a maximal palindromic factorisation of s is the minimum number of concatenations of elements in the
factorisation set to be equivalent to s. The factorisation set of s is all the centre-distinct maximal palindromes in a 
string s. Furthermore, this project aims to allow centre-distinct maximal
palindromes in DNA and RNA, where the reversal of palindromes combines with the complementary
nucleotides, to be the factorisation set of s.

To test you string or list of string, add you list of strings to the user_data in the test_set.py file. If you are checking
for palindromes that use a complementary character, such as in DNA and RNA, add you dictionary to user_comp_dict in the test_set.py file.
To create a dictionary you add the character as the key and the complementary character as the value in a list, this 
allows for multiple complementarity characters in a list. 

for example: 
{
    "A": ["T", "U"],
    "G": ["C"],
    "C": ["G"],
    "T": ["A"],
    "U": ["A"]
}


When you have set up the lists and dictionary you will run the main function, if it returns none, then no MPF exist other it will return a list of 
centre-distinct maximal palindromes that is equivalent to the string s.
The program will calculate the MPF one by one in series. 

The program runs on Python 3.8