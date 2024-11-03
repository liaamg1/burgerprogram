import pytest
from app import app  # Använd absolut import
from unittest.mock import patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_frontpage(client):
    """Testar att frontpage-routen returnerar statuskod 200."""
    response = client.get('/')
    # Kontrollera att svaret har statuskod 200
    assert response.status_code == 200

def test_display_burgers(client):
    """Testar att /order-routen returnerar en lista med burgare."""
    
    mock_burgers = [
        {'name': 'Cheeseburger', 'description': 'Delicious cheeseburger', 'price': 5.99, 'is_vegetarian': False},
        {'name': 'Veggie Burger', 'description': 'Healthy veggie burger', 'price': 4.99, 'is_vegetarian': True},
    ]

    with patch('app.get_burgers', return_value=mock_burgers):
        response = client.get('/order')
        
        # Kontrollera att svaret har statuskod 200
        assert response.status_code == 200
        
        # Kontrollera att mockade burgare finns med i svaret
        for burger in mock_burgers:
            assert burger['name'].encode() in response.data

def test_send_order(client):
    """Testar att /send-order-routen tar emot och returnerar korrekt svar."""
    
    order_data = {
        'name': 'Cheeseburger',
        'wishes': 'Extra cheese'
    }

    with patch('app.requests.post') as mock_post:
        mock_post.return_value.json.return_value = {'message': 'Order received!'}
        mock_post.return_value.status_code = 200
        
        response = client.post('/send-order', json=order_data)
        
        # Kontrollera att svaret har statuskod 200
        assert response.status_code == 200
        
        # Kontrollera att meddelandet är korrekt
        assert response.json['message'] == 'Order received!'
        
