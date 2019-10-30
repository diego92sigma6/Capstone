import React, {useState, EffectCallback} from 'react';
import {useAsyncEffect} from 'use-async-effect'
import * as Constants from '../Constants'
import { IonBackButton, IonButtons, IonHeader, IonPage, IonToolbar, IonTitle, IonContent } from '@ionic/react';
import axios from 'axios';

function Details() {

    //Use React Hook to modify the state containing the rawdata from the server
    const [data, setData ] = useState({rawdata : []})

    //AJAX call to obtain the rawdata entries from the raspberry pi
    useAsyncEffect(async () => {
        const result = await axios(`http://${Constants.Constants.SERVER_URL}/rawdata`);
        setData(result.data);
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
                <p>{JSON.stringify(data) }</p>
            </IonContent>
        </IonPage>
    );
};

export default Details;
