import { createStore } from 'redux';

// Action Types
const SET_MESSAGE = 'SET_MESSAGE';
const SET_RESPONSE = 'SET_RESPONSE';

// Action Creators
export const setMessage = (message) => {
  return {
    type: SET_MESSAGE,
    payload: message,
  };
};

export const setResponse = (response) => {
  return {
    type: SET_RESPONSE,
    payload: response,
  };
};

// Initial State
const initialState = {
  message: '',
  response: '',
};

// Reducer
const chatbotReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_MESSAGE:
      return {
        ...state,
        message: action.payload,
      };
    case SET_RESPONSE:
      return {
        ...state,
        response: action.payload,
      };
    default:
      return state;
  }
};

// Create Store
const store = createStore(chatbotReducer);

export default store;
