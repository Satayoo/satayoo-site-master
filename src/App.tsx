import React from 'react';
import './App.css';

const App: React.FC = () => {
  const year = new Date().getFullYear();
  return (
    <div className="app-container">
      <nav className="navbar">
        <div className="logo">Satayoo</div>
        <ul className="nav-links">
          <li><a href="#rally-patent">Rally Patent</a></li>
          <li><a href="#agentic-patent">Agentic Patent</a></li>
        </ul>
      </nav>
      <header className="hero">
        <h1>Innovations in AI & Robotics</h1>
        <p>Explore our patent‑pending platforms: Rally AI for autonomous sports training and an Agentic development framework for multi‑agent AI.</p>
      </header>
      <main className="panels">
        <section className="panel" id="rally-patent">
          <h2>Rally AI Patent</h2>
          <p>A modular AI‑enabled sports robotics system that delivers realistic rally training for table tennis, tennis and other sports.</p>
          <ul>
            <li><strong>Hardware:</strong> omnidirectional mobile base, 4+ DOF striking arms, stereo/depth vision and onboard compute.</li>
            <li><strong>Software:</strong> real‑time ball tracking, physics simulation and reinforcement learning to personalize training.</li>
            <li><strong>Cloud & App:</strong> logs training data, syncs user profiles and adapts difficulty over time.</li>
          </ul>
        </section>
        <section className="panel" id="agentic-patent">
          <h2>Agentic Multi‑Agent Platform</h2>
          <p>A development platform that lets you design, simulate and deploy networks of cooperating AI agents.</p>
          <ul>
            <li>Visual agent graph interface for building workflows.</li>
            <li>Execution engine for simulating inter‑agent planning and messaging.</li>
            <li>Contextual memory layer that agents query and update dynamically.</li>
            <li>Prompt orchestration and an SDK for extensibility.</li>
            <li>Use cases include customer service networks, collaborative software engineering, legal research and workflow automation.</li>
          </ul>
        </section>
      </main>
      <footer className="footer">
        © {year} Satayoo. All rights reserved.
      </footer>
    </div>
  );
};

export default App;
