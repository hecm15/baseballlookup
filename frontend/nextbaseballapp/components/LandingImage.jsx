import React from "react";
import { Typography} from "@mui/material";
import { Box, Grid, ImageList, ImageListItem } from '@mui/material'
import Image from "next/image";
import redSoxPic from '../utils/images/clark-van-der-beken-eA0-9tGE13k-unsplash.jpg';
import petcoPark from '../utils/images/derek-story-zd6Dm7Dg1OI-unsplash.jpg';
import dodgerJersey from '../utils/images/dez-hester-dezhester-eYCOVbyDY0M-unsplash.jpg';
import giantsIF from "../utils/images/john-ruddock-xg7ct-jABbI-unsplash.jpg";
import yankeesStadium from "../utils/images/lyle-hastie-2s8b5drgi-8-unsplash.jpg";
import stylesMUI from "../utils/stylesMUI";
import isMobileScreen from "./isMobile";

const imageData = [
    {
        img : redSoxPic,
        title: "Fenway Park"
    },
    {
        img : petcoPark,
        title: "Petco Park"
    },
    {
        img: dodgerJersey,
        title: "Dodger Jersey"
    },
    {
        img: giantsIF,
        title : "Giants Infield"
    },
    {
        img: yankeesStadium,
        title: "Yankee Stadium"
    }
]



export default function LandingImage(){
    const isMobile = isMobileScreen();

    let random1 = 0;
    let random2 = 0;

   random1 = Math.floor(Math.random() * 5);

    if (isMobile){
        return( 
            <Box sx={{position:"relative", width: "90%", height: "80%"}}>
                <Image
                src={imageData[random1].img}
                alt={imageData[random1].title}
                fill
                priority
                />
            </Box>
        );
    } else{
        do {
            random1 = Math.floor(Math.random() * 5);
            random2 = Math.floor(Math.random() * 5);
        } while (random1 === random2);

        return (
            <Grid container sx={{height:"95%", width: "95%"}}>
                
                <Grid item md={6} display="flex" alignItems="center" justifyContent="center">
                    <Typography variant="h4">
                        Your Baseball Data.
                    </Typography>
                </Grid>

                <Grid item md={6}>
                    <Box sx={{width: "100", height: "100%", position:"relative"}}>
                        <Image
                        src={imageData[random1].img}
                        alt={imageData[random1].title}
                        fill
                        priority
                        />
                    </Box>
                </Grid>

                <Grid item md={6} sx={{position: "relative"}}>
                    <Box sx={{width: "100", height: "100%", position:"relative"}}>
                        <Image
                        src={imageData[random2].img}
                        alt={imageData[random2].title}
                        fill
                        priority
                        />
                    </Box>
                </Grid>

                <Grid item md={6} display="flex" alignItems="center" justifyContent="center">
                    <Typography variant="h4">
                        Through the 2021 season.
                    </Typography>
                </Grid>
            </Grid>
        );
    }
}