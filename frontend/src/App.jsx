import { useState } from 'react';
import axios from 'axios';
import Header from './components/Header';
import Editor from './components/Editor';
import Terminal from './components/Terminal';
import './App.css';

function App() {
  const [code, setCode] = useState('SELECT * FROM customers;');
  const [output, setOutput] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileUpload = async (file) => {
    try {
      const fileContent = await readFileContent(file);
      setCode(fileContent);
    } catch (error) {
      console.error('Error reading file:', error);
      setOutput({ error: 'Failed to read file' });
    }
  };

  const readFileContent = (file) => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = (event) => resolve(event.target.result);
      reader.onerror = (error) => reject(error);
      reader.readAsText(file);
    });
  };

  const executeCode = async () => {
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/execute', {
        query: code
      });
      setOutput(response.data);
    } catch (error) {
      setOutput(error.response?.data || { error: 'Connection error' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <Header
        onRun={executeCode}
        loading={loading}
        onFileUpload={handleFileUpload}
      />
      <div className="content">
        <Editor code={code} setCode={setCode} />
        <Terminal output={output} />
      </div>
    </div>
  );
}

export default App;