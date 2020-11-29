import './GamesPage.css';
import GamesBox from './GamesBox.js';
import LoadingScreen from '../loading-screen/loading'
import axios from 'axios'

import {useEffect, useState} from 'react'

function GamesPage(props) {
  const friends = props.location.state.selectedFriends.length != 0 ? props.location.state.selectedFriends : ["76561198044229271","76561198025279929"]
  const [gamesList, setData] = useState(undefined);
  
  useEffect(() => {
    const fetchData = async () => {
      const result = await axios(
        `http://127.0.0.1:5000/api/games?friends=${friends}`,
      );
      setData(result.data);
    };
 
    fetchData();
  }, []);

  if (gamesList === undefined) {
    return (
      <LoadingScreen text="Finding games for you all to play!"/>
    );
  }

  const mappedList = gamesList.map(game => game[0])
  return (
    <div className='GamesPageContainer'>
      {mappedList.map(game => <GamesBox
          ImageSrc={game.game.headerImage}
          name={game.game.name}
          url={game.game.url}
          maxComboPlayers={game.game.maxComboPlayers}
          maxCouchPlayers={game.game.maxCouchPlayers}
          maxOnlinePlayers={game.game.maxOnlinePlayers}
          players={game.playerNames}
        />)
      }
    </div>
  );
}

export default GamesPage;
