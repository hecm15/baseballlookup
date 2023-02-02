import React, {useState} from "react";
import BaseballAPI from "../axiosinstance";
import { Search } from "@mui/icons-material";
import { Autocomplete, TextField, IconButton } from "@mui/material";
import isMobileScreen from "./isMobile";

export default function ManagerSearchBar(props) {
    const isMobile = isMobileScreen();
    const [managerOptions, setManagerOptions] = useState([]);

    const getManagerOptions = async(value) => {
        const response = await BaseballAPI.get(`/manageroptions?name=${value}`);
        setManagerOptions(response.data);
    }

    const inputChange = (e) => {
        if(e.target.value != ''){
            getManagerOptions(e.target.value);
        }
        else{
            setManagerOptions([])
        }
    }

    

    if(isMobile){
        return( 
            <form onSubmit={props.handleSubmit}>
                <Autocomplete
                disablePortal
                options={managerOptions}
                onInputChange={inputChange}
                onChange={(e, value) => {
                    props.handleChange(value?.playerid)
                }}
                getOptionLabel={(option) => option.name}
                renderOption={(props, option) => (
                    <li {...props} key={option.playerid}>
                    {option.name}
                    </li>
                )}
                style={{width: 250}}
                noOptionsText="No results found for this manager through the 2021 MLB season. Please check your spelling and try again."
                renderInput={(params) => (
                    <TextField {...params} label="Manager Name" variant="outlined"/>)}
                onOpen={
                    () => {
                        props.handleChange(null);
                        setManagerOptions([])
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
            options={managerOptions}
            onInputChange={inputChange}
            onChange={(e, value) => {
                props.handleChange(value?.playerid)
            }}
            getOptionLabel={(option) => option.name}
            renderOption={(props, option) => (
                <li {...props} key={option.playerid}>
                {option.name}
                </li>
            )}
            style={{width: 500}}
            noOptionsText="No results found for this manager through the 2021 MLB season. Please check your spelling and try again."
            renderInput={(params) => (
                <TextField {...params} label="Manager Name" variant="outlined"/>)}
            onOpen={
                () => {
                    props.handleChange(null);
                    setManagerOptions([])
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