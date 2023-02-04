import { Grid, Typography } from '@mui/material';
import {useState, useEffect} from "react";
import styles from "../styles/Home.module.css" 
import stylesMUI from '../utils/stylesMUI';
import NavBar from '../components/NavBar';
import navDrawer from '../components/NavDrawer';
import LandingImage from '../components/LandingImage';


export default function LandingPage(){
    const [drawer, drawerHandle] = navDrawer();

    return(
        <div className={styles.container}>
            <Grid container direction="column" sx={stylesMUI.grid}>
                <Grid item height={"10vh"}>
                    <NavBar 
                    drawerOpened={drawer}
                    handleDrawer={drawerHandle} />
                </Grid>
                <Grid item height={"90vh"}  align="center">
                    <LandingImage />
                </Grid>
            </Grid>
        </div>
    );
}

