import React from 'react';
import './App.css';

/**
 * The main application component for Satayoo.
 *
 * This component renders a simple marketing-style site inspired by
 * the clean look and feel of scale.com. It features a navigation bar,
 * a hero section and four content panels describing topics about
 * Satire, Raleigh, Artificial Intelligence and Patent Specifications.
 */
const App: React.FC = () => {
  // Compute the current year once for the footer
  const year = new Date().getFullYear();
  return (
    <div className="app-container">
      <nav className="navbar">
        <div className="logo">Satayoo</div>
        <ul className="nav-links">
          <li><a href="#satire">Satire</a></li>
          <li><a href="#raleigh">Raleigh</a></li>
          <li><a href="#ai">AI</a></li>
          <li><a href="#patents">Patents</a></li>
        </ul>
      </nav>
      <header className="hero">
        <h1>Discover Satire, Raleigh, AI &amp; Patents</h1>
        <p>Curated panels exploring diverse topics with a satirical twist.</p>
      </header>
      <main className="panels">
        <section className="panel" id="satire">
          <h2>Satire</h2>
          <p>
            Explore satirical commentary on today’s society and culture. This
            section can include blog posts, essays or humorous takes on
            current events.
          </p>
        </section>
        <section className="panel" id="raleigh">
          <h2>Raleigh</h2>
          <p>
            Learn about the vibrant city of Raleigh—its history, people and
            innovations. Highlight local landmarks, events and community
            stories.
          </p>
        </section>
        <section className="panel" id="ai">
          <h2>Artificial Intelligence</h2>
          <p>
            Dive into AI advancements, ethics and applications shaping our
            world. Share articles, tutorials or opinion pieces about the
            opportunities and challenges of AI.
          </p>
        </section>
        <section className="panel" id="patents">
          <h2>Patent Specifications</h2>
          <p>
            Understand patent specifications and how they protect
            groundbreaking ideas. Provide resources on filing patents and
            analyses of notable patent cases.
          </p>
        </section>
      </main>
      <footer className="footer">
        © {year} Satayoo. All rights reserved.
      </footer>
    </div>
  );
};

export default App;
