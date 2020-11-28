import './FriendsPage.css';
import FriendBox from './FriendBox';

function FriendsSelector({friendsList, handleToggle}) {
  return (
    <div className='FriendsSelectorContainer'>
      {friendsList.slice(0,5).map(friend => <FriendBox 
        imageSrc={friend.avatarmedium}
        name={friend.personaname}
        id={friend.steamid}
        handleToggle={handleToggle}
      />)}
    </div>
  );
}

export default FriendsSelector;