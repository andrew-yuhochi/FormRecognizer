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
1. As our data request comparison between speific forms in our database, neigther public dataset or private data are suitable to perform training for our task. -> We create synthetic data to expand our self-collected dataset to a scarsable dataset.
2. We currently have more than 50 forms are avaible in our service and are expected to raise rapidly in the coming future, retraining the model everytime when new forms added are not fleasible. -> A Siamese Network with triplt loss is used to perform 1-hot recognition instead of a muticlassification setting. For this purpose, a speical file storage arangement is also used.
3. Images are very large in size and it is not fleasible to load all images at once from the very beginning -> use flow from directory method in keras to load images into memory only when we pass them into training.

## Raw Data File
We have 53 different forms are in our scope. 5 images are taken for each forms with different lighting, background and camera setting. The form are always located nearly the middle of the photo and occupied approximately 90% of total area. Below are an example:

<img src = "images/raw_data_example.jpeg" width = "750">

All images are named in "aaaaabb.jpeg" format, where aaaaa is a 5-digit number to repersent a specific class and bb is a 2-digit number to repesent the current example under that classes. All these raw data are all located in "input_file".

## Synthetic Data File
For each raw data, we create 200 Synthetic images by a series of image transformation method. All the new images will then saved in the synthetic_file with a speaical file directory ordering as follow:

<img src = "images/synthetic_file_directory_ordering.jpeg" width = "750">

All synthetic images again are named in "aaaaa_b.jpeg" format, where aaaaa is a 5-digit number to repersent a specific class as above and b is a n-digit number to repesent the current example under that classes. All these synthetic data will be located in "synthetic_file".

## Output Data File
For fitting the Synthetic Data into a Siamese Network, we need to assign 1 possitive example and 1 negative example to each training data. Thus, we further rearrange the file directory ordering as follow:

<img src = "images/output_file_directory_ordering.jpeg" width = "750">

All data are named in "b.jpeg" format only and b is a n-digit number to repesent the current example under that classes. The same b number uner the same class will be extract at the same time and fit into the model later on. All these synthetic data will be located in "output_file".


## Notebooks
0. Synthetic_Data_Creation.ipynb
This notebook first create synthetic data with a series of transformation method, including scaling, rotating, lighting, noising and bluring. Details please refer to the Session 1. Create Synthetic Image in this notebook. Those synthetic data will then be saved into Synthetic Data File. 

The notbook will then relocate the images and create the Output Data File by assigning 1 possitive image and 1 negative image to each data.
