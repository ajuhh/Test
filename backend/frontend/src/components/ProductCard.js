import React from 'react';

const ProductCard = ({ product }) => {
  return (
    <div className="product-card">
      <h2>{product.ProductName}</h2>
      <p>Product Code: {product.ProductCode}</p>
      <p>Stock: {product.TotalStock}</p>
      <img src={product.ProductImage ? product.ProductImage : '/placeholder.jpg'} alt={product.ProductName} />
    </div>
  );
};

export default ProductCard;
