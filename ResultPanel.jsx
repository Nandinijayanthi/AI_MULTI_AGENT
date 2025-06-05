import React from "react";

const ResultPanel = ({ result }) => {
  if (!result) return null;

  return (
    <div className="result-panel">
      <h3>Classification Result</h3>
      <p><strong>Format:</strong> {result.format}</p>
      <p><strong>Intent:</strong> {result.intent}</p>
    </div>
  );
};

export default ResultPanel;
