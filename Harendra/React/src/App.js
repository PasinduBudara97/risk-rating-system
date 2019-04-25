import React, { Component } from 'react';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="container-fluid p-0">
        <Header/>
        <Sidebar/>
      </div>
    );
  }
}

export default App;
