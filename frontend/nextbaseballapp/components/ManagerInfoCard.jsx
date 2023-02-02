import React, { useContext } from "react";
import {Box, Grid, Typography, Paper} from '@mui/material';
import { ManagerInfoContext } from "../pages/managers";



export default function ManagerInfoCard(){

    const managerInfo = useContext(ManagerInfoContext);

    return(
        <Box sx={{backgroundColor: 'playerInfoCardBG.main', width: "100vw", height: "100%", maxWidth: 700}}>
            <Grid container sx={{width: "100%", height: "100%"}}>
                <Grid  container direction="column" item xs={8} sm={6} align="left"> 
                    <Grid item>
                        <Typography variant="playerNameIC" sx={{ml:1}}>
                            {managerInfo.name}
                        </Typography>
                    </Grid>

                    <Grid item>
                        <Typography variant="playerGeneralInfoIC" sx={{ml: 2}}>
                            Age : {managerInfo.age} 
                        </Typography>
                    </Grid>
                    <Grid item>
                        <Typography variant="playerGeneralInfoIC" sx={{ml: 2}}>
                            Weight: {managerInfo.weight} 
                        </Typography>
                    </Grid>
                    <Grid item>
                        <Typography variant="playerGeneralInfoIC" sx={{ml: 2}}>
                            Height : {managerInfo.height} 
                        </Typography>
                    </Grid>
                </Grid>
                <Grid item container direction="column" xs={4} sm={6}>
                     <Grid item>
                        <Typography variant="playerPositionIC">
                            {managerInfo.position}
                        </Typography>
                    </Grid>

                    <Grid item>
                        <Typography variant="playerGeneralInfoIC">
                            G : {managerInfo.games} 
                        </Typography>
                    </Grid>
                    <Grid item>
                        <Typography variant="playerGeneralInfoIC">
                            W: {managerInfo.wins} 
                        </Typography>
                    </Grid>
                    <Grid item>
                        <Typography variant="playerGeneralInfoIC">
                            L : {managerInfo.losses} 
                        </Typography>
                    </Grid>
                    <Grid item>
                        <Typography variant="playerGeneralInfoIC">
                            {managerInfo.winloss} 
                        </Typography>
                    </Grid>       
                </Grid>
            </Grid>
        </Box>
    );
}