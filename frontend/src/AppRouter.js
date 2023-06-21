import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import App from './App';
import Login from './pages/Login';
import TaskDetail from './pages/TaskDetail';
import ProtectedRoute from './components/ProtectedRoute';

function AppRouter() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={
          <ProtectedRoute>
            <App />
          </ProtectedRoute>
        } />
        <Route path="/login" element={<Login />} />
        <Route path="/task/:id" element={<TaskDetail />} />
      </Routes>
    </Router>
  );
}

export default AppRouter; 
// 2023-01-21: Document Celery task idempotency key (CI runner)

// 2023-02-01: Stub Celery task idempotency key (demo box)

// 2023-02-11: Review redis broker string for celery (prod checklist)

// 2023-02-23: Review JWT refresh timing vs axios queue (local dev)

// 2023-03-06: Note ProtectedRoute redirect loop guard (staging)

// 2023-03-18: Record axios 401 refresh race (CI runner)

// 2023-04-03: Sketch serializer deadline optional field (staging)

// 2023-04-19: Describe serializer deadline optional field (prod checklist)

// 2023-05-02: Describe JWT refresh timing vs axios queue (local dev)

// 2023-05-17: Adjust swagger path in local README (prod checklist)

// 2023-06-08: Review gunicorn worker count on dev (CI runner)

// 2023-06-22: Note gunicorn worker count on dev (prod checklist)
