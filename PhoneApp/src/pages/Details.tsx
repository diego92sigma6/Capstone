/** 
@author Rishabh Rikki
@description Consumes data from REST api and displays it
*/

import React, { useState, EffectCallback } from 'react';
import { Table } from 'react-bootstrap';
import { useAsyncEffect } from 'use-async-effect'
import * as Constants from '../Constants'
import { IonBackButton, IonRow, IonCol, IonButtons, IonHeader, IonPage, IonToolbar, IonTitle, IonContent, IonGrid } from '@ionic/react';
import axios from 'axios';
import { runInThisContext } from 'vm';
const moment = require('moment');

class Details extends React.Component {

    constructor(props: any) {
        super(props)
        this.state = {
            data: null
        }
    }

    componentDidMount(){
        this.updateData();
    }
async updateData() {
        let rows: any = [];
        const result = await axios(`http://${Constants.Constants.SERVER_URL}/rawdata`, {
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        });
        //setData(result.data);
        result.data.forEach((d: any) => {
            if (d.type === 'wifi') {
                d.data = d.data.join('\n\n');
            } else if (d.type === 'camera') {
                d.data = "image";
            }
            d.formattedDate = moment(d.date.$date).format('YYYY MMM DD HH:mm:ss');
            rows.push(<IonRow key={d._id}>
                <IonCol><div>{d.type}</div></IonCol>
                <IonCol><div>{d.formattedDate}</div></IonCol>
                <IonCol><div>{d.data}</div></IonCol>
            </IonRow>)
        });
        this.setState({
            data: rows
        });
        
        /** 
         * @author Diego Marquez
         * Ensures that data is periodically polled to display last readings constantly
        */
        setTimeout(this.updateData.bind(this), 3000)
    }

render() {
    //Use React Hook to modify the state containing the rawdata from the server


    return (
        <IonPage>
            <IonHeader>
                <IonToolbar>
                    <IonButtons slot="start">
                        <IonBackButton defaultHref="/tab2" />
                    </IonButtons>
                    <IonTitle>Detail</IonTitle>
                </IonToolbar>
            </IonHeader>
            <IonContent>
                <IonGrid>
                    <IonRow>
                        <IonCol><div>Sensor Type</div></IonCol>
                        <IonCol><div>Date</div></IonCol>
                        <IonCol><div>Contents</div></IonCol>
                    </IonRow>
                    {(this.state as any).data}
                </IonGrid>
            </IonContent>
        </IonPage>
    );
}
};

export default Details;
