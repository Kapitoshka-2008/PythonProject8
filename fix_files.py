"""
Script to fix file formatting issues.
"""


def write_file(path: str, content: str) -> None:
    """Write content to file with proper line endings."""
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def create_init_files() -> None:
    """Create __init__.py files."""
    write_file(
        "src/__init__.py",
        '"""\nE-commerce core package initialization.\n"""\n',
    )
    write_file(
        "tests/__init__.py",
        '"""\nTest package initialization.\n"""\n',
    )


def create_conftest() -> None:
    """Create conftest.py file."""
    write_file(
        "tests/conftest.py",
        'import os\nimport sys\n\n'
        '# Добавляем корневую директорию проекта в PYTHONPATH\n'
        'project_root = os.path.abspath(\n'
        '    os.path.join(os.path.dirname(__file__), "..")\n'
        ')\n'
        'sys.path.insert(0, project_root)\n',
    )


def create_product() -> None:
    """Create product.py file."""
    write_file(
        "src/product.py",
        '"""\nProduct module for e-commerce system.\n"""\n\n\n'
        'class Product:\n'
        '    """Class representing a product in the e-commerce system."""\n\n'
        '    def __init__(\n'
        '        self,\n'
        '        name: str,\n'
        '        description: str,\n'
        '        price: float,\n'
        '        quantity: int\n'
        '    ) -> None:\n'
        '        """\n'
        '        Initialize a new product.\n\n'
        '        Args:\n'
        '            name: Product name\n'
        '            description: Product description\n'
        '            price: Product price\n'
        '            quantity: Product quantity in stock\n'
        '        """\n'
        '        self.name = name\n'
        '        self.description = description\n'
        '        self.price = price\n'
        '        self.quantity = quantity\n',
    )


def create_category() -> None:
    """Create category.py file."""
    write_file(
        "src/category.py",
        '"""\nCategory module for e-commerce system.\n"""\n'
        'from typing import List\n\n'
        'from .product import Product\n\n\n'
        'class Category:\n'
        '    """Class representing a product category in the e-commerce system."""\n\n'
        '    category_count: int = 0\n'
        '    product_count: int = 0\n\n'
        '    def __init__(\n'
        '        self,\n'
        '        name: str,\n'
        '        description: str,\n'
        '        products: List[Product]\n'
        '    ) -> None:\n'
        '        """\n'
        '        Initialize a new category.\n\n'
        '        Args:\n'
        '            name: Category name\n'
        '            description: Category description\n'
        '            products: List of products in the category\n'
        '        """\n'
        '        self.name = name\n'
        '        self.description = description\n'
        '        self.products = products\n\n'
        '        # Update class attributes\n'
        '        Category.category_count += 1\n'
        '        Category.product_count += len(products)\n',
    )


def create_tests() -> None:
    """Create test_main.py file."""
    write_file(
        "tests/test_main.py",
        '"""\nTests for e-commerce core functionality.\n"""\n'
        'import pytest\n\n'
        'from src.category import Category\n'
        'from src.product import Product\n\n\n'
        '@pytest.fixture\ndef sample_product() -> Product:\n'
        '    """Fixture that returns a sample product for testing."""\n'
        '    return Product(\n'
        '        "Test Product",\n'
        '        "Test Description",\n'
        '        100.0,\n'
        '        10\n'
        '    )\n\n\n'
        '@pytest.fixture\ndef sample_category(sample_product: Product) -> Category:\n'
        '    """Fixture that returns a sample category for testing."""\n'
        '    return Category(\n'
        '        "Test Category",\n'
        '        "Test Description",\n'
        '        [sample_product]\n'
        '    )\n\n\n'
        'def test_product_initialization(sample_product: Product) -> None:\n'
        '    """Test product initialization with correct values."""\n'
        '    assert sample_product.name == "Test Product"\n'
        '    assert sample_product.description == "Test Description"\n'
        '    assert sample_product.price == 100.0\n'
        '    assert sample_product.quantity == 10\n\n\n'
        'def test_category_initialization(\n'
        '    sample_category: Category,\n'
        '    sample_product: Product,\n'
        ') -> None:\n'
        '    """Test category initialization with correct values."""\n'
        '    assert sample_category.name == "Test Category"\n'
        '    assert sample_category.description == "Test Description"\n'
        '    assert sample_category.products == [sample_product]\n\n\n'
        'def test_category_count() -> None:\n'
        '    """Test category and product counting."""\n'
        '    # Сбрасываем счетчики перед тестом\n'
        '    Category.category_count = 0\n'
        '    Category.product_count = 0\n\n'
        '    # Создаем тестовые продукты\n'
        '    product1 = Product("Product 1", "Desc 1", 100.0, 5)\n'
        '    product2 = Product("Product 2", "Desc 2", 200.0, 3)\n\n'
        '    # Создаем категории\n'
        '    Category("Category 1", "Desc 1", [product1])\n'
        '    Category("Category 2", "Desc 2", [product1, product2])\n\n'
        '    assert Category.category_count == 2\n'
        '    # Общее количество продуктов в категориях\n'
        '    assert Category.product_count == 3\n',
    )


def main() -> None:
    """Run all file creation functions."""
    create_init_files()
    create_conftest()
    create_product()
    create_category()
    create_tests()


if __name__ == "__main__":
    main() 