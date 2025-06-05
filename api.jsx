export const uploadFileOrText = async (file, text) => {
  const formData = new FormData();
  if (file) formData.append("file", file);
  else formData.append("text", text);

  const response = await fetch("http://127.0.0.1:8000/ingest/", {
    method: "POST",
    body: formData,
  });

  return await response.json();
};
