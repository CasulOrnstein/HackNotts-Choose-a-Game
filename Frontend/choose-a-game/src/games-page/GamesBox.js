import './GamesPage.css';
//import SteamLogo from '../images/steam-logo.jpg';

function GamesBox({ImageSrc}) {
  return ( 
    <div className='GamesBoxContainer'>
     <img src={ImageSrc} className='Logo'/>
    </div>
  )
}

export default GamesBox;