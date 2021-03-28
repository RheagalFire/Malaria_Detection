import streamlit as st
import PIL
#from tensorflow.keras.models import load_model
import os
import googleapiclient.discovery
from PIL import Image
import numpy as np
#import sys
#import base64
#import cv2
#from google.oauth2 import service_account
from google.api_core.client_options import ClientOptions
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="name_of_your_json_file"
#credentials = service_account.Credentials.from_service_account_file('client_secrets.json')
PROJECT="api-mal-d"
REGION="us-central1"

def process_img(image_path):
    im=Image.open(image_path)
    im=im.resize((150,150))
    im_arr=np.asarray(im)
    im_arr=im_arr/255.0
    im_arr=im_arr.reshape(1,150,150,3)
    im_arr=im_arr.astype('float16')
    #print(im_arr.size*im_arr.itemsize)
    return im_arr
def predict_json(project, region, model, instances, version=None):
    """Send json data to a deployed model for prediction.
    Args:
        project (str): project where the Cloud ML Engine Model is deployed.
        model (str): model name.
        instances ([Mapping[str: Any]]): Keys should be the names of Tensors
            your deployed model expects as inputs. Values should be datatypes
            convertible to Tensors, or (potentially nested) lists of datatypes
            convertible to Tensors.
        version (str): version of the model to target.
    Returns:
        Mapping[str: any]: dictionary of prediction results defined by the 
            model.
    """
    # Create the ML Engine service object
    prefix = "{}-ml".format(region) if region else "ml"
    api_endpoint = "https://{}.googleapis.com".format(prefix)
    client_options = ClientOptions(api_endpoint=api_endpoint)

    # Setup model path
    model_path = "projects/{}/models/{}".format(project, model)
    if version is not None:
        model_path += "/versions/{}".format(version)

    # Create ML engine resource endpoint and input data
    ml_resource = googleapiclient.discovery.build(
        "ml", "v1", cache_discovery=False, client_options=client_options).projects()
    instances_list = instances.tolist()# turn input into list (ML Engine wants JSON)
    #print(sys.getsizeof(instances_list))
    
    input_data_json = {"signature_name": "serving_default",
                       "instances": instances_list} 

    request = ml_resource.predict(name=model_path, body=input_data_json)
    response = request.execute()
    
    # # ALT: Create model api
    # model_api = api_endpoint + model_path + ":predict"
    # headers = {"Authorization": "Bearer " + token}
    # response = requests.post(model_api, json=input_data_json, headers=headers)

    if "error" in response:
        raise RuntimeError(response["error"])

    return response["predictions"]
        

st.title('Malaria Detection App')
st.write(
    """
    ### A Simple WebApp to demonstrate Transfer Learning Predictions on  Malaria Dataset
    """
)

def find_pred(im):
    res=predict_json(project=PROJECT, region=REGION,model="api_mal_d",instances=im)
    if(np.argmax(res[0])):
        state='Uninfected'
        val=1
        #print('Unifected with probability of:',format(np.argmax(res[0])*100))
        #return state,max(pred.flatten()*100))
    else:
        state='Infected'
        val=0
        #print('Infected with probability of : ',format(np.argmax(res[0])*100))
        #return state,max(pred.flatten()*100))
    return state+" with probability of : "+str(res[0][val]*100)

image_file=st.sidebar.file_uploader('Upload an image',type=['jpg','png'])

if(image_file):
    with st.beta_expander('Selected Image',expanded=True):
        st.image(image_file,use_column_width='auto')

if image_file and st.sidebar.button('Predict'):
    image=process_img(image_file)
    pred=find_pred(image)
    st.write(pred)

