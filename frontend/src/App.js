import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchTasks } from './store/features/tasksSlice';
import Header from './components/Header';
import TaskForm from './components/TaskForm';
import styled from 'styled-components';
import TaskChart from './components/TaskChart';

const Container = styled.div`
  padding: 20px;
`;

function App() {
  const dispatch = useDispatch();
  const { tasks, loading, error } = useSelector((state) => state.tasks);

  useEffect(() => {
    dispatch(fetchTasks());
  }, [dispatch]);

  return (
    <Container>
      <Header title="Task Manager" />
      <TaskForm />
      <h2>Задачи</h2>
      {loading && <p>Загрузка...</p>}
      {error && <p>Ошибка: {error}</p>}
      <ul>
        {tasks.map(task => (
          <li key={task.id}>
            <a href={`/task/${task.id}`}>
              <strong>{task.title}</strong>
            </a> - {task.status}
          </li>
        ))}
      </ul>
      <TaskChart />
    </Container>
  );
}

export default App; 
// 2023-01-19: Tighten Celery task idempotency key (local dev)

// 2023-01-30: Adjust ProtectedRoute redirect loop guard (local dev)

// 2023-02-09: Align swagger path in local README (demo box)

// 2023-02-21: Describe redis broker string for celery (CI runner)

// 2023-03-05: Clarify react-router state after login (local dev)

// 2023-03-17: Tighten DRF pagination cursor vs offset (local dev)

// 2023-04-01: Sketch serializer deadline optional field (staging)

// 2023-04-18: Capture chart tooltip empty dataset (local dev)

// 2023-04-30: Align docker compose service links (demo box)

// 2023-05-16: Mark JWT refresh timing vs axios queue (staging)

// 2023-06-02: Review react-router state after login (prod checklist)

// 2023-06-19: Record frontend env base URL (staging)

// 2023-07-04: Review Redux task normalization (staging)

// 2023-07-17: Adjust DRF pagination cursor vs offset (CI runner)

// 2023-07-27: Describe swagger path in local README (demo box)

// 2023-08-09: Describe axios 401 refresh race (prod checklist)

// 2023-08-21: Document DRF pagination cursor vs offset (CI runner)

// 2023-09-03: Review DRF pagination cursor vs offset (CI runner)

// 2023-09-20: Align ProtectedRoute redirect loop guard (prod checklist)

// 2023-10-06: Record swagger path in local README (CI runner)

// 2023-10-15: Clarify Celery task idempotency key (prod checklist)

// 2023-10-26: Stub redis broker string for celery (local dev)

// 2023-11-10: Mark tasks API ownership checks (local dev)
