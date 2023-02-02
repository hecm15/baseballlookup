import React, { useContext } from 'react';
import { Table, TableBody, TableCell, TableHead, TableRow, Paper} from '@mui/material';
import { ManagerDataContext } from '../pages/managers';


export default function ManagerStatsTable(){
    const managerStats = useContext(ManagerDataContext);

    const columnHeaders = ['Season', 'Team', 'League', 'Games', 'Wins', 'Losses', 'W-L %', 'Team Division Rank', 'WS Win ?'];

    return(
        <Paper sx={{width: "85vw", height: "40vh", maxWidth: 1200, maxHeight: 800 ,overflowX: "auto", overflowY: "auto", mt: 6}}>
            <Table stickyHeader>
                <TableHead>
                    <TableRow key="columnheadersTeamStats">
                        {columnHeaders.map(header => (
                            header == "Season" ? 
                            <TableCell sx={{position: "sticky", left: 0, borderRight: "2px solid black", backgroundColor: "#BBBBBB"}} align="center" key={header}>
                                {header}
                            </TableCell>  :

                            <TableCell sx={{backgroundColor: '#BBBBBB'}} align="center" key={header}>
                                {header}
                            </TableCell> 
                        ))}
                    </TableRow>
                </TableHead>
                <TableBody>
                    {managerStats.map((row) => (
                        <TableRow key={row.year + row.teamname + row.league}>
                            <TableCell align="center" sx={{position: "sticky", left: 0, borderRight: "2px solid black", backgroundColor:"white"}} component="th" scope="row" key={row.year}>
                                {row.year}
                            </TableCell>
                            <TableCell align="center" key={row.year + row.team+ 't'}>
                                {row.team}
                            </TableCell>
                            <TableCell align="center" key={row.year + row.league + 'l'}>
                                {row.league}
                            </TableCell>
                            <TableCell align="center" key={row.year + row.g +'g'}>
                                {row.g}
                            </TableCell>
                            <TableCell align="center" key={row.year + row.w +'w'}>
                                {row.w}
                            </TableCell>
                            <TableCell align="center" key={row.year + row.l + 'l'}>
                                {row.l}
                            </TableCell>
                            <TableCell align="center" key={row.year + row.winloss + 'wl'}>
                                {row.winloss}
                            </TableCell>
                            <TableCell align="center" key={row.year + row.rank + 'wl'}>
                                {row.rank}
                            </TableCell>
                            <TableCell align="center" key={row.year + row.wswin + 'wswin'}>
                                {row.wswin}
                            </TableCell>
                        </TableRow>
                    ))}        
                </TableBody>
            </Table>
        </Paper>
    );
}