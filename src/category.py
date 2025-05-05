"""
Category module for e-commerce system.
"""
from typing import List

from .product import Product


class Category:
    """Class representing a product category in the e-commerce system."""

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self, name: str, description: str, products: List[Product]
    ) -> None:
        """
        Initialize a new category.

        Args:
            name: Category name
            description: Category description
            products: List of products in the category
        """
        self.name = name
        self.description = description
        self.products = products

        # Update class attributes
        Category.category_count += 1
        Category.product_count += len(products)
