
'''def PythonFIleCHeckerandPythonTOText:
    if DirectoryOfPythonFile is a directory:
        extract all python files
    else:
        if its a  file name:
            check of its a python file:
            convert it to text >> return text
        else:
            raise an error ("INvlaid file")'''

def WordCloudSingleFile(  DirectoryOfile , FileDefaultName = 'WordCloud' , verbose = True , savetoDirectory=True ,
                          max_font_size=50, max_words=100, background_color="white"):
    #OpenText file
    TextfromFile = open(DirectoryOfile, "r")

    # max_font_size=50,  lower max_font_size,
    # max_words=100, change the maximum number of word
    # background_color="white" -  lighten the background:
    wordcloud = WordCloud(max_font_size, max_words, background_color).generate(TextfromFile)

    #Saving WordCLoudImage
    if savetoDirectory == True:
        OutputImagePath = os.pathname(DirectoryOfile) + FileDefaultName
        wordcloud.to_file(OutputImagePath)

    if verbose== 1:
        # Display the generated image:
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
    else:
        pass

WordCloudSingleFile("D:\C4M\Ontologies\COVID draft 3.txt")