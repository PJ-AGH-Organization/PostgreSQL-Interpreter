import React, { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

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
      setError("Błąd połączenia z backendem.");
      setResponse(null);
    }
  };

  return (
    <div className="flex h-screen bg-black text-white p-4 gap-4">
      {/* Left side - Query input */}
      <div className="w-1/2 flex flex-col">
        <div className="flex-grow bg-gray-900 rounded p-4">
          <textarea
            className="w-full h-full p-2 bg-gray-800 text-white rounded border border-gray-700 resize-none focus:outline-none focus:border-blue-500 font-mono"
            placeholder="Enter your SQL query here..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
        </div>
        <button
          onClick={sendQuery}
          className="mt-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 focus:outline-none font-bold"
        >
          Execute
        </button>
      </div>

      {/* Right side - Results */}
      <div className="w-1/2 flex flex-col bg-gray-900 rounded p-4">
        <div className="text-lg font-mono mb-4">Result of your query</div>

        <div className="flex-grow min-h-0"> {/* Kontener z ograniczoną wysokością */}
          {response ? (
            response.length > 0 ? (
              <div className="bg-gray-800 rounded p-4 h-full flex flex-col">
                <div className="overflow-auto flex-grow"> {/* Scrollable area */}
                  <table className="font-mono">
                    <thead>
                      <tr className="sticky top-0 bg-gray-800">
                        {Object.keys(response[0]).map((col) => (
                          <th key={col} className="border border-gray-600 px-4 py-2 text-left whitespace-nowrap">
                            {col}
                          </th>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {response.map((row, i) => (
                        <tr key={i}>
                          {Object.values(row).map((val, j) => (
                            <td key={j} className="border border-gray-600 px-4 py-2 whitespace-nowrap">
                              {val}
                            </td>
                          ))}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
                <div className="text-gray-400 text-sm mt-2">
                  {response.length} row{response.length !== 1 ? 's' : ''} returned
                </div>
              </div>
            ) : (
              <div className="bg-gray-800 rounded p-4 h-full flex items-center justify-center text-gray-400">
                No content in table
              </div>
            )
          ) : (
            <div className="bg-gray-800 rounded p-4 h-full flex items-center justify-center text-gray-400">
              <div className="text-center">
                <div className="font-mono">| C1 | C2 |</div>
                <div className="mt-2 text-sm">No data to display</div>
              </div>
            </div>
          )}
        </div>

        {/* Error display */}
        {error && (
          <div className="mt-4 p-4 bg-red-900 text-red-200 rounded font-mono text-sm whitespace-pre-wrap">
            {error}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;