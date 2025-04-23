import pytest
from main import Product, Category


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 100.0, 10)


@pytest.fixture
def sample_category(sample_product):
    return Category("Test Category", "Test Description", [sample_product])


def test_product_initialization(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 10


def test_category_initialization(sample_category, sample_product):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Description"
    assert sample_category.products == [sample_product]


def test_category_count():
    # Reset counts
    Category.category_count = 0
    Category.product_count = 0
    
    # Create test products
    product1 = Product("Product 1", "Desc 1", 100.0, 5)
    product2 = Product("Product 2", "Desc 2", 200.0, 3)
    
    # Create categories
    category1 = Category("Category 1", "Desc 1", [product1])
    category2 = Category("Category 2", "Desc 2", [product1, product2])
    
    assert Category.category_count == 2
    assert Category.product_count == 3  # Total unique products 