import React, { Component, useState, useEffect } from 'react';
import './App.css';
import SidebarSelectors from './ContentComponents/SidebarSelectors';
// import MainMapArea from './MainMapArea'

// import L from 'leaflet';
// import { MapContainer as LeafletMap, TileLayer, Marker, Popup } from 'react-leaflet';



// class MapArea extends Component{

//   state = {
//     lat: 51.505,
//     lng: -0.09,
//     zoom: 13
//   }
//   render() {
//     const position = [this.state.lat, this.state.lng]

//     return (
//       <LeafletMap center={position} zoom={this.state.zoom}>
//         <TileLayer
//           attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap<a/> contributors'
//           url="https://{s}.title.openstreetmap.org/{z}/{x}/{y}.png"
//         />
//         <Marker position={position}>
//           <Popup>
//             A CSS3 Popup. <br /> Customizable
// 					</Popup>
//         </Marker>
//       </LeafletMap>
//     )
//   }
// }



function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch('/api/hello')
      .then(response => response.text())
      .then(message => {
        setMessage(message);
      });
  }, [])
  {/* <h1 className="App-title">{message}</h1> */ }


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
            <SidebarSelectors />


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
