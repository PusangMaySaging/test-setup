from models.product import Product
from models.user import User
from helpers.utils import create_hash
def initialize():
    products = Product()
    if len(products.get()) == 0:
        product_samples = [{
            'name':'Nike Shoe',
            'price':150
        },
        {
            'name':'Adidas Shoe',
            'price':120,
        },
        {
            'name':'Fila Shoe',
            'price': 110, 
        }
        ]
        products.createMany(product_samples)
    
    user = User()
    if len(user.get()) == 0:
        user.createOne({
            'name':'Ryan Ali',
            'email': 'Ryanali456@gmail.com',
            'password': create_hash('admin'),
            'mobile_number': '09151520264',
            'role':"admin"
        })
        pass