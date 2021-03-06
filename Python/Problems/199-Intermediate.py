"""
[2015-1-26] Challenge #199 Bank Number Banners Pt 1 (self.dailyprogrammer)

submitted 3 days ago by professorlamp1 0 [H]
Description

You work for a bank, which has recently purchased an ingenious machine to assist in reading letters and faxes sent in by branch offices. The machine scans the paper documents, and produces a file with a number of entries which each look like this:

    _  _     _  _  _  _  _
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|

Each entry is 4 lines long, and each line has 27 characters. The first 3 lines of each entry contain an account number written using pipes and underscores, and the fourth line is blank. Each account number should have 9 digits, all of which should be in the range 0-9.

Right now you're working in the print shop and you have to take account numbers and produce those paper documents.
Input

You'll be given a series of numbers and you have to parse them into the previously mentioned banner format. This input...

000000000
111111111
490067715

Output

...would reveal an output that looks like this

 _  _  _  _  _  _  _  _  _
| || || || || || || || || |
|_||_||_||_||_||_||_||_||_|


 |  |  |  |  |  |  |  |  |
 |  |  |  |  |  |  |  |  |

    _  _  _  _  _  _     _
|_||_|| || ||_   |  |  ||_
  | _||_||_||_|  |  |  | _|

Notes

Thanks to /u/jnazario for yet another challenge!
"""

seven_segment = [
 " _     _  _     _  _  _  _  _ ",
 "| |  | _| _||_||_ |_   ||_||_|",
 "|_|  ||_  _|  | _||_|  ||_| _|"]

test_input = ["000000000", "111111111", "490067715"]

print_out = []
for numbers in test_input:
    for idx in range(0,3):
        line = ""
        for num in numbers:
            line += seven_segment[idx][int(num) * 3:int(num) * 3 + 3]
        print_out.append(line)

for x in print_out:
    print(x)
