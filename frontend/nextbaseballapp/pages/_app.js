import '../styles/globals.css'
import { CssBaseline, createTheme, Grid } from '@mui/material';
import { ThemeProvider } from '@mui/material/styles'
import { theme } from "../utils/theme.js"
import createEmotionCache from '../utils/createEmotionCache';
import { CacheProvider } from '@emotion/react';
import { QueryClient, QueryClientProvider } from "react-query" ;
import {useState} from 'react';
import { Css } from '@mui/icons-material';

const clientSideEmotionCache = createEmotionCache();


export default function App({ Component, emotionCache = clientSideEmotionCache ,pageProps }) {
  const [queryClient] = useState(() => new QueryClient());
  
  return(
    <Grid container sx={{width: '100vw', height: "100vh"}}>
      <Grid item sx={{pb: 4}}>
        <QueryClientProvider client={queryClient}>
          <CacheProvider value={emotionCache}>
            <ThemeProvider theme={theme}>
            <CssBaseline/>
                <Component {...pageProps} />
            </ThemeProvider>
          </CacheProvider>
        </QueryClientProvider>
      </Grid>
    </Grid>
  );
}
