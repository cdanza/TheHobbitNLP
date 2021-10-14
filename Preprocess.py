import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

wnl = WordNetLemmatizer()

# Adding stopwords based on initial hi_freq_chart viewing
stopwords = nltk.corpus.stopwords.words('english')
custom_stopwords = ['say', 'get', 'one', 'could', 'like']
stopwords.extend(custom_stopwords)

# -----------------------------------------------------------------------------------------------

# Each cleaning task separated by function
# Adverbs still not lemmatizing.
def remove_punct(file) -> list:
    r = [word for word in file if word.isalnum()]
    
    return r

def to_lowercase(file) -> list:
    l = [word.lower() for word in file]
    
    return l

def remove_stopwords(file) -> list:
    rs = [word for word in file if word not in stopwords]
    
    return rs

def lemmatize(file):
    
    # Pos tagger function
    def pos_tagger(nltk_tag):
    	if nltk_tag.startswith('J'):
    		return wordnet.ADJ
    	elif nltk_tag.startswith('V'):
    		return wordnet.VERB
    	elif nltk_tag.startswith('N'):
    		return wordnet.NOUN
    	elif nltk_tag.startswith('R'):
    		return wordnet.ADV
    	else:		
    		return None
    
    # Find the pos tag for each token
    pos_tagged = nltk.pos_tag(file)
    
    
    # Use our made pos_tagger to simplify
    wordnet_tagged = list(map(lambda x: (x[0], pos_tagger(x[1])), pos_tagged))
    
    lemmatized_corpus = []
    
    for word, tag in wordnet_tagged:
        if tag is None:
    		# If there is no available tag, append the token as is
            lemmatized_corpus.append(word)
        # This doesn't seem to work, theres' still 32 dwarves occurrences
        elif tag == "dwarves":
            lemmatized_corpus.append("dwarf")
        else:	
    		# else use the tag to lemmatize the token
            lemmatized_corpus.append(wnl.lemmatize(word, tag))
            
    # Line below recreates one string out of list        
    #lemmatized_corpus = " ".join(lemmatized_corpus)
    
    return lemmatized_corpus

# -----------------------------------------------------------------------------------------------

# Load in 2 strings to compare, then 2 lists to compare relative string count pre- and post- lemmatization
def lemmatizer_verify(w, x, y, z):
    y_count_w = 0
    y_count_x = 0
    for item in y:
        if item == w:
            y_count_w += 1
        if item == x:
            y_count_x += 1
    print("List1_", w, "=", y_count_w)
    print("List1_", x, "=", y_count_x)
    print("Total", w, "+", x, "in List1 = ", y_count_w + y_count_x)
    
    z_count_w = 0
    z_count_x = 0
    for item in z:
        if item == w:
            z_count_w += 1
        if item == x:
            z_count_x += 1
    print("List2_", w, "=", z_count_w)
    print("List2_", x, "=", z_count_x)
    print("Total", w, "+", x, "in List2 = ", z_count_w + z_count_x)
    
    return


