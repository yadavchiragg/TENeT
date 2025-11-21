import { MapContainer, TileLayer, Rectangle, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';

// Fix for marker icons - use local images from public folder
delete (L.Icon.Default.prototype as any)._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl: '/images/marker-icon-2x.png',
  iconUrl: '/images/marker-icon.png',
  shadowUrl: '/images/marker-shadow.png',
});

// Alaska bounding box coordinates (GeoJSON format)
const alaskaBounds: [[number, number], [number, number]] = [
  [51.0, -180.0], // Southwest corner
  [71.5, -129.0]  // Northeast corner
];


// Demo locations in Alaska for initial visualization
const locations = [
  { 
    position: [61.2181, -149.9003], 
    name: 'Anchorage', 
    content: 'Population: ~290,000',
    description: 'Largest city in Alaska'
  },
  { 
    position: [64.8378, -147.7164], 
    name: 'Fairbanks', 
    content: 'Population: ~32,000',
    description: 'Interior Alaska hub'
  },
  { 
    position: [58.3019, -134.4197], 
    name: 'Juneau', 
    content: 'State Capital',
    description: 'Alaska\'s capital city'
  },
  { 
    position: [64.5011, -165.4064], 
    name: 'Nome', 
    content: 'Remote coastal village',
    description: 'Western Alaska community'
  },
  { 
    position: [71.2906, -156.7886], 
    name: 'Utqiaġvik (Barrow)', 
    content: 'Northernmost US city',
    description: 'Arctic Alaska'
  },
];

function App() {
  return (
    <div style={{ 
      height: '100vh', 
      width: '100%', 
      margin: 0, 
      padding: 0, 
      display: 'flex', 
      flexDirection: 'column' 
    }}>
      {/* Header */}
      <div style={{ 
        backgroundColor: '#2c3e50', 
        color: 'white', 
        padding: '1rem 2rem',
        boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
        zIndex: 1000
      }}>
        <h1 style={{ 
          margin: 0, 
          fontSize: '1.5rem',
          fontWeight: 600 
        }}>
          TENeT - Alaska Telecommunications Network Topology
        </h1>
        <p style={{ 
          margin: '0.5rem 0 0 0', 
          fontSize: '0.9rem', 
          opacity: 0.9 
        }}>
          Interactive visualization of Alaska's telecommunications infrastructure
        </p>
      </div>

      {/* Map Container */}
      <div style={{ flex: 1, position: 'relative' }}>
        <MapContainer
          center={[64.2008, -154.4937]} // Center of Alaska
          zoom={5}
          style={{ height: '100%', width: '100%' }}
          maxBounds={alaskaBounds}
          maxBoundsViscosity={1.0}
          minZoom={4}
        >
          {/* Base tile layer - OpenStreetMap */}
          <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          
          {/* Alaska boundary rectangle (GeoJSON representation) */}
          <Rectangle 
            bounds={alaskaBounds} 
            pathOptions={{ 
              color: '#3498db', 
              weight: 3, 
              fillOpacity: 0,
              dashArray: '10, 10'
            }} 
          />

          {/* City markers with popups */}
          {locations.map(({ position, name, content, description }) => (
            <Marker 
              key={name} 
              position={position as [number, number]}
            >
              <Popup>
                <div style={{ minWidth: '150px' }}>
                  <strong style={{ fontSize: '1.1rem', color: '#2c3e50' }}>
                    {name}
                  </strong>
                  <br />
                  <span style={{ color: '#7f8c8d' }}>{description}</span>
                  <br />
                  {content}
                  <br />
                  <em style={{ fontSize: '0.85rem', color: '#95a5a6' }}>
                    Demo location
                  </em>
                </div>
              </Popup>
            </Marker>
          ))}
        </MapContainer>
      </div>

      {/* Footer */}
      <div style={{ 
        backgroundColor: '#34495e', 
        color: 'white', 
        padding: '0.75rem 2rem',
        textAlign: 'center',
        fontSize: '0.85rem',
        zIndex: 1000
      }}>
        <p style={{ margin: 0 }}>
          TENeT Project • Kathiravelu Lab • Data sources: RIPE Atlas, Healthsites.io
        </p>
      </div>
    </div>
  );
}

export default App;