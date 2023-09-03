const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const port = 1245;

// Create a Redis client and promisify relevant functions
const redisClient = redis.createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

// Sample product data
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Function to get an item by itemId
const getItemById = (itemId) => {
  return listProducts.find((product) => product.itemId === itemId);
};

// Function to reserve stock for an item
const reserveStockById = async (itemId, stock) => {
  await setAsync(`item:${itemId}`, stock);
};

// Function to get current reserved stock by itemId
const getCurrentReservedStockById = async (itemId) => {
  const reservedStock = await getAsync(`item:${itemId}`);
  return parseInt(reservedStock) || 0;
};

// Middleware to parse JSON requests
app.use(express.json());

// Route to get the list of all available products
app.get('/list_products', (req, res) => {
  res.json(listProducts.map((product) => ({
    itemId: product.itemId,
    itemName: product.itemName,
    price: product.price,
    initialAvailableQuantity: product.initialAvailableQuantity,
  })));
});

// Route to get product details by itemId
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (product) {
    const currentQuantity = product.initialAvailableQuantity - await getCurrentReservedStockById(itemId);
    res.json({
      itemId: product.itemId,
      itemName: product.itemName,
      price: product.price,
      initialAvailableQuantity: product.initialAvailableQuantity,
      currentQuantity,
    });
  } else {
    res.status(404).json({ status: 'Product not found' });
  }
});

// Route to reserve a product by itemId
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    res.status(404).json({ status: 'Product not found' });
  } else {
    const currentQuantity = product.initialAvailableQuantity - await getCurrentReservedStockById(itemId);

    if (currentQuantity <= 0) {
      res.json({ status: 'Not enough stock available', itemId });
    } else {
      await reserveStockById(itemId, currentQuantity - 1);
      res.json({ status: 'Reservation confirmed', itemId });
    }
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
