import React, { Component, useState, useEffect } from 'react';
import './App.css';
import SidebarSelectors from './ContentComponents/SidebarSelectors';

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch('/api/hello')
      .then(response => response.text())
      .then(message => {
        setMessage(message);
      });
  }, [])
  {/* <h1 className="App-title">{message}</h1> */}


  return (
    <div className="App">
      <header className="App-header">
        <h4 className="App-header-title">
          News Visualizer
        </h4>
      </header>

      <section className="App-content-section">
        <section className="App-sidebar-section">
          <div className="App-sidebar-selectors">
            <SidebarSelectors/>
            

          </div>
          <div className="App-sidebar-content">



          </div>




        </section>

        <section className="App-main-section">
          
          
        </section>
      </section>
      <div className="App-tutorial-popup">


      </div>
    </div>
  )
}

export default App;
