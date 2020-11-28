import './FriendsPage.css';
import FriendsSelector from './FriendsSelector';
import FriendBox from './FriendBox';
import NextButton from './NextButton';

function FriendsPage() {
  return (
    <div className='FriendsPageContainer'>
      <FriendsSelector/>
      <NextButton/>
    </div>
  );
}

export default FriendsPage;
