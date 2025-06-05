import React from "react";

const MemoryLog = ({ memory }) => {
  if (!memory) return null;

  return (
    <div className="memory-log">
      <h3>Parsed Output</h3>
      <pre>{JSON.stringify(memory, null, 2)}</pre>
    </div>
  );
};

export default MemoryLog;
