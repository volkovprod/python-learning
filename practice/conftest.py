import os

from dotenv import load_dotenv

load_dotenv()

test_database_url = os.getenv("TEST_DATABASE_URL")

if not test_database_url:
    raise RuntimeError("TEST_DATABASE_URL is not configured")

os.environ["DATABASE_URL"] = test_database_url

import pytest
from practice.database import SessionLocal
from practice.models import Product

@pytest.fixture
def test_product():
    db = SessionLocal()

    product = Product(
        name="Cola",
        price=25,
        stock=100,
    )
    db.add(product)
    db.commit()

    yield product
    db.delete(product)
    db.commit()
    db.close()
