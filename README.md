# Product Review

Ever wanted to purchase a product online? Wanted to know how it actually fared? Social media and customer reviews are the best ways to decide the quality of a product. This project intends to help the user determine the reviews of the produdct using state-of-the-art techniques. 

### Classification of Reviews

Initial approaches involved CNNs and LSTMs, but they were insufficient and didn't perform upto the mark. With that we transitioned to use Transformers, which quitel literally transformed the project. A ribust model was made which classified tweets as positive, neutral and negative. 

### Useful Insights

In addition to the review classification, we have also added functionalities such as 
 <ol>
  <li>Word Cloud to determmine the most important features that have been stressed on by consumers.</li>
  <li>Piechart which show the sentiment distribution</li>
  <li>Tweets from all over the world translated to Engilsh for ease</li>
  <li>Map depicting distribution of users of the product</li>
 <li>Stats on the Top twitter usage Platforms</li>
</ol>
 
### Installation
To run the flask app in a  windows environment

 1. Install python 3.8
 2. Run ```pip install virtualenv```
 3. Run ```mkdir project``` to create project directory
 4. Run ```cd project``` to move to the project directory
 5. Run ```virtualenv venv``` to create a virtual environment
 6. Run ```.\Scripts\activate```  to activate the virtual environment
 7. Install the required dependencies
 8. Copy the contents of the Flask app folder to your virtual environment and use command ```python app.py``` to run the app.  

### Output

https://user-images.githubusercontent.com/68152189/120896833-d80efe80-c640-11eb-9b0f-021009a3fec5.mp4



***
