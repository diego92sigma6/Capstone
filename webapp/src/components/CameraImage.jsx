import React, { useState, useEffect } from 'react';
import APIRequestService from '../services/APIRequestService';
import base64encoder from '../utils/base64';

function CameraImage(props) {
    const [active, setActive] = useState(false);
    const [image, setImage] = useState(null);
    const getImage = () => {
        const serverData = APIRequestService().getImage(props.imageOID)
            .then(i => {
                //1
                //const uint8arr = new Uint8Array(i.data);
                //const barray = btoa(String.fromCharCode.apply(null, uint8arr));
                //setImage("data:image/jpeg;base64," + barray);

                //2
                //var urlCreator = window.URL || window.webkitURL;
                //let data = new Blob([uint8arr], {type: "image/jpeg"})
                //var imageUrl = urlCreator.createObjectURL(data);
                //setImage(imageUrl);

                //3
                //const barray = btoa(new Uint8Array(i.data).reduce(function (data, byte) {
                //    return data + String.fromCharCode(byte);
                //}, ''));
                
                //4
                const barray = base64encoder(new Uint8Array(i.data))
                setImage("data:image/jpeg;base64," + i.data[0].img);

                setActive(true);
            })
    }


    if (active) {
        return <img onClick={getImage} src={image} />
    } else {
        return <a onClick={getImage}>View Image</a>;
    }
}

export default CameraImage;