# mongodb_graphql_training

This is a learning project. I amd trying to learn smth about mongodb (pymongo - sync connector is required!) and graphql.

HTTP server in aiohttp (asyncio).

##### **How to run the app:**

`python3 -m app`

##### **DB Collections (table analog):**

1. Customers: customer_id (unique key), name, surname;
2. Goods: good_id (unique key), name, price;
3. Orders: order_id (unique key), customer_id ("foreign key" in Customers), goods: List[good_id, number];