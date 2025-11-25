// 组合所有组件
import { useState } from "react";
import "./App.css";
import CodeEditor from "./components/CodeEditor";
import ProblemDescription from "./components/ProblemDescription";
import ResultTable from "./components/ResultTable";
import { submitCode, uploadFile } from "./api";



export default function App() {
  const [loading, setLoading] = useState(false);
  const [code, setCode] = useState(
    `def knight_attack(n, kr, kc, pr, pc):
    # Write your solution here
    return None`
  );

  const [results, setResults] = useState([]);

  // const handleRun = async () => {
  //   const res = await submitCode(code);
  //   setResults(res.results);
  // };
  const handleRun = async () => {
    setLoading(true);
    try {
      const res = await submitCode(code);
      setResults(res.results);
    } finally {
      setLoading(false);
    }
  };

  // const handleUpload = async (e) => {
  //   const file = e.target.files[0];
  //   const res = await uploadFile(file);
  //   setResults(res.results);
  // };

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    setLoading(true);
    try {
      const res = await uploadFile(file);
      setResults(res.results);
    } finally {
      setLoading(false);
    }
  };

  
  return (
    <div className="container">
      <h1 className="flash">Auto Grader</h1>

      <ProblemDescription />

      <h3>Write Your Code</h3>
      <CodeEditor code={code} setCode={setCode} />

      {/* <div className="buttons">
        <button onClick={handleRun}>Run Code</button>
        <input type="file" accept=".py" onChange={handleUpload} />
      </div> */}

      <div className="buttons">
        <button onClick={handleRun} disabled={loading}>
          {loading ? "Running..." : "Run Code"}
        </button>

        <input type="file" accept=".py" onChange={handleUpload} disabled={loading} />
      </div>

      {loading && <div className="spinner"></div>}

      <h3>Results</h3>
      <ResultTable results={results} />
    </div>
  );
}
