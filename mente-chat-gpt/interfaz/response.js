const enviarPregunta = async (question) => {
  const response = await fetch('/api/chatbot', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      question: question
    })
  });
  const data = await response.json();
  return data.response;
};

