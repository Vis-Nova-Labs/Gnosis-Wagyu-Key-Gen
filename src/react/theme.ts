import { createTheme } from "@material-ui/core";
import { green, blue } from "@material-ui/core/colors";
import { GnosisGreen } from "./colors";


const theme = createTheme({
  palette: {
    type: "dark",
    primary: green,
    secondary: blue,
  },
  typography: {
    h1: {
      fontSize: "36px",
      justifyContent: "Center"
    }
  }
});


export default theme;