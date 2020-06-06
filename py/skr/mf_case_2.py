from sklearn import datasets
from sklearn.linear_model import LinearRegression

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target

model = LinearRegression()
model.fit(data_X, data_y)

print('coef:')
print(model.coef_)
print('intercept: ')
print(model.intercept_)

print("param:")
print(model.get_params())

print("score:")
print(model.score(data_X, data_y))

print('Predict:')
print(model.predict(data_X[:4, :]))
print(data_y[:4])
