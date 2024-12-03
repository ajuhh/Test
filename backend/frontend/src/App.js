// src/App.js
import React from 'react';
import ProductList from './components/ProductList';
import ProductForm from './components/ProductForm';

const App = () => {
  return (
    <div>
      <h1>Product and Stock Management</h1>
      <ProductForm />
      <ProductList />
    </div>
  );
};

export default App;
