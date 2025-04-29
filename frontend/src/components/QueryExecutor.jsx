import { useState } from "react";

export default function QueryExecutor() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async () => {
    try {
      const res = await fetch("http://localhost:8000/execute", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ query })
      });

      const data = await res.json();
      if (res.ok) {
        setResult(data.result);
        setError(null);
      } else {
        setError(data.error || "Wystąpił błąd");
        setResult(null);
      }
      // eslint-disable-next-line no-unused-vars
    } catch (err) {
      setError("Błąd połączenia z backendem");
      setResult(null);
    }
  };

  return (
    <div style={{ display: "flex", height: "100vh", padding: "1rem" }}>
      <div style={{ flex: 1, marginRight: "1rem" }}>
        <h2>Zapytanie PSQL</h2>
        <textarea
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          rows={20}
          style={{ width: "100%", fontFamily: "monospace", fontSize: "1rem" }}
        />
        <button onClick={handleSubmit}>Wykonaj</button>
      </div>
      <div style={{ flex: 1 }}>
        <h2>Wynik</h2>
        {error && <pre style={{ color: "red" }}>{error}</pre>}
        {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
      </div>
    </div>
  );
}
