// src/components/StockForm.js
import React, { useState } from 'react';
import { addStock, removeStock } from '../services/api';

const StockForm = ({ subVariantId }) => {
  const [quantity, setQuantity] = useState(0);
  const [loading, setLoading] = useState(false);

  const handleStockChange = async (action) => {
    setLoading(true);
    try {
      if (action === 'add') {
        await addStock(subVariantId, quantity);
      } else if (action === 'remove') {
        await removeStock(subVariantId, quantity);
      }
    } catch (error) {
      console.error("Error handling stock change:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <input
        type="number"
        value={quantity}
        onChange={(e) => setQuantity(e.target.value)}
        min="1"
        required
      />
      <button onClick={() => handleStockChange('add')} disabled={loading}>
        {loading ? 'Adding...' : 'Add Stock'}
      </button>
      <button onClick={() => handleStockChange('remove')} disabled={loading}>
        {loading ? 'Removing...' : 'Remove Stock'}
      </button>
    </div>
  );
};

export default StockForm;
