## Malaria Detection
Using Transfer Learning(using VGG architecture) for Malaria Detection

## Website Overview
![img](https://github.com/RheagalFire/Malaria_Detection/blob/master/Results/Infected.JPG)

## How to run this Locally
- To do this you need to deploy the model as an api endpoint on google cloud. (**SEE BELOW**)
- Then go to Service Accounts(under IAM & Admin) on your g-console and create service(**with Roles:ML Engineer and Security Admin**).
- Then create a key and download that key as a `.json` file.
- Then go in the **app.py** file and rename `os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="name_of_your_json_file"`
- Run this in your terminal `pip install -r requirements.txt`
- Run the app using terminal command `streamlit run app.py`

## Deploying model as api-endpoint using google's AI-Platform service
- Either download the folder `model_vgg_v3` or create your own following the instructions of [.ipynb notebook](https://github.com/RheagalFire/Malaria_Detection/blob/master/Malaria_Detection.ipynb)
