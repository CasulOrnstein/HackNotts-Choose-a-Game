import './GamesPage.css';
//import SteamLogo from '../images/steam-logo.jpg';

function GamesBox({ImageSrc, name, players, friends, maxOnlinePlayers, maxCouchPlayers}) {
  let text = friends.length == players.length ? "You all" : players.join(' and ')

  let playersText = maxOnlinePlayers == 4 && maxCouchPlayers == 4 ? "Unknown online / couch players" : `${maxOnlinePlayers} online / ${maxCouchPlayers} couch co-op`
  return ( 
    <div className='GamesBoxContainer'>
     <img src={ImageSrc} className='GamesLogo'/>
      <div>{name}</div>
      <div style={{fontSize: '14pt', color: 'gray'}}>{playersText}</div>
      <div>{text} own this game!</div>
    </div>
  )
}

export default GamesBox;