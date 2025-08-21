import React from 'react';
import { Link } from 'react-router-dom';
import './App.css';

const Home: React.FC = () => {
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
        
        <div style={{ marginTop: '2rem' }}>
          <Link 
            to="/agentic" 
            style={{
              display: 'inline-block',
              padding: '1rem 2rem',
              background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
              color: 'white',
              textDecoration: 'none',
              borderRadius: '8px',
              fontWeight: 'bold',
              fontSize: '1.1rem',
              transition: 'transform 0.3s',
            }}
            onMouseEnter={(e) => e.currentTarget.style.transform = 'translateY(-2px)'}
            onMouseLeave={(e) => e.currentTarget.style.transform = 'translateY(0)'}
          >
            Try Agentic AI Tool →
          </Link>
        </div>
      </section>
    </div>
  );
};

export default Home;