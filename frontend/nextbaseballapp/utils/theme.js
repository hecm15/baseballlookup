import { createTheme } from "@mui/material"; 


export const theme = createTheme({
    spacing : 8, //default value
    palette: {
        mode: 'light',

        navButton : {
            main : '#FFFFFF'
        },

        playerInfoCardBG : {
            main : '#BBBBBB'
        },

        teamInfoCardBG : {
            main : '#BBBBBB'
        }
    },

    typography: {
        fontFamily : [
            'Poppins'
        ].join(','),
        
        siteHeaderMobile : {
            fontSize : '1.4rem',
            fontFamily: 'Poppins',
            
            '@media (max-width: 370px)' : {
                fontSize : '1.0rem' 
            },
            fontWeight: 600
        },

        siteHeaderDesktop : {
            fontSize : '1.7rem',
            fontFamily: 'Poppins',
            fontWeight: 600
        },

        playerNameIC: {
            fontSize : '1.7rem',
            fontFamily: 'Poppins',
            
            '@media (max-width: 370px)' : {
                fontSize : '1.2rem' 
            }
        },
        playerPositionIC: {
            fontSize : '1.4rem',
            fontFamily: 'Poppins',
            
            '@media (max-width: 370px)' : {
                fontSize : '0.9rem' 
            }
        },
        playerGeneralInfoIC: {
            fontSize : '1rem',
            fontFamily: 'Poppins',
            
            '@media (max-width: 370px)' : {
                fontSize : '0.5rem' 
            }
        },
        teamNameIC: {
            fontSize : '1.4rem',
            fontFamily: 'Poppins',
            fontWeight: 600,
            
            '@media (max-width: 370px)' : {
                fontSize : '1.0rem' 
            }
        }, 
        teamGeneralInfoIC: {
            fontSize : '0.9rem',
            fontFamily: 'Poppins',
            
            '@media (max-width: 370px)' : {
                fontSize : '0.5rem' 
            }
        }   
    }
});