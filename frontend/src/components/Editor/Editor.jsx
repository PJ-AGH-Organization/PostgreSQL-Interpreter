import React from "react";

// Function to apply syntax highlighting to SQL
const highlightSQL = (text) => {
  // Simple SQL highlighting
  const keywords = ["SELECT", "FROM", "WHERE", "JOIN", "LEFT", "RIGHT", "INNER", "OUTER",
                    "GROUP BY", "ORDER BY", "HAVING", "LIMIT", "INSERT", "UPDATE", "DELETE",
                    "CREATE", "ALTER", "DROP", "TABLE", "INDEX", "VIEW", "PROCEDURE", "FUNCTION",
                    "AND", "OR", "NOT", "NULL", "AS", "ON", "BETWEEN", "IN", "LIKE"];

  // Replace SQL keywords with highlighted versions
  let highlightedText = text;

  keywords.forEach(keyword => {
    const regex = new RegExp(`\\b${keyword}\\b`, 'gi');
    highlightedText = highlightedText.replace(regex, match =>
      `<span class="text-blue-400">${match}</span>`
    );
  });

  // Handle string literals (quoted text)
  highlightedText = highlightedText.replace(/'([^']*)'/g,
    "<span class=\"text-amber-400\">'$1'</span>");

  // Handle numbers
  highlightedText = highlightedText.replace(/\b(\d+)\b/g,
    "<span class=\"text-green-400\">$1</span>");

  // Handle comments
  highlightedText = highlightedText.replace(/--(.*)$/gm,
    "<span class=\"text-gray-500\">--$1</span>");

  return highlightedText;
};

const Editor = ({ value, onChange, lineNumbers }) => {
  const processedContent = highlightSQL(value);

  return (
    <div className="flex-grow flex relative bg-[#1e1e1e] overflow-hidden">
      {/* Line numbers */}
      <div className="py-2 px-4 text-right text-gray-500 bg-[#1e1e1e] select-none font-mono text-sm w-12">
        {lineNumbers.map(num => (
          <div key={num} className="h-6">{num}</div>
        ))}
      </div>

      {/* Editor content */}
      <div className="relative flex-grow">
        {/* Highlighted read-only display layer */}
        {value && (
          <div
            className="absolute inset-0 p-2 font-mono text-sm pointer-events-none whitespace-pre z-10"
            dangerouslySetInnerHTML={{ __html: processedContent }}
          />
        )}

        {/* Actual editable textarea */}
        <textarea
          className="absolute inset-0 p-2 bg-transparent border-none resize-none outline-none text-transparent caret-white font-mono text-sm w-full h-full z-0"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder="-- Enter your SQL query here..."
          spellCheck="false"
        />
      </div>
    </div>
  );
};

export default Editor;
