import pickle
with open("scaler.pkl", "rb") as scaler:
    scaler = pickle.load(scaler)
with open("model.pkl", "rb") as model:
    model = pickle.load(model)
if hasattr(model, "__getstate__"):
    print(model.__getstate__().get("_sklearn_version", "Tidak diketahui"))
else:
    print("Tidak dapat menemukan versi scikit-learn dalam model ini.")