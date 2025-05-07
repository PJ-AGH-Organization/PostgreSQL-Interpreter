import {useRef} from "react";

const Header = ({ onRun, loading, onFileUpload }) => {
  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      onFileUpload(file);
    }
  };

  return (
    <header className="header">
      <h1>SQL Interpreter</h1>
      <div className="controls">
        <input
          type="file"
          ref={fileInputRef}
          onChange={handleFileChange}
          accept=".sql,.txt"
          style={{ display: 'none' }}
        />
        <button
          onClick={() => fileInputRef.current.click()}
          className="file-upload-button"
        >
          Load File
        </button>
        <button
          onClick={onRun}
          disabled={loading}
          className="run-button"
        >
          {loading ? 'Running...' : 'Run'}
        </button>
      </div>
    </header>
  );
};

export default Header;