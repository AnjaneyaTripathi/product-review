# Product Review

Ever wanted to purchase a product online? Wanted to know how it actually fared? Social media and customer reviews are the best ways to decide the quality of a product. This project intends to help the user determine the reviews of the produdct using state-of-the-art techniques. 

### Classification of Reviews

Initial approaches involved CNNs and LSTMs, but they were insufficient and didn't perform upto the mark. With that we transitioned to use Transformers, which quitel literally transformed the project. A ribust model was made which classified tweets as positive, neutral and negative. 

### Useful Insights

In addition to the review classification, we have also added functionalities such as word clouds to determmine the most important features that have been stressed on by consumers. Graphs which show the trends of the product in the past few days/weeks have also been enabled.

***

#### Setting Up the Anaphora Resolution File

Go to [this site](https://stanfordnlp.github.io/CoreNLP/index.html#download) and download CoreNLP 4.2.0. Once downloaded, unzip the file and remember where it is. Fire up the terminal and cd into the CoreNLP 4.2.0 folder and enter the following command.
```
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9000 -timeout 30000
```
This will start the server on port 9000 and you are ready to use your anaphora.py file. 
