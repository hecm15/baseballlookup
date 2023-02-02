import React, {useContext} from "react";
import {Table,TableBody, TableCell, TableHead, TableRow ,Typography, Paper } from '@mui/material';
import { TeamDataContext } from "../pages/teams";


export default function TeamStatsTable(){
    const teamStats = useContext(TeamDataContext);

    const columnHeaders = ['Season', 'Name', 'Division', 'Rank', 'Games', 'Wins', 'Losses', 'W-L %', 'WS Win', 'R', 'RA', 'Attendance', 'Park'];
    

    return(
        <Paper sx={{width: "85vw", height: "40vh", maxWidth: 1200, maxHeight: 800 ,overflowX: "auto", overflowY: "auto", mt: 6}}>
            <Table stickyHeader>
                <TableHead>
                    <TableRow key="columnheadersTeamStats">
                        {columnHeaders.map(header => (
                            header == "Season" ? 
                            <TableCell sx={{position: "sticky", left: 0, borderRight: "2px solid black", backgroundColor: "#BBBBBB"}} align="left" key={header}>
                                {header}
                            </TableCell>  :

                            <TableCell sx={{backgroundColor: '#BBBBBB'}} align="left" key={header}>
                                {header}
                            </TableCell> 
                        ))}
                    </TableRow>
                </TableHead>
                <TableBody>
                    {teamStats.map((row) => (
                        <TableRow key={row.year + row.teamname + row.league}>
                            <TableCell align="left" sx={{position: "sticky", left: 0, borderRight: "2px solid black", backgroundColor:"white"}} component="th" scope="row" key={row.year}>
                                {row.year}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.teamname + 't'}>
                                {row.teamname}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.league + 'l'}>
                                {row.league}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.rank +'r'}>
                                {row.rank}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.g +'g'}>
                                {row.g}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.w + 'w'}>
                                {row.w}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.l + 'l'}>
                                {row.l}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.wlpercent + 'wl'}>
                                {row.wlpercent}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.wswin + 'wswin'}>
                                {row.wswin}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.r + 'runs'}>
                                {row.r}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.ra + 'ra'}>
                                {row.ra}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.attendance + 'a'}>
                                {row.attendance}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.park + 'p'}>
                                {row.park}
                            </TableCell>
                        </TableRow>
                    ))}        
                </TableBody>
            </Table>
        </Paper>
    );

}