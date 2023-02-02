import React, {useState} from "react";
import BaseballAPI from "../axiosinstance";
import { Search } from "@mui/icons-material";
import { Autocomplete, TextField, IconButton } from "@mui/material";
import isMobileScreen from "./isMobile";


export default function TeamSearchBar(props){
    const isMobile = isMobileScreen();
    const [teamOptions, setTeamOptions] = useState([]);

    const getTeamOptions = async(value) => {
        const response = await BaseballAPI.get(`/teamoptions?name=${value}`);
        setTeamOptions(response.data);
    }

    const inputChange = (e) => {
        if(e.target.value != ''){
            getTeamOptions(e.target.value);
        }
        else{
            setTeamOptions([])
        }
    }

    if(isMobile){
        return( 
            <form onSubmit={props.handleSubmit}>
                <Autocomplete
                disablePortal
                options={teamOptions}
                onInputChange={inputChange}
                onChange={(e, value) => {
                    props.handleChange(value?.franchid)
                }}
                getOptionLabel={(option) => option.name}
                renderOption={(props, option) => (
                    <li {...props} key={option.franchid}>
                    {option.name}
                    </li>
                )}
                style={{width: 250}}
                noOptionsText="No results found for this team in the 2021 MLB season. Please check your spelling and utilize currently active teams before trying again."
                renderInput={(params) => (
                    <TextField {...params} label="Team Name" variant="outlined"/>)}
                onOpen={
                    () => {
                        props.handleChange(null);
                        setTeamOptions([])
                    }   
                }
                filterOptions={(x) => x}
                />
    
                <IconButton size="large" type="submit">
                    <Search/>
                </IconButton>
            </form>
        );
    }

    return(
        <form onSubmit={props.handleSubmit}>
            <Autocomplete
            disablePortal
            options={teamOptions}
            onInputChange={inputChange}
            onChange={(e, value) => {
                props.handleChange(value?.franchid)
            }}
            getOptionLabel={(option) => option.name}
            renderOption={(props, option) => (
                <li {...props} key={option.franchid}>
                {option.name}
                </li>
            )}
            style={{width: 500}}
            noOptionsText="No results found for this team in the 2021 MLB season. Please check your spelling and utilize currently active teams before trying again."
            renderInput={(params) => (
                <TextField {...params} label="Team Name" variant="outlined"/>)}
            onOpen={
                () => {
                    props.handleChange(null);
                    setTeamOptions([])
                }   
            }
            filterOptions={(x) => x}
            />

            <IconButton size="large" type="submit">
                <Search/>
            </IconButton>
        </form>
    );
    
}