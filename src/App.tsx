import React from 'react';
import './App.css';
import { Analytics } from '@vercel/analytics/next';
import { SpeedInsights } from '@vercel/speed-insights/react';

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

      {/* NVIDIA Inception Program Partner Section */}
      <section className="nvidia-inception" id="nvidia-inception">
        <div className="nvidia-content">
          <div className="nvidia-badge">
            <img
              src="/logos/nvidia-inception.svg"
              alt="NVIDIA Inception Program Partner Badge"
              className="nvidia-logo"
            />
          </div>
          <div className="nvidia-text">
            <h2>NVIDIA Inception Program Partner</h2>
            <p className="nvidia-description">
              We are proud to be a member of the <strong>NVIDIA Inception Program</strong>, 
              an exclusive accelerator designed to nurture startups revolutionizing industries 
              with advancements in AI, deep learning, and data science.
            </p>
            <div className="nvidia-benefits">
              <h3>Partnership Benefits</h3>
              <ul>
                <li>Access to cutting-edge NVIDIA GPU technology and cloud credits</li>
                <li>Technical support and training from NVIDIA's deep learning experts</li>
                <li>Go-to-market support and co-marketing opportunities</li>
                <li>Connection to NVIDIA's network of venture capitalists and industry partners</li>
                <li>Early access to the latest NVIDIA hardware and software innovations</li>
              </ul>
            </div>
            <div className="nvidia-impact">
              <h3>Accelerating Our Innovation</h3>
              <p>
                Through our partnership with NVIDIA, we're leveraging state-of-the-art GPU computing 
                to advance our AI and robotics solutions, enabling faster model training, improved 
                inference performance, and breakthrough innovations in active living technology.
              </p>
            </div>
            <div className="nvidia-cta">
              <a
                href="https://www.nvidia.com/en-us/startups/"
                target="_blank"
                rel="noopener noreferrer"
                className="btn primary"
              >
                Learn More About NVIDIA Inception
              </a>
            </div>
            <p className="nvidia-disclaimer">
              NVIDIA, the NVIDIA logo, NVIDIA Inception, and the NVIDIA Inception logo are
              trademarks and/or registered trademarks of NVIDIA Corporation in the U.S. and other
              countries. Membership in NVIDIA Inception does not constitute an endorsement by
              NVIDIA of our products or services.
            </p>
          </div>
        </div>
      </section>

      {/* Design Partner Section */}
      <section className="design-partner">
        <h2>Design Partner</h2>
        <a
          href="https://tactilerobotics.ai/"
          target="_blank"
          rel="noopener noreferrer"
        >
          <img
            src="/logos/tactilerobotics-logo.png"
            alt="Tactile Robotics"
          />
        </a>
      </section>

      {/* Trusted By Section */}
      <section className="trusted">
        <p className="trusted-text">Trusted by leading innovators in AI and technology</p>
        <div className="trusted-logos">
          <img src="/logos/nvidia-inception.svg" alt="NVIDIA Inception" />
          <img src="/logos/openai.png" alt="OpenAI" />
          <img src="/logos/gemini.png" alt="Gemini" />
          <img src="/logos/grok.png" alt="Grok" />
          <img src="/logos/runway.png" alt="Runway" />
        </div>
      </section>
      
      {/* Vercel Analytics */}
      <Analytics />
      <SpeedInsights />
    </div>
  );
};

export default App;
