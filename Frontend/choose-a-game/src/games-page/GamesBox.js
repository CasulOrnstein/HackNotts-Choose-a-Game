import './GamesPage.css';
//import SteamLogo from '../images/steam-logo.jpg';

function GamesBox({ImageSrc, name, players}) {
  return ( 
    <div className='GamesBoxContainer'>
     <img src={ImageSrc} className='GamesLogo'/>
      <div>{name}</div>
      <div>{players.join(' and ')} own this game</div>
    </div>
  )
}

export default GamesBox;