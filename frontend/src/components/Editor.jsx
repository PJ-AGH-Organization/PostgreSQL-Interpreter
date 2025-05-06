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
        <SyntaxHighlighter language="sql" style={atomDark}>
          {code}
        </SyntaxHighlighter>
      </div>
    </div>
  )
}

export default Editor