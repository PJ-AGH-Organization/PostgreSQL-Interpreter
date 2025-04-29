import React from "react";

const ResultPanel = ({ response, error }) => {
  return (
    <div className="flex-grow overflow-auto p-4 bg-[#1e1e1e] font-mono text-sm">
      {error ? (
        <div className="p-4 bg-red-900/30 border border-red-800 text-red-200 rounded whitespace-pre-wrap">
          {error}
        </div>
      ) : response ? (
        response.length > 0 ? (
          <div className="flex flex-col h-full">
            <div className="overflow-auto flex-grow">
              <table className="w-full border-collapse">
                <thead>
                  <tr>
                    {Object.keys(response[0]).map((col) => (
                      <th key={col} className="border-b border-gray-700 px-4 py-2 text-left sticky top-0 bg-[#252526] font-medium">
                        {col}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {response.map((row, i) => (
                    <tr key={i} className="hover:bg-[#2a2d2e]">
                      {Object.values(row).map((val, j) => (
                        <td key={j} className="border-b border-gray-800 px-4 py-2">
                          {val !== null ? String(val) : <span className="text-gray-500">null</span>}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <div className="text-gray-500 text-xs mt-2 pt-2 border-t border-gray-800">
              {response.length} row{response.length !== 1 ? 's' : ''} returned
            </div>
          </div>
        ) : (
          <div className="flex items-center justify-center h-full text-gray-500">
            Query executed successfully. No rows returned.
          </div>
        )
      ) : (
        <div className="flex items-center justify-center h-full text-gray-500">
          <div className="text-center">
            <div className="text-xs bg-[#252526] inline-block p-2 rounded border border-gray-700 mb-2">
              No results to display
            </div>
            <div>
              Enter a SQL query and click Run to see results
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ResultPanel;