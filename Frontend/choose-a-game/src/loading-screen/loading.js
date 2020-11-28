import './Loading.css';
import Logo from '../images/steam_logo_transparent.png';

function LoadingScreen({text}) {
  return (
    <div className='LoadingContainer'>
      <img src={Logo} className='LoadingIcon'></img>
      <div>{text}</div>
    </div>
  );
}

export default LoadingScreen;