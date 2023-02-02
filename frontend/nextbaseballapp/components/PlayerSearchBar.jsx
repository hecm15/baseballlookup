import React, { useState, useEffect,useContext } from "react";
import { Autocomplete, TextField, IconButton} from "@mui/material";
import { Search, Clear } from "@mui/icons-material";
import BaseballAPI from "../axiosinstance";
import isMobileScreen from "./isMobile";



export default function PlayerSearchBar(props){

    const[playerOptions, setPlayerOptions] = useState([]);
    const isMobile = isMobileScreen();
    
    const getPlayerOptions = async(value) => {
        const response = await BaseballAPI.get(`/playeroptions?name=${value}`);
        setPlayerOptions(response.data);
    }
   
    const inputChange = (e) => {
        if(e.target.value != ''){
            getPlayerOptions(e.target.value);
        }
        else{
            setPlayerOptions([])
        }
    }

    if(isMobile){
        return(
            <form onSubmit={props.handleSubmit}>
                <Autocomplete
                disablePortal
                options={playerOptions} 
                onInputChange={inputChange} // handles keystroke click and retrieval of availible database options
                onChange={(e, value) => {
                    props.handleChange(value?.playerid);
                }} // handles click of avaible options and saves playerid of this option in parent state for data retrieval
                getOptionLabel={(option) => option.name}
                renderOption={(props, option) => (
                    <li {...props} key={option.playerid}>
                    {option.name + ' - ' + option.debut}
                    </li>
                )}
                style={{width: 250}}
                noOptionsText="No results found for this player through the 2021 MLB season. Please check your spelling and try again. "
                renderInput={(params) => (
                    <TextField {...params} label="Player Name" variant="outlined"/>)}
                onOpen={
                    () => {
                        props.handleChange(null);
                        setPlayerOptions([])
                    }   
                }
                filterOptions={(x) => x}
                />
    
                <IconButton type="submit" size="large">
                    <Search />
                </IconButton>
            </form> 
        );
    } else{
        return(
            <form onSubmit={props.handleSubmit}>
                <Autocomplete
                disablePortal
                options={playerOptions} 
                onInputChange={inputChange} // handles keystroke click and retrieval of availible database options
                onChange={(e, value) => {
                    props.handleChange(value?.playerid);
                }} // handles click of avaible options and saves playerid of this option in parent state for data retrieval
                getOptionLabel={(option) => option.name}
                renderOption={(props, option) => (
                    <li {...props} key={option.playerid}>
                    {option.name + ' - ' + option.debut}
                    </li>
                )}
                style={{width: 500}}
                noOptionsText="No results found for this player through the 2021 MLB season. Please check your spelling and try again. "
                renderInput={(params) => (
                    <TextField {...params} label="Player Name" variant="outlined"/>)}
                onOpen={
                    () => {
                        props.handleChange(null);
                    }
                }
                filterOptions={(x) => x}
                />
    
                <IconButton type="submit" size="large">
                    <Search />
                </IconButton>
            </form> 
        );
    }
}