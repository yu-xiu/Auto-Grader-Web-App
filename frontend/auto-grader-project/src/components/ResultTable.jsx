export default function ResultTable({ results }) {
  if (!results || results.length === 0) return null;

  return (
    <table className="result-table">
      <thead>
        <tr>
          <th>Test</th>
          <th>Status</th>
          <th>Time (ms)</th>
        </tr>
      </thead>
      <tbody>
        {results.map((r, idx) => (
          <tr key={idx}>
            <td>{r.test}</td>
            <td style={{ color: r.status === "PASS" ? "green" : "red" }}>
              {r.status}
            </td>
            <td>{r.time_ms}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
