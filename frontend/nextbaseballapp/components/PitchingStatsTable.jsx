import React, {useContext} from "react";
import {Table,TableBody, TableCell, TableHead, TableRow ,Typography, Paper, Box } from '@mui/material';
import { PlayerPitchingStatsContext } from "../pages/players";


export default function PitchingStatsTable(){
    const pitchingStats= useContext(PlayerPitchingStatsContext);

    const columnHeaders = ['Season', 'Team', 'W', 'L', 'ERA', 'G', 'GS', 'CG', 'ShO', 'SV', 'IP', 'TBF', 'H', 'R', 'ER', 'HR', 'BB', 'SO', 'WHIP', 'KK/9', 'BB/9', 'HR/9']

    return(
        <Paper sx={{width: "85vw", height: "40vh", maxWidth: 1200, maxHeight: 800 ,overflowX: "auto", overflowY: "auto", mb: 10}}>
            <Typography fontSize="1rem">
                Regular Season
            </Typography>
            <Table stickyHeader>
                <TableHead>
                    <TableRow>
                        {columnHeaders.map(header => (
                            header == "Season" ? 
                            <TableCell sx={{position: "sticky", left: 0, borderRight: "2px solid black", backgroundColor: "#BBBBBB"}} key={"reg" + header}>
                                {header}
                            </TableCell>  :

                            <TableCell sx={{backgroundColor: '#BBBBBB'}} key={"reg" + header}>
                                {header}
                            </TableCell> 
                        ))}
                    </TableRow>
                </TableHead>
                <TableBody>
                    {pitchingStats.map((row) => ( 
                        <TableRow key={row.year + row.team + row.series}>
                            <TableCell align="left" sx={{position: "sticky", left: 0, borderRight: "2px solid black", backgroundColor:"white"}} component="th" scope="row" key={row.year + row.team + 'y'}>
                                {row.year}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.team + 't'}>
                                {row.team}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.wins + 'w'}>
                                {row.wins}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.losses + 'l'}>
                                {row.losses}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.era + 'era'}>
                                {row.era}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.games + 'g'}>
                                {row.games}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.gamesstarted + 'gs'}>
                                {row.gamesstarted}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.cg + 'cg'}>
                                {row.cg}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.sho + 'sho'}>
                                {row.sho}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.sv + 'sv'}>
                                {row.sv}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.ip + 'ip'}>
                                {row.ip}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.tbf + 'tbf'}>
                                {row.tbf}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.h + 'h'}>
                                {row.h}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.r + 'r'}>
                                {row.r}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.er + 'er'}>
                                {row.er}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.hr + 'hr'}>
                                {row.hr}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.bb + 'bb'}>
                                {row.bb}
                            </TableCell>
                            <TableCell align="left"vkey={row.year + row.so + 'so'}>
                                {row.so}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.whip + 'wh'}>
                                {row.whip}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.kkper9 + 'kk9'}>
                                {row.kkper9}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.bbper9 + 'bb9'}>
                                {row.bbper9}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.hrper9 + 'hr9'}>
                                {row.hrper9}
                            </TableCell>
                        </TableRow>
                    ))}        
                </TableBody>
            </Table>
        </Paper>
    );

}