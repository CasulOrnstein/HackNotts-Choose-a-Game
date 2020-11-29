import './FriendsPage.css';
import { useState } from 'react'

function FriendBox({imageSrc, name, id, handleToggle}) {
  const [isSelected, setSelectedState] = useState(false)

  const toggleState = () => {
    setSelectedState(!isSelected);
    handleToggle(id)
  }

  return (
    <div className='FriendBox' onClick={toggleState} style={isSelected ? { backgroundColor: '#2a80ed'} : {} }>
      <img src={imageSrc} className="Image"/>
      <div className='FriendBoxText'>{name}</div>
    </div>
  )
}

export default FriendBox;