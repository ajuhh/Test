// src/components/ProductList.js
import React, { useEffect, useState } from 'react';
import { fetchProducts } from '../services/api';



const ProductList = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const getProducts = async () => {
      try {
        const data = await fetchProducts();
        setProducts(data);
      } catch (error) {
        console.error("Error fetching products:", error);
      } finally {
        setLoading(false);
      }
    };
    getProducts();
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h2>Products</h2>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            {product.ProductName}
            <ul>
              {product.variants.map((variant) => (
                <li key={variant.id}>
                  {variant.name}
                  <ul>
                    {variant.sub_variants.map((subVariant) => (
                      <li key={subVariant.id}>
                        {subVariant.option} - {subVariant.stock} in stock
                      </li>
                    ))}
                  </ul>
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;

// import React, { useState, useEffect } from "react";
// import { fetchProducts } from "../services/api";  // Make sure this import is correct

// const ProductList = () => {
//   const [products, setProducts] = useState([]);

//   // Fetch products when the component mounts
//   useEffect(() => {
//     const loadProducts = async () => {
//       try {
//         const data = await fetchProducts();  // Use the fetchProducts function
//         setProducts(data);  // Set the products data in state
//       } catch (error) {
//         console.error("Error loading products:", error);
//       }
//     };

//     loadProducts();
//   }, []);

//   return (
//     <div>
//       <h2>Product List</h2>
//       <ul>
//         {products.length > 0 ? (
//           products.map((product) => (
//             <li key={product.id}>{product.ProductName}</li>
//           ))
//         ) : (
//           <p>No products available</p>
//         )}
//       </ul>
//     </div>
//   );
// };

// export default ProductList;
