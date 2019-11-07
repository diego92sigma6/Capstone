import Constants from '../Constants';
const axios = require('axios').default;

function APIRequestService() {
    return {
        getRawData: async() => {
            const result = await axios(`http://${Constants.SERVER_URL}/rawdata`);
            return result.data;
        }
    }
}

export default APIRequestService