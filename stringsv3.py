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
	
	# set to store labeled dataset
	labeled_data_sets = []
	
	lines_dataset = tf.data.TextLineDataset(f.name)

	labeled_dataset = lines_dataset.map(lambda ex: labeler(ex, 0))
		
	tokenizer = tfds.features.text.Tokenizer()

	vocabulary_set = set()
	for text_tensor, _ in labeled_dataset:
		some_tokens = tokenizer.tokenize(text_tensor.numpy())
		vocabulary_set.update(some_tokens)

	# size of vocabulary
	vocab_size = len(vocabulary_set)
	
	encoder = tfds.features.text.TokenTextEncoder(vocabulary_set)

	def encode(text_tensor, label):
		encoded_text = encoder.encode(text_tensor.numpy())
		return encoded_text, label
		
	def encode_map_fn(text, label):
	# py_func doesn't set the shape of the returned tensors.
		encoded_text, label = tf.py_function(encode, 
							inp=[text, label], 
							Tout=(tf.int64, tf.int64))

	# `tf.data.Datasets` work best if all components have a shape set
	#  so set the shapes manually: 
		encoded_text.set_shape([None])
		label.set_shape([])

		return encoded_text, label

	all_encoded_data = labeled_dataset.map(encode_map_fn)
	vocab_size += 1
	pred = model.predict(all_encoded_data)
	pred_array = []
	index = 0
	while index < len(pred):
		if pred[index, 0] > pred[index, 1]:
			pred_array.append(0)
			index += 1
		elif pred[index, 0] < pred[index, 1]:
			pred_array.append(1)
			index += 1
	
	for words, labels in all_encoded_data.take(1):  # only take first element of dataset
		numpy_words = words.numpy()
		numpy_labels = labels.numpy()
	
	result = np.vstack((data, pred_array)).T
	print(result)
    			

if __name__ == '__main__':
    # usage format
	if len(sys.argv) != 2:
		print(f'Usage: python3 {sys.argv[0]} filename', file=sys.stderr)
		sys.exit()
    # run strings on first argument
	stringsv2(sys.argv[1])
