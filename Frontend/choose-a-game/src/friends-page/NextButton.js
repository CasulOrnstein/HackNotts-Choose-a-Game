import './FriendsPage.css';
import {
  Link
} from "react-router-dom";

function NextButton({selectedFriends}) {
  console.log(selectedFriends)
  return ( 
    <div className='NextButtonContainer'>
      <Link to={{
        pathname: "/games",
        state: { selectedFriends }
      }}>
        <div className="NextButton">Next</div>
      </Link>
    </div>
  )
}

export default NextButton;