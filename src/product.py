"""
Product module for e-commerce system.
"""


class Product:
    """Class representing a product in the e-commerce system."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """
        Initialize a new product.

        Args:
            name: Product name
            description: Product description
            price: Product price
            quantity: Product quantity in stock
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
