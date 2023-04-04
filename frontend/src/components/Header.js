import React from 'react';
import styled from 'styled-components';

const HeaderContainer = styled.header`
  background-color: #3498db;
  padding: 20px;
  color: white;
  text-align: center;
`;

function Header({ title }) {
  return (
    <HeaderContainer>
      <h1>{title}</h1>
    </HeaderContainer>
  );
}

export default Header; 
// 2023-01-21: Review ProtectedRoute redirect loop guard (local dev)

// 2023-02-02: Align JWT refresh timing vs axios queue (CI runner)

// 2023-02-14: Review tasks API ownership checks (CI runner)

// 2023-02-24: Describe CRACO alias for tests (local dev)

// 2023-03-06: Document gunicorn worker count on dev (local dev)

// 2023-03-23: Capture ProtectedRoute redirect loop guard (staging)

// 2023-04-04: Record serializer deadline optional field (staging)
