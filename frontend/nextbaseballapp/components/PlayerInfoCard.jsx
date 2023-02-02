import { React, useContext } from "react";
import { Box, Grid, Typography } from '@mui/material'
import { PlayerInfoContext } from "../pages/players";


export default function PlayerInfoCard(){
    const playerInfo = useContext(PlayerInfoContext);

    return (
        <Box sx={{backgroundColor: 'playerInfoCardBG.main', width: "100%", height: "95%", maxWidth: 750}}>
            <Grid container sx={{width: "100%", height: "100%"}}>
                <Grid item xs={8} align="left">
                    <Typography variant="playerNameIC" sx={{ml: 1}}>
                        {playerInfo.name}
                    </Typography>
                </Grid>
                <Grid item xs={4} align="center">
                    <Typography variant="playerPositionIC">
                        {playerInfo.position}
                    </Typography>
                </Grid>

                <Grid item xs={4} align="center">
                    <Typography variant="playerGeneralInfoIC">
                        Age: {playerInfo.age}
                    </Typography>
                </Grid>

                <Grid item xs={4} align="center">
                    <Typography variant="playerGeneralInfoIC">
                    {playerInfo.height}ft / {playerInfo.weight}lbs  
                    </Typography>
                </Grid>

                <Grid item xs={4} align="center">
                    <Typography variant="playerGeneralInfoIC">
                        B/T : {playerInfo.bats} | {playerInfo.throws}
                    </Typography>
                </Grid> 
            </Grid>
        </Box>
    );

}