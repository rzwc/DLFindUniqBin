import sys
import tensorflow as tf
from tensorflow.keras import layers

import numpy as np

# for tokenization and encoding
import tensorflow_datasets as tfds

from tensorflow import keras
#ascii 
#testing
def stringsv2(filename):

	try:
        # open binary file to read
		f = open(filename, 'r')
		data = f.readlines()
		data = [x.strip() for x in data] 

    	# print usage format if IOError
	except IOError as e:
		print(f'{filename}: {e.strerror}', file=sys.stderr)
		sys.exit()
	
	data.reverse()
		

	FILE_NAME = ['teststringoutput.txt']

	model = keras.models.load_model('kerasmodelquadgraphs')
	
	def labeler(example, index):
		return example, tf.cast(index, tf.int64)  
	
	labeled_data_sets = []

	#for i, file_name in enumerate(FILE_NAME):
	#	lines_dataset = tf.data.TextLineDataset(file_name)
	#	labeled_dataset = lines_dataset.map(lambda ex: labeler(ex, i))
	
	#	labeled_data_sets.append(labeled_dataset)
	
	lines_dataset = tf.data.TextLineDataset('teststringoutput.txt')
	#for ex in lines_dataset.take(20):
  #		print(ex)
	labeled_dataset = lines_dataset.map(lambda ex: labeler(ex, 0))
	
	labeled_data_sets.append(labeled_dataset)
	
#	for ex in labeled_dataset.take(20):
 # 		print(ex)

	
	#print(len(lines_dataset))
        
	BUFFER_SIZE = 500000
	BATCH_SIZE = 64
	TAKE_SIZE = 5000

	all_labeled_data = labeled_data_sets[0]
	#for labeled_dataset in labeled_data_sets[1:]:
	#	all_labeled_data = all_labeled_data.concatenate(labeled_dataset)
  
	#all_labeled_data = all_labeled_data.shuffle(
	#	BUFFER_SIZE, reshuffle_each_iteration=False)
		
	tokenizer = tfds.features.text.Tokenizer()

	vocabulary_set = set()
	for text_tensor, _ in all_labeled_data:
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
		
	#for ex in all_labeled_data.take(20):
  	#	print(ex)

	

	all_encoded_data = all_labeled_data.map(encode_map_fn)
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
	#print(len(all_encoded_data))
	#print(encoder.decode(numpy_words))
	print("Length of Data: " + str(len(data)))
	#print(len(pred_array))
	print("Length of Returned Prediction Array: " + str(len(pred)))
	#print(data)
	print(pred_array)
	index = 0
	
	#for ex in all_encoded_data.take(169):
  	#	print(ex)
  	#	index +=1
	
	#print(index)
	
	#print(pred_array)
	#	print(numpy_words)
	#print(encoder.decode(numpy_words))
	#print(pred_array)
	result = np.vstack((data, pred_array)).T
	print(result)
	#print(result[0])
	#print(pred)
	#print(len(pred))
    		
	


	

if __name__ == '__main__':
    # usage format
	if len(sys.argv) != 2:
		print(f'Usage: python3 {sys.argv[0]} filename', file=sys.stderr)
		sys.exit()
    # run strings on first argument
	stringsv2(sys.argv[1])
