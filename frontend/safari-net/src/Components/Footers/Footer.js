import * as React from 'react'
import {Container, Grid} from '@mui/material'

function Footer() {
    return (
        
        <footer style={{backgroundColor: "#212121", paddingTop: 24, paddingBottom: 24}}> 
            <Container maxWidth="lg">
                <Grid 
                    container
                    spacing={2}
                    direction="row"
                    justifyContent="space-between"
                    alignItems="flex-start">
                    <Grid item xs={8}>
                        <div style={{color:"#F1F1F1"}}>For Algeria tours: <br/>
                            31000 Oran 93 <br/>
                            Oran , AB T0B 4J5 <br/>
                            Toll Free number in N. America: +213 779686706 <br/>
                            Customer Service is open daily from 8 AM to 5 PM GMT-6 <br/>
                        </div>
                    </Grid>
                    <Grid item xs={4}>
                        <div style={{color:"#F1F1F1"}}>Safari Network</div>
                    </Grid>
                </Grid>
            </Container>
        </footer>
    )
}

export default Footer;