import React, { Component } from 'react'
import './css/App.css'
import Box from './components/Box'

export default class App extends Component {
    render() {
        return (
            <div className="App center">
                <Box area="서울" all={10} today={100} />
                <Box area="서울" all={10} today={100} />
                <Box area="서울" all={10} today={100} />
            </div>
        )
    }
}
