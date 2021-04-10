# product-review

#### Setting Up the Anaphora Resolution File

Go to [this site](https://stanfordnlp.github.io/CoreNLP/index.html#download) and download CoreNLP 4.2.0. Once downloaded, unzip the file and remember where it is. Fire up the terminal and cd into the CoreNLP 4.2.0 folder and enter the following command.
```
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9000 -timeout 30000
```
This will start the server on port 9000 and you are ready to use your anaphora.py file. 
