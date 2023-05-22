"""
Created for Neuro Insights

@author: Matthew Mortensen
@email: matthew.m.mortensen@gmail.com

parts of the code have been sanitized due to NDA
"""
import pandas as pd
#function used for selecting a predominat logo per video
#input needed; dataframe from logo_output
#input needed; confidence cutoff number
#input needed; file path for customized json outputs
def logo_selection(df, file_path: str, confidence=#num):
    path = file_path
    df_logo = df
    cutoff = confidence
    #sanitized
    #sum up number of frames per logo detected
    #sanitized
    dfdrop.to_json(path+'market_industry.json', orient='index', indent=2)
    
    #create separeate file showing logos that have been excluded from selection
    #sanitized
    df_exc.to_json(path+'excluded_logos.json', orient='index', indent=2)
    return dfdrop

#function used for selecting a predominat logo per video
#
#input needed; dataframe from logo_output
#input needed; file path for customized json outputs
#input needed; confidence cutoff number, 
def logo_selection_noML(df, file_path: str, confidence=#num):
    path = file_path
    df_logo = df
    cutoff = confidence
    #sanitized
    
    dfls.to_json(path + 'market_industry_noML.json', orient='index', indent=2)
    
    #create separeate file showing videos that have been excluded from selection
    #sanitized
    df_exc.to_json(path + 'excluded_logos_noML.json', orient='index', indent=2)
    return dfls