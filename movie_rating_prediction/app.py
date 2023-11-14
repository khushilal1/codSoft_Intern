
import streamlit as slt
import pandas as pd
import pickle
import warnings
warnings.filterwarnings("ignore")


# Load the Rideg classifiet model from the pickle file
model = pickle.load(open('model.pkl', 'rb'))

data_df=pickle.load(open("data.pkl",'rb'))
# Define the columns for user input

columns=['Year',"Duration","Votes"]


# Create a function to preprocess user input make predictions

def predict_rating(input_data):
    # Preprocess the input data
    input_df = pd.DataFrame([input_data], columns=columns)
   
    # Make predictions using the loaded model
    prediction = model.predict(input_df)
    
    return prediction


# Create the Streamlit app
def main():


    slt.title("Movie Rating Prediction on  the basis of Given specs")
    slt.write("Enter detail to get the rating value")



    Year= slt.selectbox("Select the Year in which movie release", data_df['Year'].unique())


    Duration= slt.selectbox("Select the Time duration of Movie", data_df['Duration'].unique())

    Votes= slt.selectbox("Select the Votes You want to give on baisis of Public Voting", data_df['Votes'].unique())


 

    if slt.button("Predict"):
    
        # Create a dictionary to store the user input
        input_data = {
            'Year':Year,
            "Duration":Duration,
            'Votes':Votes

           
        }

        # # Predict churn based on user input
        predicted_rating = predict_rating(input_data)
        
        slt.write(f'The Predicted Rating of movie will be approx: {round(predicted_rating[0],2)}')
     

# Run the Streamlit app
if __name__ == '__main__':
    main()