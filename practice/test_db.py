from practice.database import SessionLocal
from practice.service import create_product, get_product_by_name, update_product,delete_product


def test_get_product_by_name(test_product):
    product = get_product_by_name("Cola")

    assert product is not None
    assert product.name == "Cola"

def test_get_product_by_name_not_found():
    product = get_product_by_name("Nonexistent product")

    assert product is None

def test_update_product(test_product):
    product = update_product(
        "Cola",
        30,
        80,
    )
    assert product is not None
    assert product.name == "Cola"
    assert product.price == 30
    assert product.stock == 80

def test_delete_product(test_product):
    result = delete_product("Cola")

    assert result is True
    assert get_product_by_name("Cola") is None


def test_get_product():
    product = create_product(
        name="Test Gin",
        price=50,
        stock=10,
    )

    assert product is not None
    assert product.name == "Test Gin"
    assert product.price == 50
    assert product.stock == 10

    db = SessionLocal()
    db.delete(product)
    db.commit()
    db.close()

def test_create_dublicate_product():
    first_product = create_product(
        name="Test Dublicate",
        price=50,
        stock=10,
    )

    assert first_product is not None

    second_product = create_product(
        name="Test Dublicate",
        price=50,
        stock=10,
    )

    assert second_product is None

    db = SessionLocal()
    db.delete(first_product)
    db.commit()
    db.close()
