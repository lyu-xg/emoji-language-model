from magpie import MagpieModel
import pandas as pd
import numpy as np
data_folder = 'data/'

magpie = MagpieModel()

magpie.init_word_vectors(data_folder, vec_dim=100)

from emojilist import emojis
#magpie.train(data_folder, ['smile', 'rock', 'smilecry', 'sad', 'star', 'shock', 'bullseye', 'fire'], test_ratio=0.2, nb_epochs=1000)
try:
	magpie.train(data_folder, emojis, test_ratio=0.2, nb_epochs=5)
except:
	magpie.save_word2vec_model('saved_model/word2vec', overwrite=True)
	magpie.save_scaler('saved_model/scaler', overwrite=True)
	magpie.save_model('saved_model/keras_model.h5')
