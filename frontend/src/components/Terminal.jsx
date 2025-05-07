import { useEffect, useRef, useState } from 'react';

const Terminal = ({ output }) => {
  const [activeTab, setActiveTab] = useState(0);
  const tableRefs = useRef([]);
  const tabsRef = useRef(null);

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
    if (tabsRef.current) {
      tabsRef.current.scrollLeft = 0;
    }
  }, [output]);

  const renderOutput = () => {
    if (!output) return <div className="terminal-placeholder">Results will appear here...</div>;

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
        </div>
      );
    }

    return (
      <div className="result-container">
        {currentResult.result && currentResult.result.length > 0 && (
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
        )}

        {currentResult.parse_tree && (
        <div className="parse-tree-container">
          <h3>Parse Tree:</h3>
          <div className="parse-tree-scroll-container">
            <pre className="parse-tree">
              {currentResult.parse_tree}
            </pre>
          </div>
        </div>
        )}
      </div>
    );
  };

  return (
    <div className="terminal-container">
      <div className="terminal-header">
        <div className="query-tabs-container">
          <div className="query-tabs" ref={tabsRef}>
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
      </div>
      <div className="terminal-content">
        {renderOutput()}
      </div>
    </div>
  );
};

export default Terminal;