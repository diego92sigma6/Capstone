/**
 * @author Diego Marquez
 * @description Opens the socket to receive the live readings
 * also, it is the main container for the other components, but 
 * the first child of the App component
*/

import React from 'react'
import Constants from '../../Constants';
import io from 'socket.io-client'
import ReadingsLiveGraph from './ReadingsLiveGraph'
import SensorReadings from '../SensorReadings';
const axios = require('axios').default;

export default class Dashboard extends React.Component {


    constructor(props) {
        super(props);
        this.state = {
            plotData: []
        }
        //generate connection
        this.socket = io(`http://${Constants.SERVER_IP}:${Constants.SERVER_SOCKET_PORT}`, {
            transports: ['websocket']
        })
        this.socket.on('dashboard', (data) => {
            data = JSON.parse(data);
            this.receiveData(data);
        })
        this.socket.on('connect', (data) => {
            console.log(`socket connection status: ${this.socket.connected}`)
            this.socket.send('request');
        })
        const handleError = (data) => {
            console.log(data);
        }
        this.socket.on("connect_error", handleError)
        this.socket.on('error', handleError)
    }

    receiveData(incomingData) {
        console.log('Receiving socket data')
        let newRow = incomingData.data
        newRow = newRow.split(' ')
            .filter(col => col.length)
            .map(col => parseInt(col))
            .filter(col => !isNaN(col))
        const plotData = this.state.plotData;
        plotData.push(newRow);
        this.setState({
            plotData: plotData
        });
    }

    render() {
        return <>
        <ReadingsLiveGraph data={this.state.plotData} />
        <SensorReadings/>
        </>
    }
}