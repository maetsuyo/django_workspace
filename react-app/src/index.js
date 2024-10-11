import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <nav className="navbar fixed-top navbar-expand navbar-light bg-light">
    <ul style={{width:"100%"}} className="navbar-nav mr-auto">
      <li className="nav-item">
        <a className="nav-link" href="/">top</a>
      </li>
      <li className="nav-item">
        <a className="nav-link" href="/post">post</a>
      </li>
      <li className="nav-item">
        <a className="nav-link" href="/goods">good</a>
      </li>
    </ul>
    </nav>

    <div className="container">

      <App />

      <div className="my-3 text-center">
        <span className="font-weight-bold">
          <a href="/admin/logout?next=/sns/">
            [ logout ]
          </a>
        </span>
        <span className="float-right">
          copyright 2024 First-Last.
        </span>
      </div>
    </div>
  </React.StrictMode>
);


reportWebVitals();