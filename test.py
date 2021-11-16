import joblib

my_model = joblib.load('my_model')
print('-----')
print(my_model.coef_)