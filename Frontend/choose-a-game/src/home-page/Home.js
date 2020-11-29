import './Home.css';
import Logo from './Logo';
import Title from './Title';
import EnterButton from './EnterButton';
import SteamIDForm from './SteamIDForm';
import { useState } from 'react'

function Home() {
  const [ accountName, setAccountName ] = useState("")
  return (
    <div className='HomeContainer'>
      <Logo/>
      <Title/>
      <SteamIDForm setAccountName={setAccountName}/>
      <EnterButton accountName={accountName}/>
    </div>
  );
}

export default Home;
