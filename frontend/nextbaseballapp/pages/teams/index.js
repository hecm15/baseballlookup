import React, {createContext, use, useState} from "react";
import styles from "../../styles/Home.module.css";
import { Grid } from "@mui/material";
import NavBar from "../../components/NavBar";
import navDrawer from "../../components/NavDrawer";
import stylesMUI from '../../utils/stylesMUI';
import BaseballAPI from "../../axiosinstance";
import { useQuery } from 'react-query';
import TeamSearchBar from "../../components/TeamSearchBar";
import TeamDataDisplay from "../../components/TeamDataDisplay";

export const TeamInfoContext = createContext();
export const TeamIdContext = createContext();
export const TeamDataContext = createContext();



export default function TeamSearch(){
    const [drawer, drawerHandle] = navDrawer();
    const [team, setTeam] = useState(null);
    const [teamInfo, setTeamInfo] = useState();
    const [teamData, setTeamData] = useState();

    const handleChange = (value) => {
        setTeam(value);
    }

    const resetData = () => {
        setTeamInfo(null);
        setTeamData(null);
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        if(team){
            resetData();
            refetch();
        }
    }

    const getTeam = async() => {
        const infoResponse = await BaseballAPI.get(`/teaminfo?franchid=${team}`);
        const teamDataResponse = await BaseballAPI.get(`/teams?franchid=${team}`)
        setTeamInfo(infoResponse.data);
        setTeamData(teamDataResponse.data);
    }

    const {refetch, isLoading, isError, error} = useQuery("teams", getTeam, {
        enabled: false
    });

    return(
        <TeamInfoContext.Provider value={teamInfo}>
        <TeamIdContext.Provider value={team}>
        <TeamDataContext.Provider value={teamData}>
            <div className={styles.container}>
                <Grid container direction="column" sx={stylesMUI.grid}>
                    <Grid item sx={{height: "10vh"}}>
                        <NavBar 
                        drawerOpened={drawer}
                        handleDrawer={drawerHandle} />
                    </Grid>
                    <Grid item sx={{height: "15vh"}} align="center">
                        <TeamSearchBar
                        handleChange={handleChange}
                        handleSubmit={handleSubmit}
                        />
                    </Grid>
                    <Grid item sx={{height: "75vh"}} align="center">
                        <TeamDataDisplay
                        loading={isLoading}
                        error={error}
                        isError={isError}
                        />
                    </Grid>
                </Grid>
            </div>
        </TeamDataContext.Provider>
        </TeamIdContext.Provider>
        </TeamInfoContext.Provider>
    );
}