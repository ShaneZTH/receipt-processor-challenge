from pydantic import BaseModel, Field
from typing import Annotated, List

class Item(BaseModel):
    """
    Represents an item on a receipt.
    """
    shortDescription: Annotated[
        str,
        Field(
            pattern=r"^[\w\s\-]+$",
            description="Short Product Description"
        )
    ]
    price: Annotated[
        str,
        Field(
            pattern=r"^\d+\.\d{2}$",
            description="Price of the item"
        )
    ]

class Receipt(BaseModel):
    """
    Represents a receipt submitted for processing.
    """
    retailer: Annotated[
        str,
        Field(
            pattern=r"^[\w\s\-\&]+$",
            description="Name of the retailer or store"
        )
    ]
    purchaseDate: Annotated[
        str,
        Field(
            pattern=r"^\d{4}-\d{2}-\d{2}$",
            description="Purchase date in YYYY-MM-DD format"
        )
    ]
    purchaseTime: Annotated[
        str,
        Field(
            pattern=r"^\d{2}:\d{2}$",
            description="Purchase time in HH:mm (24-hour) format"
        )
    ]
    total: Annotated[
        str,
        Field(
            pattern=r"^\d+\.\d{2}$",
            description="Total amount paid on the receipt"
        )
    ]
    items: Annotated[
        List[Item],
        Field(
            min_items=1,
            description="List of items purchased"
        )
    ]
