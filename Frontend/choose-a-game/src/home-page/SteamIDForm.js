import './Home.css';

function SteamIDForm() {
  return ( 
    <div className='SteamIDFormContainer'>

    <div className='InputLabel'>Steam Account</div>
    <input type="text" name="Steam Name" className="SteamIDForm" placeholder="e.g. aishlinging" required/>
   
    </div>
  )

  
}

export default SteamIDForm;