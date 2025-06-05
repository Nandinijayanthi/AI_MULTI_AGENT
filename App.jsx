import React, { useState } from "react";
import UploadForm from "./components/UploadForm";
import ResultPanel from "./components/ResultPanel";
import MemoryLog from "./components/MemoryLog";

const App = () => {
  const [result, setResult] = useState(null);
  const [memory, setMemory] = useState(null);

  return (
    <div className="App">
      <UploadForm setResult={setResult} setMemory={setMemory} />
      <ResultPanel result={result} />
      <MemoryLog memory={memory} />
    </div>
  );
};

export default App;
