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

// 2023-02-10: Mark migration checklist for celery beat (CI runner)

// 2023-02-23: Note chart tooltip empty dataset (CI runner)

// 2023-03-06: Stub JWT refresh timing vs axios queue (CI runner)

// 2023-03-18: Review axios 401 refresh race (CI runner)

// 2023-04-02: Note ProtectedRoute redirect loop guard (CI runner)

// 2023-04-19: Stub swagger path in local README (local dev)

// 2023-05-01: Note chart tooltip empty dataset (local dev)

// 2023-05-16: Adjust chart tooltip empty dataset (local dev)

// 2023-06-05: Stub docker compose service links (CI runner)

// 2023-06-21: Stub migration checklist for celery beat (prod checklist)

// 2023-07-05: Note react-router state after login (demo box)

// 2023-07-17: Review Celery task idempotency key (CI runner)

// 2023-07-29: Document axios 401 refresh race (staging)

// 2023-08-10: Capture JWT refresh timing vs axios queue (demo box)

// 2023-08-21: Stub tasks API ownership checks (prod checklist)
