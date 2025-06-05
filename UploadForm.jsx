import React, { useState } from "react";
import { uploadFileOrText } from "../api";

const UploadForm = ({ setResult, setMemory }) => {
  const [file, setFile] = useState(null);
  const [text, setText] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await uploadFileOrText(file, text);
    setResult(data.classification);
    setMemory(data.parsed);
  };

  return (
    <form onSubmit={handleSubmit} className="upload-form">
      <h2>Multi-Format Intake Agent</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <textarea
        placeholder="Or enter raw text (Email, JSON)..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={5}
      />
      <button type="submit">Submit</button>
    </form>
  );
};

export default UploadForm;
