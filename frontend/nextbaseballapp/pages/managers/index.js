import React, { useState, createContext, useContext } from "react";
import styles from "../../styles/Home.module.css";
import { Grid } from "@mui/material";
import navDrawer from "../../components/NavDrawer";
import NavBar from "../../components/NavBar";
import stylesMUI from '../../utils/stylesMUI';
import BaseballAPI from "../../axiosinstance";
import { useQuery } from 'react-query';
import ManagerSearchBar from "../../components/ManagerSearchBar";
import ManagerDataDisplay from "../../components/ManagerDataDisplay";

export const ManagerInfoContext = createContext();
export const ManagerDataContext = createContext();

export default function ManagerSearch(){
    const[drawer, drawerHandle] = navDrawer();
    const [manager, setManager] = useState();
    const [managerInfo, setManagerInfo] = useState();
    const [managerData, setManagerData] = useState();
    
    const getManager = async() => {
        const managerInfoResponse = await BaseballAPI.get(`/managerinfo?playerid=${manager}`);
        const managerDataResponse = await BaseballAPI.get(`/managers?playerid=${manager}`);
        setManagerInfo(managerInfoResponse.data);
        setManagerData(managerDataResponse.data);
    }

    const { refetch, isLoading, isError, error} = useQuery("managers", getManager, {
        enabled: false
    });
   
    const handleChange = (value) => {
        setManager(value);
    }

    const resetData = () => {
        setManager(null);
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        if(manager) {
            resetData();
            refetch();
        }
    }

    return(
        <ManagerInfoContext.Provider value={managerInfo}>
        <ManagerDataContext.Provider value={managerData}>
            <div className={styles.container}>
                <Grid container direction="column" sx={stylesMUI.grid}>
                    <Grid item>
                        <NavBar 
                        drawerOpened={drawer}
                        handleDrawer={drawerHandle} />
                    </Grid>
                    <Grid item align="center" sx={{mt: 2}}>
                        <ManagerSearchBar
                        handleChange={handleChange}
                        handleSubmit={handleSubmit}/>
                    </Grid>
                    <Grid item align="center"> 
                        <ManagerDataDisplay
                        loading={isLoading}
                        isError={isError}
                        error={error}
                        />
                    </Grid>
                </Grid>
            </div>
        </ManagerDataContext.Provider>
        </ManagerInfoContext.Provider>
    );
}