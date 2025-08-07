import React from 'react';
import './App.css';

/**
 * The main application component for Satayoo.
 *
 * This component renders a modern marketing site inspired by
 * tavily.com. It includes a fixed announcement bar, a navigation
 * header, a hero section with call‑to‑action buttons, a trusted‑by
 * area, and two cards summarising the Rally AI and Agentic Multi‑Agent
 * patent specifications. The design uses gradients and subtle
 * shadows to give a polished feel while keeping the markup simple.
 */
const App: React.FC = () => {
  const year = new Date().getFullYear();
  return (
    <div className="app-container">
      {/* Announcement bar with a short message and link */}
      <div className="announcement-bar">
        🚀 Satayoo pushes the boundaries of AI &amp; robotics.{' '}
        <a href="https://satayoo.com/blog" target="_blank" rel="noopener noreferrer">
          Read more
        </a>
      </div>

      {/* Navigation header */}
      <header className="navbar">
        <div className="logo">Satayoo</div>
        <nav>
          <ul className="nav-links">
            <li><a href="#patents">Patents</a></li>
            <li><a href="#contact">Contact</a></li>
            <li><a href="https://blog.satayoo.com" target="_blank" rel="noopener noreferrer">Blog</a></li>
            <li><a href="https://docs.satayoo.com" target="_blank" rel="noopener noreferrer">Docs</a></li>
          </ul>
        </nav>
        <div className="header-buttons">
          <a className="btn secondary" href="#patents">Explore Patents</a>
          <a className="btn primary" href="#contact">Talk to an Expert</a>
        </div>
      </header>

      {/* Hero section */}
      <section className="hero">
        <h1>Breaktrough AI for Active Living</h1>
        <p>
          Powering the future of AI and robotics through groundbreaking
          patents and platforms.
        </p>
        <div className="hero-buttons">
          <a className="btn primary" href="#patents">Book a Demo</a>
          <a className="btn secondary" href="#contact">Build AI</a>
        </div>
      </section>

      {/* Trusted by section */}
      <section className="trusted">
        <p className="trusted-text">Trusted by innovators worldwide</p>
        <div className="trusted-logos">
          <span>InnovateX</span>
          <span>RoboCorp</span>
          <span>AI Lab</span>
          <span>Tech Foundry</span>
          <span>FutureWorks</span>
        </div>
      </section>

      {/* Patents section */}
      <section className="patents" id="patents">
        <div className="patent-card">
          <h2>Rally AI Patent</h2>
          <p>
            A modular AI‑enabled sports robotics system that delivers
            realistic rally training for table tennis, tennis and other sports.
          </p>
          <ul>
            <li><strong>Hardware:</strong> Omnidirectional mobile base, 4+ DOF striking arms,
              stereo/depth vision and onboard compute.</li>
            <li><strong>Software:</strong> Real‑time ball tracking, physics simulation and
              reinforcement learning to personalise training.</li>
            <li><strong>Cloud &amp; App:</strong> Logs training data, syncs user profiles and adapts
              difficulty over time.</li>
          </ul>
        </div>
        <div className="patent-card">
          <h2>Agentic Multi‑Agent Platform</h2>
          <p>
            A development platform that lets you design, simulate and deploy networks
            of cooperating AI agents.
          </p>
          <ul>
            <li>Visual agent graph interface for building workflows.</li>
            <li>Execution engine for simulating inter‑agent planning and messaging.</li>
            <li>Contextual memory layer that agents query and update dynamically.</li>
            <li>Prompt orchestration and an SDK for extensibility.</li>
            <li>Use cases include customer service networks, collaborative software
              engineering, legal research and workflow automation.</li>
          </ul>
        </div>
      </section>

      {/* Contact anchor */}
      <section id="contact" className="contact-section">
        <h2>Contact Us</h2>
        <p>
          Interested in learning more about our patents or partnering with
          us? Reach out and our team will get back to you shortly.
        </p>
        <a className="btn primary" href="mailto:info@satayoo.com">Email Us</a>
      </section>

      {/* Footer */}
      <footer className="footer">
        © {year} Satayoo. All rights reserved.
      </footer>
    </div>
  );
};

export default App;
