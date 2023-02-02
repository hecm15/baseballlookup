import React, { useContext } from "react";
import { PlayerInfoContext, PlayerPitchingStatsContext } from "../pages/players";
import PlayerInfoCard from "./PlayerInfoCard";
import BattingStatsTable from "./BattingStatsTable";
import BattingStatsPostTable from "./BattingStatsPostTable";
import FieldingStatsTable from "./FieldingStatsTable";
import FieldingStatsPostTable from "./FieldingStatsPostTable";
import PitchingStatsTable from "./PitchingStatsTable";
import PitchingStatsPostTable from "./PitchingStatsPostTable";
import { Grid, Typography } from "@mui/material"; 
import CircularProgress from '@mui/material/CircularProgress';




export default function PlayerDataDisplay(props){

    // this wont just be the playerinfo card, this will be the outer most component that handles playerinfo card , nav bar for stats, and table data. Like that we only render the rest once we know data call has been fullfilled by useQuery . So think about abstracting this.

    const playerInfo = useContext(PlayerInfoContext);
    const pitchingStats = useContext(PlayerPitchingStatsContext);

    if(props.loading){ // can pass isLoading boolean or the status variable
        return (<CircularProgress />);
    }
    if(props.isError){
        return <p> {props.error} </p>
    }

    if(playerInfo){
        if(playerInfo.position[0] != 'P'){
            return(
                <Grid container sx={{ height:"100%", overflowY: "auto"}} direction="column">
                    <Grid item height="20%">
                        <PlayerInfoCard/>
                    </Grid>
                    <Grid item sx={{pt: 2, height: "80%"}}>
                        <Typography variant="h5" sx={{pb: 4}}>
                            Batting
                        </Typography>
                        <BattingStatsTable/>
                        <BattingStatsPostTable />
                        <Typography variant="h5" sx={{pb: 4}}>
                            Fielding
                        </Typography>
                        <FieldingStatsTable/>
                        <FieldingStatsPostTable/>
                        {pitchingStats[0] ? 
                        <> 
                            <Typography variant="h5" sx={{pb: 4}}>
                                Pitching
                            </Typography>
                            <PitchingStatsTable/>
                            <PitchingStatsPostTable/>
                        </> : 
                        <></>
                        }
                    </Grid>
                </Grid> 
            );
        }
        return(
            <Grid container sx={{ height:"100%", overflowY: "auto"}} direction="column">
                <Grid item height="20%">
                    <PlayerInfoCard/>
                </Grid>
                <Grid item sx={{pt: 2, height: "80%"}}>
                    <Typography variant="h5" sx={{pb: 4}}>
                        Pitching
                    </Typography>
                    <PitchingStatsTable/>
                    <PitchingStatsPostTable/>

                    <Typography variant="h5" sx={{pb: 4}}>
                        Fielding
                    </Typography>
                    <FieldingStatsTable/>
                    <FieldingStatsPostTable/>
                    <Typography variant="h5" sx={{pb: 4}}>
                        Batting
                    </Typography>
                    <BattingStatsTable/>
                    <BattingStatsPostTable />
                </Grid>
            </Grid> 
        );
    }

    return(
        <></>
    );
}