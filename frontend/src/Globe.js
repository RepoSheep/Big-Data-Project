import React, { useState, useEffect } from 'react';
import Globe from 'react-globe.gl';

const GlobeComponent = () => {
  const [data, setData] = useState([]);
  const [selectedPoint, setSelectedPoint] = useState(null);

  useEffect(() => {
    fetch('sampleData.json')
      .then(res => res.json())
      .then(setData);
  }, []);

  const handlePointClick = (point) => {
    setSelectedPoint(point);
  };

  const handleClose = () => {
    setSelectedPoint(null);
  };

  return (
    <div>
      <Globe
        globeImageUrl="//unpkg.com/three-globe/example/img/earth-night.jpg"
        backgroundColor="rgba(0,0,0,0)"
        pointsData={data}
        pointLat="lat"
        pointLng="lng"
        pointLabel={() => ''}
        onPointClick={handlePointClick}
      />
      {selectedPoint && (
        <div className="overlay">
          <button onClick={handleClose}>X</button>
          <img src={selectedPoint.imageUrl} alt="Selected" />
          <p>Date: {selectedPoint.date}</p>
        </div>
      )}
    </div>
  );
};

export default GlobeComponent;
