"""
Created for Neuro Insights

@author: Matthew Mortensen
@email: matthew.m.mortensen@gmail.com

parts of the code are sanitized due to NDA
"""
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle
#input needed; file location of training set
def create_model(train, file_path):
    df_model = train
    path = file_path
    #sanitized
    # define our independent and dependent variables
    X = df_model
    y = df_model
    #80% train and 20% test, added random state number to get repeatable results
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
   #sanitized
    #Create random forrest classifier
    model_RF = RandomForestClassifier(random_state=10)
    model_RF.fit(X, y)
    #get accuracy measurement
    y_test_hat_RF = model_RF.predict(X_test)
    acc_RF_smote = accuracy_score(y_test, y_test_hat_RF)
    #sanitized
    return model_RF



#input needed; dataframe to make predictions
#input needed; model location to load
def model_prediction(df,model_file):
    model = model_file
    data = df
    #load model
    #sanitized
    
    #predict outcomes
    result = loaded_model.predict(df_predict)
    #add prediction column
    #sanitized
    
    #return the predicted results dataframe
    return output