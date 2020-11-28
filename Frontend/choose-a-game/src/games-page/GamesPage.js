import './GamesPage.css';
import GamesBox from './GamesBox.js';
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
      <div>Loading</div>
    );
  }

  const mappedList = gamesList.map(game => game[0].game)
  return (
    <div className='GamesPageContainer'>
      {!Array.isArray(gamesList) ? (
        <div>
          No games found :(
        </div>
      ) : (
        mappedList.map(game => <GamesBox
          ImageSrc={game.headerImage}
          name={game.name}
          url={game.url}
          maxComboPlayers={game.maxComboPlayers}
          maxCouchPlayers={game.maxCouchPlayers}
          maxOnlinePlayers={game.maxOnlinePlayers}
        />)
      )}
      
    </div>
  );
}

export default GamesPage;
