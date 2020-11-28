import './FriendsPage.css';

function FriendBox({imageSrc}) {
  return (
    <div className='FriendBox'>
      <img src={imageSrc} className="Image"/>
      <div className='FriendBoxText'>Name</div>

    </div>
  )
}

export default FriendBox;