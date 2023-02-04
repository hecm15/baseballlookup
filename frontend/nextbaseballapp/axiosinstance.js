import axios from 'axios';


const LOCAL_URL = 'https://baseballlookup-production.up.railway.app/api'
//const HOSTED_URL = url when we host on heroku
const CURRENT_URL = LOCAL_URL;


const BaseballAPI = axios.create({
    baseURL: CURRENT_URL,
})

export default BaseballAPI;

// next step is to build a working next js with material ui and test connection to database with axios. Once thats done you know you have a working frontend to backend connection and can beginning building the site å