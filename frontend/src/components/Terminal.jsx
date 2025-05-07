import { useEffect, useRef, useState } from 'react';

const Terminal = ({ output }) => {
  const [activeTab, setActiveTab] = useState(0);
  const tableRefs = useRef([]);

  // Reset scroll positions when new output arrives
  useEffect(() => {
    if (tableRefs.current.length > 0) {
      tableRefs.current.forEach(ref => {
        if (ref) {
          ref.scrollLeft = 0;
          ref.scrollTop = 0;
        }
      });
    }
    setActiveTab(0);
  }, [output]);

  const renderOutput = () => {
    if (!output) return <div className="terminal-placeholder">Results will appear here...</div>;

    // Get all query keys from the output
    const queryKeys = output ? Object.keys(output) : [];

    if (queryKeys.length === 0) {
      return <div className="terminal-placeholder">No results to display</div>;
    }

    const currentQueryKey = queryKeys[activeTab];
    const currentResult = output[currentQueryKey];

    if (currentResult.error) {
      return (
        <div className="error-output">
          <h3>Error in {currentQueryKey}:</h3>
          <pre>{currentResult.error}</pre>
          {currentResult.details && (
            <>
              <h4>Details:</h4>
              <ul>
                {currentResult.details.map((detail, i) => (
                  <li key={i}>{detail}</li>
                ))}
              </ul>
            </>
          )}
          {currentResult['Missing tables'] && (
            <>
              <h4>Missing tables:</h4>
              <ul>
                {currentResult['Missing tables'].map((table, i) => (
                  <li key={i}>{table}</li>
                ))}
              </ul>
            </>
          )}
          {currentResult['Missing columns'] && (
            <>
              <h4>Missing columns:</h4>
              <ul>
                {currentResult['Missing columns'].map((col, i) => (
                  <li key={i}>{col}</li>
                ))}
              </ul>
            </>
          )}
        </div>
      );
    }

    if (currentResult.result && currentResult.result.length > 0) {
      return (
        <div className="table-container">
          <div
            className="result-table"
            ref={el => tableRefs.current[activeTab] = el}
          >
            <table>
              <thead>
                <tr>
                  {Object.keys(currentResult.result[0]).map((key) => (
                    <th key={key}>{key}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {currentResult.result.map((row, i) => (
                  <tr key={i}>
                    {Object.values(row).map((val, j) => (
                      <td key={j}>{String(val)}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      );
    }

    return <div>No data returned for {currentQueryKey}</div>;
  };

  return (
    <div className="terminal-container">
      <div className="terminal-header">
        <div className="query-tabs">
          {output && Object.keys(output).map((queryKey, index) => (
            <button
              key={queryKey}
              className={`query-tab ${activeTab === index ? 'active' : ''}`}
              onClick={() => setActiveTab(index)}
            >
              {queryKey}
            </button>
          ))}
        </div>
      </div>
      <div className="terminal-content">
        {renderOutput()}
      </div>
    </div>
  );
};

export default Terminal;