import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/chat'; // Backend FastAPI URL

export const sendChatRequest = (data) => {
  return axios.post(API_URL, data);
};
