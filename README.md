# Malaria Detection
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
- Then go and signup for gcloud(and activate billing with free 300 dollars credit).
- Go to `Storage` under navigation pannel and create a bucket and choose `Upload Folder` and upload the `model_vgg_v3` file.
- Then Under the navigation pannel go to `AI-PLATFORM` and go to `models` and `create new model`. Create it with default settings.
- Click on the model created and then click on `create new version`.
- Select `pre-built container`
- For the model_URL click browse and select your `model_vgg_3` folder.
- Select `Python_Version==3.7`,`Tensorflow==2.3.1` and latest `ML_Runtime_version`.
- Select your preferred machine type.(Ideally **No gpu and 7.5gb Standard cpu**)
- Click on save. 
- Your model would be deployed as an api-endpoint within few mintutes.

After following all these steps you will be able to run this app locally. You can also run this app without deploying model as an api,jus tweak the code in app.py a little bit.

## To deploy this Project on Cloud Services
- Use Docker Containers to deploy this Project on any cloud service 
- For Heroku see [instructions](https://devcenter.heroku.com/categories/deploying-with-docker) for deploying with dockerimage with container_registery.
- Same goes for the google cloud platform.(Easy 10 min process is deploying through **Cloud Run**).

## Cautions
- While making model as an api point , you get a **secret json file** with you g_authentication credentials don't push it anywhere publicaly.
- While deploying this webapp don't push this **dockerfile image**(as it contains your `g_aut_secrets.json`) to DockerHub. 
