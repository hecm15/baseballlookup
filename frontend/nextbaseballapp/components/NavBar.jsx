import React from "react";
import { Box, Grid , Button ,AppBar, Drawer, List , ListItem, ListItemButton, ListItemText ,Toolbar, Typography, IconButton, Icon, ListItemIcon} from "@mui/material";
import { Menu , Search} from "@mui/icons-material";
import Link from "next/link";
import stylesMUI from "../utils/stylesMUI";
import isMobileScreen from "./isMobile";


export default function NavBar(props){

    const isMobile = isMobileScreen();

    if (isMobile){
        return(
            <AppBar position="sticky" >
                <Toolbar disableGutters>
                    <Grid container sx={{"width" : "100%", "height" : "100%"}}>
                        
                        <Grid item xs={3}>
                            <IconButton onClick={props.handleDrawer}>
                                <Menu size="large"/>
                            </IconButton>
                        </Grid>

                        <Drawer 
                        anchor="left"
                        open={props.drawerOpened}
                        onClose={props.handleDrawer}>
                            <List>
                                <ListItem disablePadding>
                                    <ListItemButton component={Link} href={"/players"}>
                                        <ListItemIcon>
                                            <Search/>
                                        </ListItemIcon>
                                        <ListItemText >
                                            <Typography>
                                                Players
                                            </Typography>
                                        </ListItemText>
                                    </ListItemButton>
                                </ListItem>

                                <ListItem disablePadding>
                                    <ListItemButton component={Link} href={"/teams"}>
                                        <ListItemIcon>
                                            <Search/>
                                        </ListItemIcon>
                                        <ListItemText >
                                            <Typography>
                                                Teams
                                            </Typography>
                                        </ListItemText>
                                    </ListItemButton>
                                </ListItem>

                                <ListItem disablePadding>
                                    <ListItemButton component={Link} href={"/managers"}>
                                        <ListItemIcon>
                                            <Search/>
                                        </ListItemIcon>
                                        <ListItemText >
                                            <Typography>
                                                Managers
                                            </Typography>
                                        </ListItemText>
                                    </ListItemButton>
                                </ListItem>
                            </List>
                        </Drawer> 


                        <Grid item xs={6} textAlign="center" justifyContent={"center"} alignItems="center">
                            <Typography variant="siteHeaderMobile" fontFamily={"Poppins"} component={Link} href={"/landing"}>
                                Baseball LookUp
                            </Typography>
                        </Grid>

                        <Grid item xs={3}>

                        </Grid>

                    </Grid>
                </Toolbar>
            </AppBar>
        );
    } else{
        return(
            <AppBar position="sticky">
                <Toolbar disableGutters>
                    <Grid container sx={{height : "100%", width: "100%"}}>
                        <Grid item md={4} align="center">
                            <Typography variant="siteHeaderDesktop" component={Link} href="/landing">
                                Baseball LookUp
                            </Typography>
                        </Grid>

                        <Grid item md={4}/>

                        <Grid item md={1}>
                            <Button variant="text" component={Link} href="/players" color="navButton">
                                Players
                            </Button>
                        </Grid>

                        <Grid item md={1}>
                            <Button variant="text" component={Link} href="/teams" color="navButton">
                                Teams
                            </Button>
                        </Grid>
                        <Grid item md={1}>
                            <Button variant="text" component={Link} href="/managers" color="navButton">
                                Managers
                            </Button>
                        </Grid>
                        <Grid item md={1} />
                    
                    </Grid>
                </Toolbar>
            </AppBar>
        );
    }
}




