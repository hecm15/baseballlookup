import React, {useState, createContext} from "react";
import styles from "../../styles/Home.module.css"
import NavBar from "../../components/NavBar";
import { Grid } from '@mui/material';
import navDrawer from "../../components/NavDrawer";
import stylesMUI from '../../utils/stylesMUI';
import PlayerSearchBar from "../../components/PlayerSearchBar";
import isMobileScreen from "../../components/isMobile";
import BaseballAPI from "../../axiosinstance";
import { useQuery } from 'react-query';
import PlayerDataDisplay from "../../components/PlayerDataDisplay";

export const PlayerInfoContext = createContext();
export const PlayerBattingStatsContext = createContext();
export const PlayerBattingStatsPostContext = createContext();
export const PlayerFieldingStatsContext = createContext();
export const PlayerFieldingStatsPostContext = createContext();
export const PlayerPitchingStatsContext = createContext();
export const PlayerPitchingStatsPostContext = createContext();

export default function PlayerSearch(){
    const [drawer, drawerHandle] = navDrawer();
    const [player, setPlayer] = useState(null);
    const [playerInfo, setPlayerInfo] = useState();
    const [playerBattingStats, setPlayerBattingStats] = useState();
    const [playerBattingStatsPost, setPlayerBattingStatsPost] = useState();
    const [playerFieldingStats, setPlayerFieldingStats] = useState();
    const [playerFieldingStatsPost, setPlayerFieldingStatsPost] = useState();
    const [playerPitchingStats, setPlayerPitchingStats] = useState();
    const [playerPitchingStatsPost, setPlayerPitchingStatsPost] = useState();

    const getPlayer = async() => {
        const infoResponse = await BaseballAPI.get(`/playerinfo?playerid=${player}`);
        const battingResponse = await BaseballAPI.get(`/batters?playerid=${player}`);
        const battingResponsePost = await BaseballAPI.get(`/batterspostszn?playerid=${player}`);
        const fieldingResponse = await BaseballAPI.get(`/fielders?playerid=${player}`);
        const fieldingPostResponse = await BaseballAPI.get(`/fielderspostszn?playerid=${player}`);
        const pitchingResponse = await BaseballAPI.get(`/pitchers?playerid=${player}`)
        const pitchingPostResponse = await BaseballAPI.get(`/pitcherspostszn?playerid=${player}`)
        setPlayerInfo(infoResponse.data);
        setPlayerBattingStats(battingResponse.data);
        setPlayerBattingStatsPost(battingResponsePost.data);
        setPlayerFieldingStats(fieldingResponse.data);
        setPlayerFieldingStatsPost(fieldingPostResponse.data);
        setPlayerPitchingStats(pitchingResponse.data);
        setPlayerPitchingStatsPost(pitchingPostResponse.data);
    }

    const { refetch, isLoading, isError, error } = useQuery("players", getPlayer,{
        enabled: false
    });

    const handleChange = (value) => {
        setPlayer(value);
    } 

    const resetData = () => {
        setPlayerInfo(null);
        setPlayerBattingStats(null);
        setPlayerBattingStatsPost(null);
        setPlayerFieldingStats(null);
        setPlayerBattingStatsPost(null);
        setPlayerPitchingStats(null);
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        if(player){
            resetData();
            refetch();
        }
    }

    return( 
        <PlayerInfoContext.Provider value={playerInfo}>
        <PlayerBattingStatsContext.Provider value={playerBattingStats}>
        <PlayerBattingStatsPostContext.Provider value={playerBattingStatsPost}>
        <PlayerFieldingStatsContext.Provider value={playerFieldingStats}>
        <PlayerFieldingStatsPostContext.Provider value={playerFieldingStatsPost}>
        <PlayerPitchingStatsContext.Provider value={playerPitchingStats}>
        <PlayerPitchingStatsPostContext.Provider value={playerPitchingStatsPost}>
            <div className={styles.container}>
                    <Grid container direction="column" sx={stylesMUI.grid}>
                        <Grid item sx={{height: "10vh"}}>
                            <NavBar 
                            drawerOpened={drawer}
                            handleDrawer={drawerHandle} />
                        </Grid>
                        <Grid item align="center" sx={{height: "15vh"}}>
                            <PlayerSearchBar
                            handleChange={handleChange}
                            handleSubmit={handleSubmit}/>
                        </Grid>
                        <Grid item sx={{height: "75vh"}} align="center">
                            <PlayerDataDisplay 
                            loading={isLoading}
                            error={error}
                            isError={isError}/>
                        </Grid>
                    </Grid>
                </div>
        </PlayerPitchingStatsPostContext.Provider>
        </PlayerPitchingStatsContext.Provider>
        </PlayerFieldingStatsPostContext.Provider>
        </PlayerFieldingStatsContext.Provider>
        </PlayerBattingStatsPostContext.Provider>
        </PlayerBattingStatsContext.Provider>
        </PlayerInfoContext.Provider>
    );
}

// TO CONTINUE: add context logic to our player data , other props that get handed down one level may not need context, once thats ready , begin working on backend logic to gather the info you need for each component 