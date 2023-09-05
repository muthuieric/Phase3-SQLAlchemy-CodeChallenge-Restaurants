from app import Restaurant, Customer, Review, session

# Create restaurants
restaurant1 = Restaurant(name='Restaurant A', price=3)
restaurant2 = Restaurant(name='Restaurant B', price=2)

# Create customers
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')

# Create reviews
review1 = Review(star_rating=5, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=4, restaurant=restaurant2, customer=customer2)

# Add data to the session and commit to the database
session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])
session.commit()
