import streamlit as st
import PIL
import numpy as np
from tensorflow.keras.models import load_model


def find_pred(image_file):
    im=PIL.Image.open(image_file)
    im=im.resize((224,224))
    im_arr=np.asarray(im)
    im_arr=im_arr/255.0
    im_arr=im_arr.reshape(1,224,224,3)
    print(im_arr.shape)
    model=load_model('./Saved_model/model_vgg19.h5')
    pred=model.predict(im_arr)
    if(np.argmax(pred,axis=1)):
        state='Uninfected'
        print('Unifected with probability of:',format(max(pred.flatten()*100)))
        #return state,max(pred.flatten()*100))
    else:
        state='Infected'
        print('Infected with probability of : ',format(max(pred.flatten()*100)))
        #return state,max(pred.flatten()*100))
    return state+" with probability of : "+str(max(pred.flatten()*100))
        

st.title('Malaria Detection App')
st.write(
    """
    ### A Simple WebApp to demonstrate Transfer Learning Predictions on  Malaria Dataset
    """
)

image_file=st.sidebar.file_uploader('Upload an image',type=['jpg','png'])

if(image_file):
    with st.beta_expander('Selected Image',expanded=True):
        st.image(image_file,use_column_width='auto')

if image_file and st.sidebar.button('Predict'):
    pred=find_pred(image_file)
    st.write(pred)

