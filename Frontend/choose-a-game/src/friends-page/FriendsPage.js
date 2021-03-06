import './FriendsPage.css';
import FriendsSelector from './FriendsSelector';
import NextButton from './NextButton';
import axios from 'axios'
import LoadingScreen from '../loading-screen/loading'

import {useEffect, useState} from 'react'

function FriendsPage(props) {
  const accountName = props.location.state.accountName || "CasulOrnstein"
  const [friendsList, setData] = useState(undefined);
  const [selectedFriends, setSelectedFriends] = useState([])

  const addRemoveFriendId = (id) => {
    if(selectedFriends.includes(id)) {
      setSelectedFriends(selectedFriends.filter(i => i !== id))
    } else {
      setSelectedFriends([...selectedFriends, id])
    }
  }
 
  useEffect(() => {
    const fetchData = async () => {
      const result = await axios(
        `http://127.0.0.1:5000/api/friends?name=${accountName}`,
      );
      setData(result.data.friends);
      setSelectedFriends([...selectedFriends, result.data.thisuserid.toString()])
    };
    fetchData();
  }, [accountName]);
  if (friendsList === undefined) {
    return (
      <LoadingScreen text="Listing all your friends!"/>
    );
  }

  return (
    <div className='FriendsPageContainer'>
      <div style={{paddingTop:'5vh', fontSize:'25pt'}}>Select friends you want to play with!</div>
      <FriendsSelector friendsList={friendsList} handleToggle={addRemoveFriendId}/>
      <NextButton selectedFriends={selectedFriends}/>
    </div>
  );
}

export default FriendsPage;
