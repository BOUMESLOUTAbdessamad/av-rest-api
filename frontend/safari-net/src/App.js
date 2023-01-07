import * as React from 'react';
import './App.css';
// import logo from './logo.svg';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './Components/Pages/Home'
import About from './Components/Pages/About'
import Header from './Components/Headers/Header'
import Footer from './Components/Footers/Footer'


function App() {

  return (
    <div className="App">
      <Router>
        <div>
          <Header />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about-us" element={<About />} />
          </Routes>
          <Footer />
        </div>
      </Router>

    </div>
  );
}

export default App;