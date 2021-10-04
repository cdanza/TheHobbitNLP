import nltk
from Preprocess import full_preprocess, lemmatizer, clean_file, lemmatizer_verify
from Figures import word_hifreq_chart, word_lofreq_chart

"""
Unsure if downloads below need to be run locally >1 time
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
"""

# Opening and reading the file
f = open('/Users/cdanza/Documents/Coding/The Hobbit NLP Project/TheHobbit.txt','r', encoding='utf8')
raw = f.read()


# Still testing, but will possibly remove: Tokenization, cleaning, lemmatizing in that order -> problem due to stopwords created post-lemma
# New idea to create functions for each step, then apply in whichever order chosen
wordtokenized3 = nltk.word_tokenize(raw)
clean_corpus = clean_file(wordtokenized3)
lemmatized_corpus = lemmatizer(clean_corpus)

# Still testing -> adverbs not always lemmatizing
fullpreprocess = full_preprocess(raw)

lemmatizer_verify('quick', 'quickly', lemmatized_corpus, fullpreprocess)

# Get charts
#word_hifreq_chart(fullpreprocess)
#word_hifreq_chart(lemmatized_corpus)
#word_lofreq_chart(lemmatized_corpus)


"""
Future directions:
    Bilbo word count over time.
    Bilbo sentiment over time.
    Bilbo interactions with Gandalf/Dwarfs over time.
    Ring count over time.
    Ring sentiment over time.
"""