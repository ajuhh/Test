import React, { useState } from 'react';
import { addProduct } from '../services/api';  
import '../styles/ProductForm.css';  

const ProductForm = () => {
  const [productName, setProductName] = useState('');
  const [productCode, setProductCode] = useState('');
  const [variants, setVariants] = useState([{ name: '', options: [''] }]); // Initial variant setup
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Manually set the logged-in user ID (e.g., admin)
  const loggedInUserId = 'admin';  // For simulation, this should be fetched dynamically in a real app

  const handleProductNameChange = (e) => {
    setProductName(e.target.value);
  };

  const handleProductCodeChange = (e) => {
    setProductCode(e.target.value);
  };

  const handleVariantChange = (index, e) => {
    const updatedVariants = [...variants];
    updatedVariants[index].name = e.target.value;
    setVariants(updatedVariants);
  };

  const handleSubVariantChange = (variantIndex, subVariantIndex, e) => {
    const updatedVariants = [...variants];
    updatedVariants[variantIndex].options[subVariantIndex] = e.target.value;
    setVariants(updatedVariants);
  };

  const addVariant = () => {
    setVariants([...variants, { name: '', options: [''] }]);
  };

  const addSubVariant = (variantIndex) => {
    const updatedVariants = [...variants];
    updatedVariants[variantIndex].options.push('');
    setVariants(updatedVariants);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);
    
    const productData = {
      ProductName: productName,
      ProductCode: productCode,
      variants: variants.map((variant) => ({
        name: variant.name,
        options: variant.options.filter(option => option), // Filter out empty options
      })),
      CreatedUser: loggedInUserId, // Set the logged-in user ID (admin in this case)
      IsFavourite: true,
      Active: true,
      HSNCode: "1234",  // Example HSN Code
      TotalStock: 100.00,
    };

    try {
      await addProduct(productData); // Assuming addProduct sends the data to the backend
      setProductName('');
      setProductCode('');
      setVariants([{ name: '', options: [''] }]);  // Reset form
      alert('Product added successfully!');
    } catch (err) {
      setError('Failed to add product');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="form-container">
      <h2>Add New Product</h2>
      {error && <p className="error">{error}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Product Name:</label>
          <input
            type="text"
            value={productName}
            onChange={handleProductNameChange}
            required
          />
        </div>
        <div>
          <label>Product Code:</label>
          <input
            type="text"
            value={productCode}
            onChange={handleProductCodeChange}
            required
          />
        </div>

        <h3>Variants</h3>
        {variants.map((variant, variantIndex) => (
          <div key={variantIndex}>
            <div>
              <label>Variant Name:</label>
              <input
                type="text"
                value={variant.name}
                onChange={(e) => handleVariantChange(variantIndex, e)}
                required
              />
            </div>

            <h4>Sub-Variants</h4>
            {variant.options.map((option, subVariantIndex) => (
              <div key={subVariantIndex}>
                <label>Sub-Variant Option:</label>
                <input
                  type="text"
                  value={option}
                  onChange={(e) => handleSubVariantChange(variantIndex, subVariantIndex, e)}
                  required
                />
              </div>
            ))}
            <button type="button" onClick={() => addSubVariant(variantIndex)}>
              Add Sub-Variant
            </button>
          </div>
        ))}

        <button type="button" onClick={addVariant}>
          Add Variant
        </button>

        <div>
          <button type="submit"  disabled={isLoading}>
            {isLoading ? 'Adding Product...' : 'Add Product'}
          </button>
        </div>
      </form>
    </div>
  );
};

export default ProductForm;
