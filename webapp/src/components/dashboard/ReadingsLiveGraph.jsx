/**
 * @author Diego Marquez
 * @description Formats the readings received from the socket
 * and appends every new reading to an animated graph.
 * Four graphs are used, considering there are 4 scales to display
*/

import React from 'react'
import Constants from '../../Constants';
import '../../css/ReadingsLiveGraph.css'
import * as V from 'victory'

export default class ReadingsLiveGraph extends React.Component {

    prepareData(rawData) {
        let result = rawData.map((row, index) => {
            let entry = {};
            for (const prop in Constants.READING_INDEXES) {
                let chartGroup;
                for (const group in Constants.INDEX_GROUPS) {
                    if (Constants.INDEX_GROUPS[group].find(g => g === prop)) {
                        chartGroup = group;
                        break
                    }
                }
                entry[prop] = {
                    x: index,
                    y: row[Constants.READING_INDEXES[prop]],
                    group: chartGroup,
                }
            }
            return entry;
        });
        return result;
    }

    generateCharts(data) {
        let chartStacks = {};
        let legendData = {};
        for (const prop in Constants.READING_INDEXES) {
            let chartData = data.map(row => row[prop])
            if (chartData.length > 10) {
                chartData = chartData.slice(chartData.length - 10);
            }
            const group = chartData[0].group;
            let linePlot = <V.VictoryLine data={chartData} name={prop} />
            let legendElement = {
                name: prop
            };
            if (chartStacks[group]) {
                chartStacks[group].push(linePlot);
                legendData[group].push(legendElement);
            } else {
                chartStacks[group] = [linePlot];
                legendData[group] = [legendElement];
            }
        }
        const result = [];
        for (let group in Constants.INDEX_GROUPS) {
            result.push(
                <div className="ChartContainer">
                    <V.VictoryChart
                        key={group}
                        theme={V.VictoryTheme.grayscale}
                        height={200}
                        animate={{ duration: 1000 }}
                        containerComponent={<V.VictoryZoomContainer />}
                    >
                        <V.VictoryLegend
                            orientation="horizontal"
                            gutter={20}
                            data={legendData[group]} />
                        <V.VictoryStack>
                            {chartStacks[group]}
                        </V.VictoryStack>
                    </V.VictoryChart>
                </div>
            )
        }
        return {
            charts: result,
        }
    }

    render() {
        if (!this.props.data.length) {
            return <></>
        }
        const data = this.prepareData(this.props.data);
        let { charts } = this.generateCharts(data);
        return <div className="ReadingsLiveGraph">
            {charts}
        </div>
    }
}