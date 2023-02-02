import React, {useContext} from "react";
import {Table,TableBody, TableCell, TableHead, TableRow ,Typography, Paper, Box } from '@mui/material';
import { PlayerFieldingStatsPostContext } from "../pages/players";


export default function FieldingStatsPostTable(){
    const fieldingStats= useContext(PlayerFieldingStatsPostContext);

    const columnHeaders = ['Season', 'Team', "Series" ,'Position', 'G', 'GS', 'InnOuts', 'PO', 'A', 'E', 'DP', 'PB','SB', 'CS']

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
                            <TableCell sx={{position: "sticky", left: 0, borderRight: "2px solid black", backgroundColor: "#BBBBBB"}} key={"post" + header}>
                                {header}
                            </TableCell>  :

                            <TableCell sx={{backgroundColor: '#BBBBBB'}} key={"post" + header}>
                                {header}
                            </TableCell> 
                        ))}
                    </TableRow>
                </TableHead>
                <TableBody>
                    {fieldingStats.map((row) => (
                        <TableRow key={row.year + row.series}>
                            <TableCell align="left" sx={{position: "sticky", left: 0, borderRight: "2px solid black", backgroundColor:"white"}} component="th" scope="row" key={row.year + row.team + 'y'}>
                                {row.year}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.team + 't'}>
                                {row.team}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.series + 'ser'}>
                                {row.series}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.position + 'pos'}>
                                {row.position}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.games + 'g'}>
                                {row.games}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.gamesstarted + 'gs'}>
                                {row.gamesstarted}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.innouts + 'io'}>
                                {row.innouts}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.po + 'po'}>
                                {row.po}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.a + 'a'}>
                                {row.a}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.e + 'e'}>
                                {row.e}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.dp + 'dp'}>
                                {row.dp}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.pb + 'pb'}>
                                {row.pb}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.sb + 'sb'}>
                                {row.sb}
                            </TableCell>
                            <TableCell align="left" key={row.year + row.cs + 'cs'}>
                                {row.cs}
                            </TableCell>
                        </TableRow>
                    ))}        
                </TableBody>
            </Table>
        </Paper>
    );

}