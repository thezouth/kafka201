CREATE TABLE orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATETIME,
    customer_id INTEGER,
    customer_name TEXT,
    is_member BOOLEAN
);

CREATE TABLE order_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    amount INTEGER,
    price_per_unit REAL
);