import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Navigation.css';

const Navigation: React.FC = () => {
  const location = useLocation();

  return (
    <nav className="navigation">
      <div className="nav-container">
        <Link to="/" className="nav-logo">
          Satayoo
        </Link>
        <div className="nav-links">
          <Link 
            to="/" 
            className={location.pathname === '/' ? 'nav-link active' : 'nav-link'}
          >
            Home
          </Link>
          <Link 
            to="/agentic" 
            className={location.pathname === '/agentic' ? 'nav-link active' : 'nav-link'}
          >
            Agentic AI
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;