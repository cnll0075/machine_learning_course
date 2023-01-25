from fastcore.all import *
from fastai.vision.all import *


def predict(img):
    model = load_learner('../nb_with_full_notes/model/ab_license_plate.pkl', cpu=False)
    pred = model.predict(img)[0]
    print(pred)
    return pred
