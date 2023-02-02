import React, { useContext } from 'react';
import { Grid, Typography } from '@mui/material';
import CircularProgress from '@mui/material/CircularProgress';
import { ManagerInfoContext } from '../pages/managers';
import ManagerInfoCard from './ManagerInfoCard';
import { ManagerDataContext } from '../pages/managers';
import ManagerStatsTable from './ManagerStatsTable';


export default function ManagerDataDisplay(props){
    const managerInfo = useContext(ManagerInfoContext);
    const managerData = useContext(ManagerDataContext);

    if(props.loading){
        return (<CircularProgress/>);
    }
    if(props.isError){
        return <p> {props.error} </p>
    }

    if(managerInfo){
        return(
            <Grid container sx={{height: "100%", overflowY: "auto"}} direction="column">
                <Grid item>
                    <ManagerInfoCard />
                </Grid>
                <Grid item>
                    <ManagerStatsTable/>
                </Grid>
            </Grid>
        );
    }

    return <></>
}