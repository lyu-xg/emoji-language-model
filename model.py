from magpie import MagpieModel
from emojilist import emojis
magpie = MagpieModel(
    keras_model='saved_model/keras_model.h5',
    word2vec_model='saved_model/word2vec',
    scaler='saved_model/scaler',
    labels=emojis
)

def predict(t):
    return magpie.predict_from_text(t)