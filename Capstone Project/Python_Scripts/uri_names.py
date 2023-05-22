"""
Created for Neuro Insights

@author: Matthew Mortensen
@email: matthew.m.mortensen@gmail.com
"""
from google.cloud import storage
#function to extract the file names of ads from a google cloud bucket.
#input needed; string of the bucket name in GCP that holds the advertisments
#input needed; string of specific folder in bucket that holds the advertisments
# the string for the folder must end with a / or it will not pull files
# ex. gcp_folder/
def get_names(bucket: str, prefix: str):
    #use to get file names
    name = [] # list to hold the file names
    GCP_bucket = bucket #bucket name in GCP
    GCP_prefix = prefix #folder name in GCP
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(GCP_bucket)
    blobs = bucket.list_blobs(prefix = GCP_prefix, delimiter = '/') #the reason why we need the end /

    for blob in blobs: #loop to get file names
        #filters out the bucket folder name and makes sure only .mp4 files are selected
        if(blob.name != GCP_prefix and blob.name.endswith('.mp4')):
            name.append(blob.name.replace(GCP_prefix, ""))
            
    #output is a list of the video file names from the GCP bucket    
    return name



#function to create the uri's to process videos for video intelligence
#input needed; string of the bucket name in GCP that holds the advertisments
#input needed; string of specific folder in bucket that holds the advertisments
#input needed; list of file names generated from get_names function 
# the string for the folder must end with a / or it will not pull files
# ex. gcp_folder/
def get_GCP_uri(bucket: str, prefix: str, names:list):
    name = names #needs list created from get_names function
    GCP_bucket = bucket #bucket name in GCP
    GCP_prefix = prefix #folder name in GCP
    out_uri = [e.replace('.mp4','.json') for e in name] #change file extension
    uri = ['gs://' + GCP_bucket + '/' + GCP_prefix + item for item in name]
    out_uri = ['gs://' + GCP_bucket + '/' + GCP_prefix + item for item in out_uri]
    
    #output is a tuple of lists of the uri and output uri needed to run the detect_logo function
    return uri, out_uri

