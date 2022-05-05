# Synthetic_Data_Creation
input_dir = "./input_file"
synthetic_dir = "./synthetic_file"
output_dir = "./output_file"

num_of_syn = 200
train_val_test_ratio = [0.6, 0.2,0.2]


# Model Training
data_path = "C:/Users/user/Data_Science/Fill_Easy/FormRecognition/0.Synthetic_Data_Creation/output_file"
call_back_save_path = "./Model_callback"
model_save_path = "./Model_object"
seed = 2046
batch_size = 8
emb_size = 256
initial_learning_rate = 5e-4
max_num_epochs = 30
margin = 2

# Batch_Inference
reference_data_path = "./Reference_data/"
reference_embedding_save_path = "./Reference_Embedding"
names = 'siamese_53classes_0.0005margin_2alpha_embedding_size_256'
