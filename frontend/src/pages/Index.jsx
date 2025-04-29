import React, { useState } from "react";
import Header from "../components/Header/Header.jsx";
import Editor from "../components/Editor/Editor.jsx";
import ResultPanel from "../components/ResultPanel/ResultPanel.jsx";

const Index = () => {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);
  const [lineNumbers, setLineNumbers] = useState(["1"]);

  // Handle line numbers when text changes
  const handleQueryChange = (value) => {
    setQuery(value);
    const lines = (value.match(/\n/g) || []).length + 1;
    setLineNumbers(Array.from({ length: lines }, (_, i) => String(i + 1)));
  };

  const sendQuery = async () => {
    try {
      const res = await fetch("http://localhost:8000/execute", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });

      const data = await res.json();
      if (data.error) {
        setError(`${data.error}: ${JSON.stringify(data.details || data["Missing columns"] || data["Missing tables"])}`);
        setResponse(null);
      } else {
        setResponse(data.result);
        setError(null);
      }
      // eslint-disable-next-line no-unused-vars
    } catch (err) {
      setError("Error connecting to backend.");
      setResponse(null);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-[#1e1e1e] text-gray-300">
      {/* Header with logo and controls */}
      <Header onExecute={sendQuery} />

      {/* Main content area */}
      <div className="flex flex-grow overflow-hidden">
        {/* Left panel - Editor */}
        <div className="w-1/2 flex flex-col border-r border-gray-700">
          <div className="p-2 bg-[#252526] border-b border-gray-700 text-sm flex items-center">
            <span className="px-2 py-1 bg-[#1e1e1e] rounded text-gray-300 flex items-center">
              main.sql
            </span>
          </div>
          <Editor
            value={query}
            onChange={handleQueryChange}
            lineNumbers={lineNumbers}
          />
        </div>

        {/* Right panel - Results */}
        <div className="w-1/2 flex flex-col">
          <div className="p-2 bg-[#252526] border-b border-gray-700 text-sm font-medium">
            RESULTS
          </div>
          <ResultPanel response={response} error={error} />
        </div>
      </div>
    </div>
  );
};

export default Index;
