import axios from 'axios';

const API_URL = 'http://127.0.0.1:3000/api/'; // Replace with your backend API URL

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Function to fetch products
export const fetchProducts = async () => {
  try {
    const response = await api.get('products/');
    return response.data;
  } catch (error) {
    console.error("Error fetching products:", error);
    throw error;
  }
};

// Add product with variants and sub-variants
export const addProduct = async (productData) => {
  try {
    const response = await api.post('products/', productData);
    return response.data;
  } catch (error) {
    console.error("Error adding product:", error);
    throw error;
  }
};
