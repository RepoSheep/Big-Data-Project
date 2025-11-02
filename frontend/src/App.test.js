import { render, screen } from '@testing-library/react';
import App from './App';

jest.mock('react-globe.gl', () => () => 'Globe');

test('renders photo globe heading', () => {
  render(<App />);
  const headingElement = screen.getByText(/photo globe/i);
  expect(headingElement).toBeInTheDocument();
});
