import './Home.css';
import SteamLogo from '../images/steam-logo.jpg';

function Logo() {
  return ( 
    <div className='LogoContainer'>
     <img src={SteamLogo} alt="Choose a Game Logo" className='Logo'/>
    </div>
  )
}

export default Logo;