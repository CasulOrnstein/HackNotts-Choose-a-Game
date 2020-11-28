import './GamesPage.css';
import GamesBox from './GamesBox.js';

function GamesPage() {
  return (
    <div className='GamesPageContainer'>
      <GamesBox ImageSrc="https://steamcdn-a.akamaihd.net/steam/apps/203160/header.jpg?t=1601485883"/>
      <GamesBox ImageSrc="https://steamcdn-a.akamaihd.net/steam/apps/203160/header.jpg?t=1601485883"/>
      <GamesBox ImageSrc="https://steamcdn-a.akamaihd.net/steam/apps/203160/header.jpg?t=1601485883"/>
    </div>
  );
}

export default GamesPage;
