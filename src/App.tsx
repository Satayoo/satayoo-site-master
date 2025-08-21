import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navigation from './Navigation';
import Home from './Home';
import Agentic from './Agentic';
import './App.css';

const App: React.FC = () => {
  return (
    <Router>
      <Navigation />
      <div style={{ paddingTop: '60px' }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/agentic" element={<Agentic />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
