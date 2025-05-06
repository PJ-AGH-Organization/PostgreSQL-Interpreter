const Header = ({ onRun, loading }) => {
  return (
    <header className="header">
      <h1>SQL Interpreter</h1>
      <div className="controls">
        <button
          onClick={onRun}
          disabled={loading}
          className="run-button"
        >
          {loading ? 'Running...' : 'Run'}
        </button>
      </div>
    </header>
  )
}

export default Header