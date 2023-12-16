!sudo apt-get install libhunspell-dev
!pip install hunspell

import hunspell

# Path to the Hindi dictionary and affix files. Replace with the actual paths where you have stored these files.
hindi_dic_path = '/content/hi_IN.dic'
hindi_aff_path = '/content/hi_IN.aff'

# Initialize the Hunspell spellchecker for Hindi
spellchecker = hunspell.HunSpell(hindi_dic_path, hindi_aff_path)

# List of Hindi words to check
words_to_check = ['समाचार', 'चाय', 'सूरज','चायी','पुस्तल','फूली','पाणी','राती']  # Add more Hindi words here

# Function to check spelling of a word
def check_spelling(word):
    if spellchecker.spell(word):
        return f"'{word}' is spelled correctly in Hindi."
    else:
        suggestions = spellchecker.suggest(word)
        return f"'{word}' might be misspelled in Hindi. Suggestions: {suggestions}"

# Check the spelling of each word in the list
for word in words_to_check:
    result = check_spelling(word)
    print(result)
