import { React, useContext} from "react";
import { Box, Grid, Typography } from '@mui/material';
import { TeamInfoContext } from "../pages/teams";
import Image from "next/image";
import { teamLogos } from "../logos/logos";

export default function TeamInfoCard(){
    const teamInfo = useContext(TeamInfoContext);
    
    return(
        <Box sx={{backgroundColor: 'teamInfoCardBG.main', width: "100%", height: "100%", maxWidth: 750}}>
            <Grid container sx={{width: "100%", height: "100%"}}>
                <Grid container item xs={8} md={7}>
                    <Grid xs={12} item align="center">
                        <Typography variant="teamNameIC" color={teamLogos[teamInfo.franchid].color}>
                            {teamInfo.activeteamname}
                        </Typography>
                    </Grid>
                    <Grid item xs={12}> 
                        <Typography variant="teamGeneralInfoIC">
                            Seasons: {teamInfo.seasons}
                        </Typography>
                    </Grid>
                    <Grid item xs={12}>
                        <Typography variant="teamGeneralInfoIC">
                            Record: {teamInfo.record}
                        </Typography>
                    </Grid>
                    <Grid item xs={12}>
                        <Typography variant="teamGeneralInfoIC">
                            Pennants: {teamInfo.pennants}
                        </Typography>
                    </Grid>
                    <Grid item xs={12}>
                        <Typography variant="teamGeneralInfoIC" >
                            World Series: {teamInfo.wswins}
                        </Typography>
                    </Grid>
                    <Grid item xs={12}>
                        <Typography variant="teamGeneralInfoIC">
                            Team Names: {teamInfo.team_names}
                        </Typography>
                    </Grid>
                </Grid>
                <Grid item xs={4} md={5} sx={{position: "relative"}}>
                    <Image 
                    src={teamLogos[teamInfo.franchid].logo}
                    alt={`${teamInfo.activeteamname} logo`}
                    fill
                    priority/>
                </Grid>
            </Grid>
        </Box>
    );


}