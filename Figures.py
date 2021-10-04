import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Create a high word count dataframe and then
def word_hifreq_chart(file) -> list:
    counter = Counter(file)
    count_df = pd.DataFrame(counter.most_common(10), columns=['Words', 'Count'])
    print(count_df)
    
    fig, ax = plt.subplots(figsize = (8, 8))
    count_df.sort_values(by = 'Count').plot.barh(
        x='Words',
        y='Count',
        ax=ax,
        color="black")
    ax.set_title("Most Frequent Words in 'The Hobbit'")
    plt.xlabel("Count")
    plt.ylabel("Words", rotation = 0, labelpad = 25)
    ax.get_legend().remove()
    
    return


# Create a high word count dataframe and then take last 10 in list, then plot
def word_lofreq_chart(file) -> list:
    counter = Counter(file)
    count_df = pd.DataFrame(counter.most_common()[-10:], columns=['Words', 'Count'])
    print(count_df)
    
    fig, ax = plt.subplots(figsize = (8, 8))
    count_df.sort_values(by = 'Count').plot.barh(
        x='Words',
        y='Count',
        ax=ax,
        color="black")
    ax.set_title("Least Frequent Words in 'The Hobbit'")
    plt.xlabel("Count")
    plt.ylabel("Words", rotation = 0, labelpad = 25)
    ax.get_legend().remove()
    
    return
