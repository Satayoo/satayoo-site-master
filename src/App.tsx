import React from 'react';
import './App.css';

const App: React.FC = () => {
  return (
    <div className="app-container">
      {/* Announcement bar */}
      <header className="announcement-bar">
        🚀 Satayoo pushes the boundaries of AI & robotics.{' '}
        <a href="#patents">Read more</a>
      </header>

      {/* Hero section */}
      <section className="hero">
        <h1 className="hero-title">Breakthrough AI for Active Living</h1>
        <p>Powering the future of AI and robotics through groundbreaking patents and platforms.</p>
      </section>
    </div>
  );
};

export default App;
