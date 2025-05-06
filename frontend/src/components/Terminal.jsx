import { useEffect, useRef } from 'react';

const Terminal = ({ output }) => {
  const tableRef = useRef(null);

  // Reset scroll position when new output arrives
  useEffect(() => {
    if (tableRef.current) {
      tableRef.current.scrollLeft = 0;
      tableRef.current.scrollTop = 0;
    }
  }, [output]);

  const renderOutput = () => {
    if (!output) return <div className="terminal-placeholder">Results will appear here...</div>;

    if (output.error) {
      return (
        <div className="error-output">
          <h3>Error:</h3>
          <pre>{output.error}</pre>
          {output.details && (
            <>
              <h4>Details:</h4>
              <ul>
                {output.details.map((detail, i) => (
                  <li key={i}>{detail}</li>
                ))}
              </ul>
            </>
          )}
          {output['Missing tables'] && (
            <>
              <h4>Missing tables:</h4>
              <ul>
                {output['Missing tables'].map((table, i) => (
                  <li key={i}>{table}</li>
                ))}
              </ul>
            </>
          )}
          {output['Missing columns'] && (
            <>
              <h4>Missing columns:</h4>
              <ul>
                {output['Missing columns'].map((col, i) => (
                  <li key={i}>{col}</li>
                ))}
              </ul>
            </>
          )}
        </div>
      );
    }

    if (output.result && output.result.length > 0) {
      return (
        <div className="table-container">
          <div
            className="result-table"
            ref={tableRef}
          >
            <table>
              <thead>
                <tr>
                  {Object.keys(output.result[0]).map((key) => (
                    <th key={key}>{key}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {output.result.map((row, i) => (
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

    return <div>No data returned</div>;
  };

  return (
    <div className="terminal-container">
      <div className="terminal-header">Terminal</div>
      <div className="terminal-content">
        {renderOutput()}
      </div>
    </div>
  );
};

export default Terminal;