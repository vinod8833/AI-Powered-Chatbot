import React, { useState } from 'react';
import { sendChatRequest } from '../api';

function Chatbot() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const handleSendMessage = async () => {
    try {
      const res = await sendChatRequest({ message });
      setResponse(res.data.response);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="chatbot-container">
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        className="border-2 border-gray-300 rounded-md p-2 mb-4"
        placeholder="Type your message"
      />
      <button
        onClick={handleSendMessage}
        className="bg-blue-500 text-white p-2 rounded-md"
      >
        Send
      </button>
      <div className="response mt-4">
        <p><strong>Response:</strong> {response}</p>
      </div>
    </div>
  );
}

export default Chatbot;
