import axios from 'axios';


//const LOCAL_URL = '127.0.0.1:3000/'
const HOSTED_URL = 'https://baseballlookup-production.up.railway.app/api'
const CURRENT_URL = HOSTED_URL;


const BaseballAPI = axios.create({
    baseURL: CURRENT_URL,
})

export default BaseballAPI;

