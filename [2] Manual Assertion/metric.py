import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# read the Excel file and load it into a pandas DataFrame
df = pd.read_excel('path/to/file.xlsx')

# define the list of stopwords to remove
stop_words = set(stopwords.words('english'))

# define the most common themes
themes = ['theme1', 'theme2', 'theme3']

# define a dictionary to keep track of sentiment scores for each theme
sentiments = {t: 0 for t in themes}

# iterate through each cell in the Excel file
for index, row in df.iterrows():
    # check if the cell contains the number 1
    if '1' in str(row):
        # extract the content after the number 1 and before the number 2
        content = str(row).split('1')[1].split('2')[0]
        # tokenize the content
        tokens = word_tokenize(content.lower())
        # remove stop words
        filtered_tokens = [token for token in tokens if token not in stop_words]
        # calculate sentiment scores for each theme
        for theme in themes:
            if theme in filtered_tokens:
                sentiments[theme] += 1

# print the sentiment scores for each theme
for theme, score in sentiments.items():
    print(f"{theme}: {score}")


#################### 1-20  MANUAL STATS CATEGORIZATION ########################

# Education 1A 1D 7A 9A 10A 18A 19A 4B (8) +30 >38
# Mental Health 3A 6A 8A 11A 12A 13A 16A 17A 5B 12B (10) +25 >35
# Food 20A 6B (2) +20 >22
# Transportation 4A 14A 15A 2B 8B (5) +15 >20
# Activites 1B 3A 1B (3) +10 >13
# Housing 10B (1) +20 > 21
# Technology 3B (1) +10 > 11
# Infrastrtucture 7B (1) +15 >16
# Holidays 9B (1) +5 >6
# Administration 11B (1) +12 > 13 
# Security 1
# Sports 4