import os
import pickle 
from functools import lru_cache

from django.conf import settings

@lru_cache(maxsize=1)
def load_bundle():
    pkl_path = os.path.join(settings.BASE_DIR,'recognition','ml','Crop_recognition_jupytercode.pkl')
     #<BASE_DIR>/recognition/ml/Crop_recognition_jupytercode.pkl

    with open(pkl_path,'rb') as f:
        bundle = pickle.load(f)

    assert "model" in bundle and "feature_cols" in bundle, "Invalid model bundle structure."
    return bundle                 


def predictions(feature_dict):

    bundle = load_bundle()

    model = bundle["model"]
    order = bundle["feature_cols"]   # we got here ['N','P','K','temperature','humidity','ph','rainfall']

    x = [[float(feature_dict[c]) for c in order]]
    pred = model.predict(x)
    return pred[0]