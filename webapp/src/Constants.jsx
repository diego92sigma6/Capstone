const SERVER_IP = `192.168.2.77`;


const Constants = {
    SERVER_URL: `${SERVER_IP}:8080`,
    SERVER_IP: SERVER_IP,
    SERVER_SOCKET_PORT: '5000',
    API_METHODS: {
        RAWDATA: 'rawdata',
        IMAGE: 'image',
        LAST_WIFI: 'lastWifiReading'
    },
    OUTPUT_TYPES: {
        CAMERA : 'camera',
        WIFI: 'wifi',
        PIEZOELECTRIC: 'piezo',
        MOTION : 'motion',
    },
    READING_INDEXES: {
        PIEZO: 0,
        MOTION: 1,
        DETECTED_0: 2,
        DETECTED_1: 3,
        AVERAGE_PWR_0: 4,
        AVERAGE_PWR_1: 5,
        MEDIAN_0: 6,
        MEDIAN_1: 7,
        VARIANCE_0: 8,
        VARIANCE_1: 9,
        DETECTED_CARS : 210
    },
    INDEX_GROUPS: {
        SENSOR: [
            "PIEZO",
            "MOTION",
        ],
        STATS: [
            "AVERAGE_PWR_0",
            "AVERAGE_PWR_1",
            "MEDIAN_0",
            "MEDIAN_1",
        ],
        STATS_2: [
            "VARIANCE_0",
            "VARIANCE_1"
        ],
        DETECTED_CARS: [
            "DETECTED_CARS"
        ]
    }
}
export default Constants;
