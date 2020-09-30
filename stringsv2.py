# Program used to replicate linux program strings using a neural network

import sys
import tensorflow as tf
from tensorflow.keras import layers

import numpy as np

# for tokenization and encoding
import tensorflow_datasets as tfds

from tensorflow import keras

def stringsv2(filename):

	try:
        # open textfile to read
		f = open(filename, 'r')
		# store file in data set
		data = f.readlines()
		data = [x.strip() for x in data] 

    	# print usage format if IOError
	except IOError as e:
		print(f'{filename}: {e.strerror}', file=sys.stderr)
		sys.exit()
	
	# reverse ordering of dataset to match neural network predictions later 
	data.reverse()
	
	# load previously saved model
	model = keras.models.load_model('kerasmodelquadgraphs')
	
	# labeler to assign integer to label file
	def labeler(example, index):
		return example, tf.cast(index, tf.int64)  
	
	# dataset of lines from text file
	lines_dataset = tf.data.TextLineDataset(f.name)

	# map each line with labeler 
	labeled_dataset = lines_dataset.map(lambda ex: labeler(ex, 0))
		
	# set tokenizer 
	tokenizer = tfds.features.text.Tokenizer()

	# initialize vocabulary set
	vocabulary_set = set()
	# tokenize each line from text file, add to vocabulary 
	for text_tensor, _ in labeled_dataset:
		some_tokens = tokenizer.tokenize(text_tensor.numpy())
		vocabulary_set.update(some_tokens)

	# set encoder
	encoder = tfds.features.text.TokenTextEncoder(vocabulary_set)

	# create encoder function to return integers for strings
	def encode(text_tensor, label):
		encoded_text = encoder.encode(text_tensor.numpy())
		return encoded_text, label
		
	# create map to encode and decode strings
	def encode_map_fn(text, label):
	# py_funct passes regular tensors to wrapped python function
		encoded_text, label = tf.py_function(encode, 
							inp=[text, label], 
							Tout=(tf.int64, tf.int64))
							

	# py_func doesn't set the shape of the returned tensors.
	# `tf.data.Datasets` work best if all components have a shape set
	#  so shapes are set manually
		encoded_text.set_shape([None])
		label.set_shape([])

		return encoded_text, label

	# encode data by passing encoded map to dataset's map function
	all_encoded_data = labeled_dataset.map(encode_map_fn)
	
	# introduced new token encoding (0 used for coding) so vocabulary size increases by one
	vocab_size += 1
	
	# use model to predict on encodered data
	pred = model.predict(all_encoded_data)
	
	# initialize array to store predictions
	pred_array = []
	
	# index to loop through predictions
	index = 0
	
	# loop through returned prediction list
	while index < len(pred):
		# if probability of it being a legible string is greater than nonlegible, prediction is 0 for legible string
		if pred[index, 0] > pred[index, 1]:
			pred_array.append(0)
			index += 1
		# if probability of it being a nonlegible string is greater than legible, prediction is 1 for nonlegible string
		elif pred[index, 0] < pred[index, 1]:
			pred_array.append(1)
			index += 1
	
	# join input data with predictions
	result = np.vstack((data, pred_array)).T
	
	# print predictions 
	print(result) 
    			

if __name__ == '__main__':
    # usage format
	if len(sys.argv) != 2:
		print(f'Usage: python3 {sys.argv[0]} filename', file=sys.stderr)
		sys.exit()
    # run stringsv2 on first argument
	stringsv2(sys.argv[1])
