import pytest
from kitchen import app, orders  # Adjust the import based on your project structure

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            orders.clear()  # Reset orders list before each test
        yield client

def test_index(client):
    """Tests that the front page route returns a status code 200."""
    response = client.get('/')
    assert response.status_code == 200

def test_receive_order(client):
    """Tests that the /receive-order route receives and saves orders."""
    order_data = {
        'name': 'Cheeseburger',
        'wishes': 'Extra cheese'
    }
    
    response = client.post('/receive-order', json=order_data)
    
    # Check that the response has status code 200
    assert response.status_code == 200
    assert response.json['message'] == 'Order received'

    # Check that the order was saved
    assert len(orders) == 1
    assert orders[0]['burger'] == 'Cheeseburger'
    assert orders[0]['wishes'] == 'Extra cheese'

def test_display_orders(client):
    """Tests that the /display-orders route shows received orders."""
    order_data = {
        'name': 'Veggie Burger',
        'wishes': 'No mayo'
    }
    client.post('/receive-order', json=order_data)

    response = client.get('/display-orders')

    # Check that the response has status code 200
    assert response.status_code == 200

    # Check that the order appears in the response
    assert b'Veggie Burger' in response.data
    assert b'No mayo' in response.data

def test_display_no_orders(client):
    """Tests that the /display-orders route shows a message when no orders are present."""
    response = client.get('/display-orders')

    # Check that the response has status code 200
    assert response.status_code == 200

    # Check for a message indicating no orders (if applicable in your HTML)
    assert b'No orders available' in response.data  # Update this based on your HTML
