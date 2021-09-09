# California Housing prediction
In this project I have built a Real Estate Price Predictor for the California State using the fudamentals of Data Science and Machine Learning like Feature Engineering, Data Transformation, One Hot Encoding, Outlier Detection, KFoldCrossValidation and GridSearchCV. The project in the Backend uses RandomForestRegression to predict the price for a certain district in california taking into account the geographical location as well as the overall district's real estate data. It also has a frontend, built using HTML & CSS     and deployed over heroku.
**Link** - https://california-houses-prediction.herokuapp.com/

## Dataset
This dataset is a modified version of the California Housing dataset available from Luís Torgo's page (University of Porto). Luís Torgo obtained it from the StatLib repository (which is closed now). This dataset appeared in a 1997 paper titled Sparse Spatial Autoregressions by Pace, R. Kelley and Ronald Barry, published in the Statistics and Probability Letters journal. They built it using the 1990 California census data. It contains one row per census block group. A block group is the smallest geographical unit for which the U.S. Census Bureau publishes sample data (a block group typically has a population of 600 to 3,000 people).

#### Modifications
  The dataset is almost identical to the original, with two differences:
- 207 values were randomly removed from the total_bedrooms column, in order to tackle missing data problem.
- An additional categorical attribute called ocean_proximity was added, indicating (very roughly) whether each block group is near the ocean, near the Bay area, inland or on an    island so that the model can handle both numerical and categorical data. 

## Technologies Used
- Python as Programming Language
- Pandas & Numpy for Handling Data
- matplotlib for Data Visualization
- sklearn for Model Building
- Flask for Backend Server
- HTML, CSS & JQuery for Frontend

## Project Structure
**Branch : main**
- **model.py** - contains code for the transformation pipelines used to convert the user input(i.e. both numerical and categorical) in a format as per required by the model(**my_model.pkl**) and computes the predicted value based on the model.
- **app.py** - contains Flask APIs that receives input through the GUI or API calls, receives the predicted value from model.py and returns it.
- **templates\home.html** - contains all the HTML code and CSS-Bootstrap styling used to design the frontend along, with the Ajax request that will send all the user entered data to the Flask API.

**Branch : model**
 
 contains the original dataset used for training the model and the jupyter notebook which contains the code for the model.
