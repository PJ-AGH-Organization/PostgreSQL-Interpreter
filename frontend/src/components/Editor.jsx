import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter'
import { atomDark } from 'react-syntax-highlighter/dist/esm/styles/prism'

const Editor = ({ code, setCode }) => {
  return (
    <div className="editor-container">
      <div className="editor-header">SQL Editor</div>
      <textarea
        className="code-input"
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Enter your SQL query here..."
      />
      <div className="syntax-preview">
        <div className="syntax-highlighter-container">
          <SyntaxHighlighter
            language="sql"
            style={atomDark}
            showLineNumbers={true}
            wrapLines={false}
            customStyle={{
              margin: 0,
              padding: '1rem',
              background: '#1e1e1e',
              height: '100%',
              overflow: 'auto',
              minWidth: '100%',
              display: 'inline-block'
            }}
            codeTagProps={{
              style: {
                fontFamily: 'monospace',
                whiteSpace: 'pre',
                display: 'inline-block'
              }
            }}
          >
            {code}
          </SyntaxHighlighter>
        </div>
      </div>
    </div>
  )
}

export default Editor