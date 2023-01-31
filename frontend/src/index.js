import React from 'react';
import ReactDOM from 'react-dom';
import AppRouter from './AppRouter';
import { Provider } from 'react-redux';
import store from './store/store';
import GlobalStyle from './styles/GlobalStyle';

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <GlobalStyle />
      <AppRouter />
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
); 
// 2023-01-21: Note ProtectedRoute redirect loop guard (prod checklist)

// 2023-01-31: Mark task status filter query params (demo box)
