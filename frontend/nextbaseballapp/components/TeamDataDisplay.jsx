import React, {useContext} from "react";
import { Grid, Typography } from '@mui/material';
import { TeamInfoContext } from "../pages/teams";
import TeamInfoCard from "./TeamInfoCard";
import TeamStatsTable from "./TeamStatsTable";
import CircularProgress from '@mui/material/CircularProgress';


export default function TeamDataDisplay(props){

    const teamInfo = useContext(TeamInfoContext);

    if(props.loading){
        return(
            <CircularProgress />
        );
    }

    if (props.isError){
        return <p>{props.error}</p>
    }

    if(teamInfo){
        return (
            <Grid container sx={{height: "100%", overflowY: "auto"}} direction="column">
                <Grid item maxHeight="50%">
                    <TeamInfoCard/>
                </Grid>
                <Grid item maxHeight="50%">
                        <Typography variant="h5" sx={{pt: 5}}>
                           Team History
                        </Typography>
                    <TeamStatsTable/>
                </Grid>
            </Grid>
        );
    }

    return (
        <></>
    );

}