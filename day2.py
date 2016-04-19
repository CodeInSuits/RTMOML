# coding: utf-8
import graphlab
sales = graphlab.SFrame('home_data.gl/')
sales = graphlab.SFrame('home_data.gl/')
sales = graphlab.SFrame('home_data.gl/')
sales
sales.show(view="Scatter Plot", x = "sqft_living", y = "price")
graphlab.canvas.set_target('ipynb')
sales.show(view="Scatter Plot", x = "sqft_living", y = "price")
train_data, test_data = sales.random_split(.8)
train_data, test_data = sales.random_split(.8,seed=0)
sqft_model = graphlab.linear_regression.create()
sqft_model = graphlab.linear_regression.create()
sqft_model = graphlab.linear_regression.create(train_data_data, target = 'price', features = ['sqft_living'] )
sqft_model = graphlab.linear_regression.create(train_data, target = 'price', features = ['sqft_living'] )
print test_data['price'].mean()
sqft_model.evaluate(test_data)
print sqft_model.evaluate(test_data)
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
plt.plot(test_data['sqft_living'], test_data['price'], '.',test_data[sqft_living], sqft_model.predict(test_data), '-')
print test_data['sqft_living']
plt.plot(test_data['sqft_living'], test_data['price'], '.',test_data['sqft_living'], sqft_model.predict(test_data), '-')
sqft_model.get('coefficient')
sqft_model.get('coefficient')
sqft_model.get('coefficients')
features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode']
sales[features].show
sales[features].show()
sales.show(view = 'BoxWhisker Plot', x = 'zipcode', y = 'price')
my_features_model = graphlab.linear_regression.create(train_data, target = 'price', features)
my_features_model = graphlab.linear_regression.create(train_data, target = 'price', features = features)
my_features_model.show()
print sqft_model.evaluate(test_data)
print sqft_model.evaluate(test_data)
print my_features_model.evaluate(test_data)
house1 = sales[sales['id'] == '5309101200']
house1
print house1['price']
print sqft_model.predict(house1)
print my_features_model.predict(house1)
