Find-and-replace is a standard feature in text editors, IDEs, and word processor software. 

Even the Python language comes with a replace() string method since programs often use it. In this exercise, you’ll reimplement this common string operation.


Exercise Description

Write a findAndReplace() function that has three parameters: text is the string with text to be replaced, oldText is the text to be replaced, and newText is the replacement text. Keep in mind that this function must be case-sensitive: if you are replacing 'dog' with 'fox', then the 'DOG' in 'MY DOG JONESY' won’t be replaced.

These Python assert statements stop the program if their condition is False. Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ conditions are all True:

assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'

assert findAndReplace('fox', 'fox', 'dog') == 'dog'

assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'

assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'

assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'



