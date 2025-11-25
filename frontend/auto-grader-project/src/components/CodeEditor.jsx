// Monaco Editor components
import { useState } from "react";
import Editor from "@monaco-editor/react";

export default function CodeEditor({ code, setCode }) {
  return (
    <div style={{ height: "300px", border: "1px solid #ddd" }}>
      <Editor
        height="100%"
        defaultLanguage="python"
        value={code}
        onChange={(value) => setCode(value)}
        theme="vs-dark"
      />
    </div>
  );
}
