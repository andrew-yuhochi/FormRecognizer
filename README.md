# FormRecognisor
A form recognisor built in FillEasy to extent business from online to offline

# FillEasy
FillEasy aim to create the world's first centralized form filling platform and provide a 1-stop solution to end user from finding, to filling, signing and submitting multiple forms with only a coples of mintues. 

FillEasy is Founded by a team of MSc Financial Technology students passionate to solve the problem of forms.

Website @ https://fill-easy.com/home

follow us @ https://www.facebook.com/filleasy/

## Team:
YU, Ho Chi Andrew @ FillEasy as Lead AI Developer

Lee, Zi Jin Matthew @ FillEasy as CEO

Zhang, Ruiqi Rachel @ FillEasy as COO

LI, Jiayi @ FillEasy as CFO

## Date: 
20 Dec 2021 (HKT/ GMT +8)

## Problem Statement:
We @FillEasy providing digital form filling service and maintaining > 50 forms available in current stage. In Hong Kong, our regional hub, marjority of citizen still use phycial forms as their common practice and we are trying to extent our service from online to offline. Therefore, a form recognition idea is brainstomed, which is to detect if a photo containing a form that is also available in our service, and guide them through our digital solution if possible.

## Difficulty & Our Reaction: 
1. As our data request comparison between speific forms in our database, neigther public dataset or private data are suitable to perform training for our task. ---> We create synthetic data to expand our self-collected dataset to a scarsable dataset.
2. We currently have more than 50 forms are avaible in our service and are expected to raise rapidly in the coming future, retraining the model everytime when new forms added are not fleasible. ---> A Siamese Network with triplt loss is used to perform 1-hot recognition instead of a muticlassification setting. For this purpose, a speical file storage arangement is also used.
3. Images are very large in size and it is not fleasible to load all images at once from the very beginning ---> use flow from directory method in keras to load images into memory only when we pass them into training.

## Raw Data 
We have 53 different forms are in our scope. 5 images are taken for each forms with different lighting, background and camera setting. The form are always located nearly the middle of the photo and occupied approximately 90% of total area. Below are an example:

<img src = "raw_data_example.jpeg" width = "750">

We reverse the ownership of our data.

## Reference Data
We use a digital version of 53 forms as reference data for all inferencing purpose.

## Notebooks
0. Synthetic_Data_Creation.ipynb

The first part of this notebook is to create synthetic data with a series of transformation method, including scaling, rotating, lighting, noising and bluring. All synthetic data will then be saved into a Synthetic Data File. The second part of the notebook relocate the images and create a output data file by assigning 1 possitive image and 1 negative image to each data, which match with the structure of Siamese network.

1. Model_Training.ipynb

This notebook contain 1) customized data generator, 2) base model setting, 3) simanese Network setting, 4) model training and 5) loss plotting. 1) Customized data generator is built for calling the Anchor, Positive & Negative images in a correct order.  2) Base model setting is to add 3 dense, dropout and batch normalization layers on-top of a resnet50 network. 3) Simanese Network setting is to define 2 new classes, the DistanceLayer classes for calculating the triplet loss from our input images and SiameseModel classes to combine all items & construct a simple model object. 4) model training is to train the model with defined learning rate schedule, batch size, metric and epoch. 5) loss plotting is to plot the training and validation loss for easier understnading on model performance.

2. Batch_Inference.ipynb

After training the sigmnese model, we then pass the reference data and testing data into the base model. A n-dimension embedding will be returned and we then compare the similarity between testing data to each of the reference data by calculating cosine similarity. Testing data is passed to the model and a finally testing top K accuracy is obtained. 

 
