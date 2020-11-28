import './Home.css';

function SteamIDForm({setAccountName}) {
  return ( 
    <div className='SteamIDFormContainer'>

    <div className='InputLabel'>Steam Account</div>
      <input
        type="text"
        name="Steam Name"
        className="SteamIDForm"
        placeholder="e.g. aishlinging"
        required
        onBlur={(e) => setAccountName(e.target.value)}
      />
    </div>
  )

  
}

export default SteamIDForm;