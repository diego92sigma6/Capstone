import React, { useState, useEffect } from 'react'
import { Table } from 'react-bootstrap'
import APIRequestService from '../services/APIRequestService';
import CameraImage from './CameraImage'
import Constants from '../Constants';
import { Row, Col } from 'react-bootstrap';
const moment = require('moment');

function SensorReadings() {
    const [data, setData] = useState([]);
    const [req, setReq] = useState(false);
    useEffect(() => {
        if (!req) {
            setReq(true);
            APIRequestService().getRawData().then(apiData => {
                setTimeout(() => setReq(false), 3000)
                let rows = [];
                apiData.data.forEach((d, index) => {
                    if (d.type === Constants.OUTPUT_TYPES.WIFI) {
                        d.data = d.data.map((cur, index) => <>{`antenna ${index}: ${cur.map(ant => JSON.parse(ant).pwr).join(',')}`}<br /></>)
                    } else if (d.type === Constants.OUTPUT_TYPES.CAMERA) {
                        d.data = <CameraImage imageOID={d.data} />;
                    } else {
                        d.data = `${d.data}`;
                    }
                    d.formattedDate = moment(d.date.$date).format('YYYY MMM DD HH:mm:ss');
                    rows.push(<tr key={`${d._id.$oid}${index}`}>
                        <td key={`${d._id.$oid}${index}type`}>{d.type}</td>
                        <td key={`${d._id.$oid}${index}date`}>{d.formattedDate}</td>
                        <td key={`${d._id.$oid}${index}data`}>{d.data}</td>
                    </tr>)
                })
                setData(rows);
            });
        }
    }, [req])

    return (
        <Row>
            <Col md="3"></Col>
            <Col>
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
            </Col>
            <Col md="3"></Col>
        </Row>
    );
}

export default SensorReadings;
