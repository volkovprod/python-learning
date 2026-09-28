from practice.service import get_product_by_name

def test_get_product_by_name(test_product):
    product = get_product_by_name("Cola")

    assert product is not None
    assert product.name == "Cola"

def test_get_product_by_name_not_found():
    product = get_product_by_name("Nonexistent product")

    assert product is None