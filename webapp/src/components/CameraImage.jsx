import React, { useState} from 'react';
import APIRequestService from '../services/APIRequestService';

function CameraImage(props) {
    const [active, setActive] = useState(false);
    const [image, setImage] = useState(null);
    const getImage = () => {
        APIRequestService().getImage(props.imageOID)
            .then(i => {
                setImage("data:image/jpeg;base64," + i.data[0].img);
                setActive(true);
            })
    }


    if (active) {
        return <img alt="" onClick={getImage} src={image} />
    } else {
        return <a onClick={getImage}>View Image</a>;
    }
}

export default CameraImage;