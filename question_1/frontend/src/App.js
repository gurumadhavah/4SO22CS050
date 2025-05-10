import React, { useState } from 'react';
import './App.css';

function App() {
  //state vars
  const [windowPrevState, setWindowPrevState] = useState([]);
  const [windowCurrState, setWindowCurrState] = useState([]);
  const [fetchedNumbers, setFetchedNumbers] = useState([]);
  const [average, setAverage] = useState("0.00");
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const API_BASE_URL = "http://localhost:8000"; //fastapi
//get res
  const fetchAverageData = async (numberId) => {
    setError('');
    setLoading(true);
    try {
      const response = await fetch(`${API_BASE_URL}/numbers/${numberId}`);
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || `Error status: ${response.status}`);
      }
      const data = await response.json();
      setWindowPrevState(data.windowPrevState);
      setWindowCurrState(data.windowCurrState);
      setFetchedNumbers(data.numbers);
      setAverage(data.avg);
    } catch (e) {
      console.error("Fetch error:", e);
      setError(`Failed to fetch data: ${e.message}`);
    } finally {
      setLoading(false);
    }
  };
//types of num
  const numberIds = [
    { id: 'p', name: 'Prime' },
    { id: 'f', name: 'Fibonacci' },
    { id: 'e', name: 'Even' },
    { id: 'r', name: 'Random' },
  ];
//ui
  return (
    <div className="App">
      <header className="App-header">
        <h1>Calculator</h1>
      </header>
      <main>
        <div className="types">
          <h2>Select Number Type:</h2>
          {numberIds.map((type) => (
            <button
              key={type.id}
              onClick={() => fetchAverageData(type.id)}
              disabled={loading}
            >
              {loading ? 'Loading...' : type.name}
            </button>
          ))}
        </div>

        {error && <p className="error-message">Error: {error}</p>}

        <div className="results">
          <div className="result-section">
            <h3>Numbers Received from Server (This Call):</h3>
            <pre>{JSON.stringify(fetchedNumbers, null, 2)}</pre>
          </div>
          <div className="result-section">
            <h3>Window - Previous State:</h3>
            <pre>{JSON.stringify(windowPrevState, null, 2)}</pre>
          </div>
          <div className="result-section">
            <h3>Window - Current State (Stored Numbers):</h3>
            <pre>{JSON.stringify(windowCurrState, null, 2)}</pre>
          </div>
          <div className="result-section">
            <h3>Calculated Average:</h3>
            <p className="average-display">{average}</p>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;