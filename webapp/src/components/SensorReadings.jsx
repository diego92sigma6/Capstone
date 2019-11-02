import React, { useState, useEffect } from 'react'
import { Table } from 'react-bootstrap'
import APIRequestService from '../services/APIRequestService';
const moment = require('moment');

function SensorReadings() {
    const [data, setData] = useState([]);
    const [req, setReq] = useState(false);
    let x = 0;
    useEffect(() => {
        if (!req) {
            setReq(true);
            APIRequestService().getRawData().then(d => {
                let rows = [];
                d.forEach(d => {
                    if (d.type === 'wifi') {
                        d.data = d.data.join('\n\n');
                    } else {
                        d.data = `${d.data}`;
                    }
                    d.formattedDate = moment(d.date.$date).format('YYYY MMM DD HH:mm:ss');
                    rows.push(<tr>
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