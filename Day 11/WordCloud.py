#pip install wordcloud

#conda install -c conda-forge wordcloud

import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

print('checkpoint1')

rawtext =  open('D:\C4M\Ontologies\cido.txt')

text = 'covid is a highly deadily disease that has spread acorss all the countires of the world. THe only soluiton that ww currently have is to stay in our homes af do social distancing'


wordcloud = WordCloud().generate(text)    # Create and generate a word cloud image:

# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


wordcloud.to_file("img/first_review.png")   # Save the image in the img folder: