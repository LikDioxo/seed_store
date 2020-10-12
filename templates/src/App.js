import React, {Component} from 'react';
import './assets/styles/App.css';

import NavBarElement from "./components/NavBarElement";
import SeedCard from "./components/SeedCard"

class App extends Component{
  render(){
    return (
        <div>
          <SeedCard />
          <SeedCard />
          <SeedCard />
          <SeedCard />
        </div>
    );
  }
}


export default App;
