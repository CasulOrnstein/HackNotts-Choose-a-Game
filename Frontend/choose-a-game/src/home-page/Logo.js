import './Home.css';
import SteamLogo from '../images/steamlogo.png';

function Logo() {
  return ( 
    <div className='LogoContainer'>
     <img src={SteamLogo} alt="Steam Logo" className='Logo'/>
    </div>
  )
}

export default Logo;