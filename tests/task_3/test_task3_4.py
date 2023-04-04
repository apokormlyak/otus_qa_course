
def test_add_option(base_url, status_code, method):
    response = method(url=base_url)
    assert str(response.status_code) == status_code
