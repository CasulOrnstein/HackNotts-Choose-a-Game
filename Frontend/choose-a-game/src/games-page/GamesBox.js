import './GamesPage.css';
//import SteamLogo from '../images/steam-logo.jpg';

function GamesBox({ImageSrc}) {
  return ( 
    <div className='GamesBoxContainer'>
     <img src={ImageSrc} className='GamesLogo'/>
      <div>Game Name:</div>
      <div>A, B, C own this game</div>
    </div>
  )
}

export default GamesBox;