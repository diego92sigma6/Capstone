import Constants from '../Constants';
const axios = require('axios').default;

function APIRequestService() {
    return {
        getRawData: async() => {
            const result = await axios(`http://${Constants.SERVER_URL}/${Constants.API_METHODS.RAWDATA}`)
            return result;
        },
        getImage: async(imageOID) => {
            //const result = await axios(`http://${Constants.SERVER_URL}/${Constants.API_METHODS.IMAGE}/${imageOID}`,
            //{responseType: 'arraybuffer'});
            const result = await axios(`http://${Constants.SERVER_URL}/${Constants.API_METHODS.IMAGE}/${imageOID}`);
            return result;
        }
    }
}

export default APIRequestService