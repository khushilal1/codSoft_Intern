
import streamlit as slt
import pandas as pd
import pickle

# Load the Rideg classifiet model from the pickle file
model = pickle.load(open('model.pkl', 'rb'))

data_df=pickle.load(open("data.pkl",'rb'))
# Define the columns for user input

columns=['sepal_length','sepal_width','petal_length','petal_width']

# Create a function to preprocess user input make predictions

def classify_flower(input_data):
    # Preprocess the input data
    input_df = pd.DataFrame([input_data], columns=columns)
   
    # Make predictions using the loaded model
    prediction = model.predict(input_df)
    
    return prediction


# Create the Streamlit app
def main():


    slt.title("Iris flower Classification in the basis of Give specs")
    slt.write("Enter the customer details below to predict churn.")


    sepal_length= slt.selectbox("Select the length of Sepal of flower", data_df['sepal_length'].unique())

    sepal_width= slt.selectbox("Select the Width of Sepal of flower", data_df['sepal_width'].unique())

    petal_length= slt.selectbox("Select the Length of Petal of flower", data_df['petal_length'].unique())

    petal_width= slt.selectbox("Select the Width of Petal of flower", data_df['petal_width'].unique())


    if slt.button("Predict"):
    
        # Create a dictionary to store the user input
        input_data = {
            'sepal_length':sepal_length,
            "sepal_width":sepal_width,
            'petal_length':petal_length,
            "petal_width":petal_width,
        
        }

        # # Predict churn based on user input
        classified_flower = classify_flower(input_data)
        
        slt.write(f'The classified value on the basisi of given measurement is {classified_flower[0]}')
     

# Run the Streamlit app
if __name__ == '__main__':
    main()