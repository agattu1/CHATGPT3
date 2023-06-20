# How to Run

- run `python catergorize.py` in a setup python 3 environment
- ensure test1.csv is in the same folder as the python script.
- This program will sort the responses based on 6-10 or 1-5.
- Line 32 must be edited to <6 for 1-5 or >5 for 6-10
- Responses will be printed in the console, which can be copied, or standard console can be piped into a csv automatically (i.e. `python catergorize.py >> after.csv` in Unix)

# after.csv

- contains responses labeled 1-5

# before.csv

- contains responses labeled 6-10

# test1.csv

- data sorted by ChatGPT with the number of the suggestion
