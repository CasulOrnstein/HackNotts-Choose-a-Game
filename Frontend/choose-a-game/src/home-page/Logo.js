import './Home.css';
import SteamLogo from '../images/steamlogo.png';

function Logo() {
  return ( 
    <div className='LogoContainer'>
     <img src={SteamLogo} alt="Choose a Game Logo" className='Logo'/>
    </div>
  )
}

export default Logo;