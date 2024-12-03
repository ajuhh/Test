import React, { useState, useEffect } from 'react';
import axios from 'axios';
import StockForm from '../components/StockForm';

const StockManagementPage = () => {
  const [subVariants, setSubVariants] = useState([]);
  
  useEffect(() => {
    const fetchSubVariants = async () => {
      try {
        // Example URL, adjust according to your data model
        const response = await axios.get('http://localhost:8000/api/subvariants/');
        setSubVariants(response.data);
      } catch (error) {
        console.error(error);
      }
    };
    
    fetchSubVariants();
  }, []);
  
  return (
    <div>
      <h2>Stock Management</h2>
      {subVariants.map(subVariant => (
        <div key={subVariant.id}>
          <h3>{subVariant.option}</h3>
          <StockForm subVariantId={subVariant.id} action="add_stock" />
          <StockForm subVariantId={subVariant.id} action="remove_stock" />
        </div>
      ))}
    </div>
  );
};

export default StockManagementPage;
