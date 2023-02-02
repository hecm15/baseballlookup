import React from "react";
import { useState } from "react";


export default function navDrawer(){
    const [drawer, setDrawer] = useState(false);

    return [drawer, (event) => setDrawer(!drawer)];

}