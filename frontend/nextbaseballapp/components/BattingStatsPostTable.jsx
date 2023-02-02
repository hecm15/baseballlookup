import React, {useContext} from "react";
import {Table,TableBody, TableCell, TableHead, TableRow ,Typography, Paper, Box } from '@mui/material';
import { PlayerBattingStatsPostContext } from "../pages/players";


export default function BattingStatsPostTable(){
    const battingStatsPost = useContext(PlayerBattingStatsPostContext);

    const columnHeaders = ['Season', 'Team', 'Series', 'G', 'AB', 'R', ,'RBI', 'H', '2B', '3B', 'HR', 'BB%', 'SO%', 'SB', 'CS', 'AVG']
    

    return(
        <Paper sx={{width: "85vw", height: "40vh", maxWidth: 1200, maxHeight: 800 ,overflowX: "auto", overflowY: "auto", mb: 10}}>
            <Typography fontSize="1rem">
                Postseason
            </Typography>
            <Table stickyHeader>
                <TableHead>
                    <TableRow>
                        {columnHeaders.map(header => (
                            header == "Season" ? 
                            <TableCell sx={{position: "sticky", left: 0, borderRight: "2px solid black", backgroundColor: "#BBBBBB"}} key={'post' + header}>
                                {header}
                            </TableCell>  :

                            <TableCell sx={{backgroundColor: '#BBBBBB'}} key={'post' + header}>
                                {header}
                            </TableCell> 
                        ))}
                    </TableRow>
                </TableHead>
                <TableBody>
                    {battingStatsPost.map((row) => (
                        <TableRow key={row.year + row.series}>
                            <TableCell align="left" sx={{position: "sticky", left: 0, borderRight: "2px solid black", backgroundColor:"white"}} component="th" scope="row" key={row.year + 'y'}>
                                {row.year}
                            </TableCell>
                            <TableCell align="left"  key={row.year + row.team + 't'}>
                                {row.team}
                            </TableCell>
                            <TableCell align="left" key={row.year+ row.series + 's'}>
                                {row.series}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.games + 'g'}>
                                {row.games}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.atbats + 'abs'}>
                                {row.atbats}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.runs + 'r'}>
                                {row.runs}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.rbis + 'rbis'}>
                                {row.rbis}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.hits + 'h'}>
                                {row.hits}
                            </TableCell>
                            <TableCell align="left"  key={row.year + row.doubles + '2b'}>
                                {row.doubles}
                            </TableCell>
                            <TableCell align="left"  key={row.year + row.triples + '3b'}>
                                {row.triples}
                            </TableCell>
                            <TableCell align="left"  key={row.year + row.homeruns + 'hr'}>
                                {row.homeruns}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.bbpercent + 'bb%'}>
                                {row.bbpercent}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.sopercent + 'so%'}>
                                {row.sopercent}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.sb + 'sb'}>
                                {row.sb}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.cs + 'cs'}>
                                {row.cs}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.avg + 'avg'}>
                                {row.avg}
                            </TableCell>
                        </TableRow>
                    ))}        
                </TableBody>
            </Table>
        </Paper>
    );
}