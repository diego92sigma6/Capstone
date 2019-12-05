import React, { useState, EffectCallback } from 'react';
import { Table } from 'react-bootstrap';
import { useAsyncEffect } from 'use-async-effect'
import * as Constants from '../Constants'
import { IonBackButton, IonRow, IonCol, IonButtons, IonHeader, IonPage, IonToolbar, IonTitle, IonContent, IonGrid } from '@ionic/react';
import axios from 'axios';
const moment = require('moment');

function Details() {

    //Use React Hook to modify the state containing the rawdata from the server
    const [data, setData] = useState<any[]>([])
    let rows: any[] = [];

    //AJAX call to obtain the rawdata entries from the raspberry pi
    useAsyncEffect(async () => {
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
        setData(rows);
    }, []);

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
                    {data}
                </IonGrid>
            </IonContent>
        </IonPage>
    );
};

export default Details;
