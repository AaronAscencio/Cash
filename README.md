# Cash
Implement a program that calculates the minimum number of coins required to give a user
change.
# Implementation Details
Write, in a file called cash.py, a program that first asks the user how much change is owed <br />
and then spits out the minimum number of coins with which said change can be made. <br /> 
Get the user’s input and print to output your answer. Assume that the only coins available are <br />
quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢). <br />
In other words, if some customer is owed $9.75 (as in the case where a newspaper costs 25¢ <br />
but the customer pays with a $10 bill), assume that your program’s input will be 9.75 and not <br />
$9.75 or 975. However, if some customer is owed $9 exactly, assume that your program’s <br />
input will be 9.00 or just 9 but, again, not $9 or 900. Of course, by nature of floating-point <br />
values, your program will likely work with inputs like 9.0 and 9.000 as well; you need not worry <br />
about checking whether the user’s input is &quot;formatted&quot; like money should be. <br />
If the user fails to provide a non-negative value, your program should re-prompt the user for a <br />
valid amount again and again until the user complies. <br />
Incidentally, so that we can automate some tests of your code, we ask that your program’s <br />
last line of output be only the minimum number of coins possible: an integer followed by a <br />
new line (i.e. print() line). <br />
Hint: Convert dollars to cents. <br />
# Usage
Your program should behave per the example below. Assume that the underlined text is what <br />
some user has typed: <br />
$ python cash.py <br />
Change owed: 0.41 <br />
4 <br />
# Testing
$ python cash.py <br />
Change owed: -0.41 <br />
Change owed: -0.41 <br />
Change owed: foo <br />
Change owed: 0.41 <br />
4 <br />
# How to run
' python cash.py '
