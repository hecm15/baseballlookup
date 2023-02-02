import { useMediaQuery, useTheme } from "@mui/material";


export default function isMobileScreen(){
    const theme = useTheme();
    return useMediaQuery(theme.breakpoints.down('md'));
}