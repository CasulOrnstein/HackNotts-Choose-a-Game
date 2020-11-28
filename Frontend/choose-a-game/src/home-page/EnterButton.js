import './Home.css';
import {
  Link
} from "react-router-dom";

function EnterButton({ accountName }) {
  return ( 
    <div className='EnterButtonContainer'>
      <Link to={{
        pathname: "/friends",
        state: { accountName }
      }}>
        <div className="EnterButton">Enter</div>
      </Link>
    </div>
  )
}

export default EnterButton;