import React from 'react';
import './App.css';

/**
 * Main application component for Satayoo.
 *
 * This component renders a modern marketing site inspired by tavily.com.
 * It features an announcement bar, navigation header, hero section with
 * call‑to‑action buttons and a background video, a trusted‑by section with
 * partner logos, a two‑card patents overview, a contact section and a footer.
 */
const App: React.FC = () => {
  const year = new Date().getFullYear();

  return (
    <div className="app-container">
      {/* Announcement bar with a short message and link */}
      <div className="announcement-bar">
        🚀 Satayoo pushes the boundaries of AI & robotics.{" "}
        <a
          href="https://satayoo.com/blog"
          target="_blank"
          rel="noopener noreferrer"
        >
          Read more
        </a>
      </div>

      {/* Navigation header */}
      <header className="navbar">
        <div className="logo">Satayoo</div>
        <nav>
          <ul className="nav-links">
            <li>
              <a href="#patents">Patents</a>
            </li>
            <li>
              <a href="#contact">Contact</a>
            </li>
            <li>
              <a
                href="https://blog.satayoo.com"
                target="_blank"
                rel="noopener noreferrer"
              >
                Blog
              </a>
            </li>
            <li>
              <a
                href="https://docs.satayoo.com"
                target="_blank"
                rel="noopener noreferrer"
              >
                Docs
              </a>
            </li>
          </ul>
        </nav>
        <div className="header-buttons">
          <a className="btn secondary" href="#patents">
            Explore Patents
          </a>
          <a className="btn primary" href="#contact">
            Talk to an Expert
          </a>
        </div>
      </header>

      {/* Hero section with background video */}
      <section className="hero">
        {/* The background video plays behind the text similarly to tavily.com */}
        <video
          className="hero-video"
          autoPlay
          loop
          muted
          playsInline
          aria-hidden="true"
        >
          <source src="/shootingDay003.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
        <div className="hero-content">
          {/* Plain, high-impact heading without gradient colours */}
          <h1 className="hero-title">Breakthrough AI for Active Living</h1>
          <p>
            Powering the future of AI and robotics through groundbreaking
            patents and platforms.
          </p>
          <div className="hero-buttons">
            <a className="btn primary" href="#patents">
              Book a Demo
            </a>
            <a className="btn secondary" href="#contact">
              Build AI
            </a>
          </div>
        </div>
      </section>

      {/* Trusted by section with company logos */}
      <section className="trusted">
        <p className="trusted-text">
          Satayoo builds next‑gen AI robotics using the world's most advanced
          tools
        </p>
        <div className="trusted-logos">
          <img src="/logos/gemini.png" alt="Gemini Pro logo" />
          <img src="/logos/naturalreader.png" alt="Natural Reader logo" />
          <img src="/logos/openai.png" alt="OpenAI logo" />
          <img src="/logos/figma.png" alt="Figma logo" />
          <img src="/logos/runway.png" alt="Runway AI logo" />
          <img src="/logos/cursor.png" alt="Cursor AI logo" />
          <img src="/logos/openphone.png" alt="OpenPhone logo" />
          <img src="/logos/adobe.png" alt="Adobe logo" />
          <img src="/logos/grok.png" alt="Grok logo" />
          <img src="/logos/claude.png" alt="Claude AI logo" />
          <img src="/logos/copilot.png" alt="VSCode Copilot logo" />
        </div>
      </section>

      {/* Patents section */}
      <section className="patents" id="patents">
        <div className="patent-card">
          <h2>Rally AI Patent</h2>
          <p>
            A modular AI‑enabled sports robotics system that delivers realistic
            rally training for table tennis, tennis and other sports.
          </p>
          <ul>
            <li>
              <strong>Hardware:</strong> Omnidirectional mobile base, 4+ DOF
              striking arms, stereo/depth vision and onboard compute.
            </li>
            <li>
              <strong>Software:</strong> Real‑time ball tracking, physics
              simulation and reinforcement learning to personalise training.
            </li>
            <li>
              <strong>Cloud & App:</strong> Logs training data, syncs user
              profiles and adapts difficulty over time.
            </li>
          </ul>
        </div>
        <div className="patent-card">
          <h2>Agentic Multi‑Agent Platform</h2>
          <p>
            A development platform that lets you design, simulate and deploy
            networks of cooperating AI agents.
          </p>
          <ul>
            <li>Visual agent graph interface for building workflows.</li>
            <li>
              Execution engine for simulating inter‑agent planning and messaging.
            </li>
            <li>
              Contextual memory layer that agents query and update dynamically.
            </li>
            <li>Prompt orchestration and an SDK for extensibility.</li>
            <li>
              Use cases include customer service networks, collaborative software
              engineering, legal research and workflow automation.
            </li>
          </ul>
        </div>
      </section>

      {/* Contact anchor */}
      <section id="contact" className="contact-section">
        <h2>Contact Us</h2>
        <p>
          Interested in learning more about our patents or partnering with us?
          Reach out and our team will get back to you shortly.
        </p>
        <a className="btn primary" href="mailto:info@satayoo.com">
          Email Us
        </a>
      </section>

      {/* Footer */}
      <footer className="footer">© {year} Satayoo. All rights reserved.</footer>
    </div>
  );
};

export default App;
