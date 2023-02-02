import createCache from "@emotion/cache";

// needed for server side css rendering, I provide this cache to our app by wrapping our application and theme provider with the cache provider component in app.js
export default function createEmotionCache(){
    return createCache({key: "css", prepend: true});
}