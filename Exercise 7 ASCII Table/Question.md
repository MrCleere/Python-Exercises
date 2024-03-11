ASCII stands for American Standard Code for Information Interchange. 

Computers can only store numbers, so each letter, numeral, punctuation mark, and every other character is assigned a number called a code point. ASCII was a popular standard mapping of text characters to numbers. For example, 'Hello' would be represented by 72, 101, 108, 108, 111. 

Specifically, computers only store the ones and zeros of binary numbers. These decimal numbers translate to 01001000, 01100101, 01101100, 01101100, 01101111 in binary. 

An ASCII table showed all the characters and their assigned ASCII number values.

However, ASCII is an old and somewhat limited standard: 

It doesn’t have numbers assigned for Cyrillic or Chinese characters, for example. 

It is an American standard: it has a code point for the dollar sign (code point 36) but not the British pound sign.

ASCII is no longer enough now that the internet has made global communication commonplace. 

The newer Unicode character set provides code points for every character and is what Python uses for its string values. Unicode’s code points are backward compatible with ASCII, so we can still easily use Python to display an ASCII table.

In this exercise you’ll learn how to use the ord() and chr() functions to translate between integers and text characters.

# Exercise Description

Write a printASCIITable() function that displays the ASCII number and its corresponding text character, from 32 to 126. (These are called the printable ASCII characters.)

Your solution is correct if calling printASCIITable() displays output that looks like the following:

32 

33 !

34 "

35 #

--more--

124 |

125 }

126 ~

Note that the character for ASCII value 32 is the space character, which is why it looks like nothing is next to 32 in the output.
