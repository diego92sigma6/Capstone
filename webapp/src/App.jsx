/**
 * @author Diego Marquez
 * @description Main page. Contains the dashboard component and loads stylesheet
*/
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './css/App.css';
import Dashboard from './components/dashboard/Dashboard';

function App() {
    return (
        <>
        <Dashboard></Dashboard>
        </>
    );
}

export default App;
