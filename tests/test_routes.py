def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Vote for Your Favorite!" in response.data

def test_results_page(client):
    response = client.get('/results')
    assert response.status_code == 200
    assert b"Results" in response.data
