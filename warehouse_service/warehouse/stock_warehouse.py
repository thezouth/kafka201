from .stock import StockItem

STOCK_WAREHOUSE = {
    item.product_id : item 
    for item in [
        StockItem(1, 'Butter', 20),
        StockItem(2, 'Milk', 100),
        StockItem(3, 'Flour', 30),
        StockItem(4, 'Dark Chocolate', 35),
        StockItem(5, 'Milke Chocolate', 54),
        StockItem(6, 'Baking Soda', 43)
    ]
}