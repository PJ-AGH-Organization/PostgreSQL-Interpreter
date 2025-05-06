import { useState } from 'react'
import axios from 'axios'
import Header from './components/Header'
import Editor from './components/Editor'
import Terminal from './components/Terminal'
import './App.css'

function App() {
  const [code, setCode] = useState('SELECT * FROM customers;')
  const [output, setOutput] = useState(null)
  const [loading, setLoading] = useState(false)

  const executeCode = async () => {
    setLoading(true)
    try {
      const response = await axios.post('http://localhost:8000/execute', {
        query: code
      })
      setOutput(response.data)
    } catch (error) {
      setOutput(error.response?.data || { error: 'Connection error' })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <Header onRun={executeCode} loading={loading} />
      <div className="content">
        <Editor code={code} setCode={setCode} />
        <Terminal output={output} />
      </div>
    </div>
  )
}

export default App