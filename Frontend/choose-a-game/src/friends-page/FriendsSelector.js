import './FriendsPage.css';
import FriendBox from './FriendBox';
import cooltimes from '../images/cooltimes-icon.jpg';
import casul from '../images/casul-icon.jpg'; 
import aishling from '../images/aishling-icon.jpg';
import jamespellis from '../images/jamespellis-icon.jpg';

function FriendsSelector() {
  const images = [cooltimes, casul, aishling, jamespellis];
  return (
    <div className='FriendsSelectorContainer'>
      {images.map(img => <FriendBox imageSrc={img}/>)}
    </div>
  );
}

export default FriendsSelector;