# DLFindUniqBin

Summer research project as part of the P.U.R.E. program at the University of Calgary, supervisored by Prof. John Aycock.

Recurrent neural network created in Python using the TensorFlow library to identify unique legible strings from binary programs, currently can only predict on strings without nonalphanumeric characters (single strings on each line). 

Usage: python stringsv2.py file_to_scan_for_strings

Sample file without nonalphanumeric characters: stripedteststringsoutput.txt

Folders:
cleaning_data_functions: programs used to clean data
keras_rnn: saved neural network
sample_files: files used to create training data
strings_vs_stringlish: comparing strings and stringlish output
training_data: training data used to train neural network
word_graphs: functions used to create digraphs, trigraphs and quadgraphs of training data, and compare them
words_to_ascii: unfinished code to encoding training data to ASCII encoding

Stringlish can be found at: https://github.com/aycock/stringlish
