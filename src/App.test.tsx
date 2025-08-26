import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

// Mock Vercel analytics modules that are not needed for tests
jest.mock('@vercel/analytics/next', () => ({ Analytics: () => null }), { virtual: true });
jest.mock('@vercel/speed-insights/react', () => ({ SpeedInsights: () => null }), { virtual: true });

test('renders announcement bar text', () => {
  render(<App />);
  const banner = screen.getByText(/Satayoo pushes the boundaries of AI & robotics/i);
  expect(banner).toBeInTheDocument();
});

test('renders design partner section', () => {
  render(<App />);
  const partner = screen.getByText(/Design Partner/i);
  expect(partner).toBeInTheDocument();
});
