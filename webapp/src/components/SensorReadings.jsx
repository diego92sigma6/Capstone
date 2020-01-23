import React, { useState, useEffect } from 'react'
import { Table } from 'react-bootstrap'
import APIRequestService from '../services/APIRequestService';
import CameraImage from './CameraImage'
import Constants from '../Constants';
const moment = require('moment');

function SensorReadings() {
    const [data, setData] = useState([]);
    const [req, setReq] = useState(false);
    useEffect(() => {
        if (!req) {
            setReq(true);
            APIRequestService().getRawData().then(apiData => {
                let rows = [];
                apiData.data.forEach(d => {
                    if (d.type === Constants.OUTPUT_TYPES.WIFI) {
			d.data = d.data.antenna0 + d.data.antenna1;
                    } else if (d.type === Constants.OUTPUT_TYPES.CAMERA){
                        d.data = <CameraImage imageOID={d.data}/>;
                    } else {
                        d.data = `${d.data}`;
                    }
                    d.formattedDate = moment(d.date.$date).format('YYYY MMM DD HH:mm:ss');
                    rows.push(<tr key={d._id.$oid}>
                        <td>{d.type}</td>
                        <td>{d.formattedDate}</td>
                        <td>{d.data}</td>
                    </tr>)
                })
                setData(rows);
            });
        }
    })

    return (
        <Table striped bordered hover>
            <thead>
                <tr>
                    <th>Sensor Type</th>
                    <th>Date</th>
                    <th>Contents</th>
                </tr>
            </thead>
            <tbody>
                {data}
            </tbody>
        </Table>
    );
}

export default SensorReadings;
