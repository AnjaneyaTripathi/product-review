from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

def freq_words(str):
	str = str.split()		
	str2 = []
	for i in str:			
		if i not in str2:
			str2.append(i)
	return str2

def generate_wordcloud(df):
    val = ''
    for x in df.Text:
        val += (x)
    stopwords = set(STOPWORDS)
    comment_words = ''
    tokens = val.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    comment_words += " ".join(tokens)+" "
    s = freq_words(comment_words)
    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    stopwords = stopwords,
                    min_font_size = 10).generate(comment_words)
				
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()
    wordcloud.to_file('cloud.png')

df = pd.read_csv('Reviews.csv')
df = df[:100]
generate_wordcloud(df)
#freq_words(val)

