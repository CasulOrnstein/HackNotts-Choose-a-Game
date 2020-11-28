import './Home.css';
import Logo from './Logo';
import EnterButton from './EnterButton';
import SteamIDForm from './SteamIDForm';

function Home() {
  return (
    <div className='HomeContainer'>
      <Logo/>
      <SteamIDForm/>
      <EnterButton/>
    </div>
  );
}

export default Home;
